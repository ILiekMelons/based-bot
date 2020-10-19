import discord
import os
import importlib
import logging
import time
from classes.CommandHandler import CommandHandler
from classes.BaseCommandGroup import BaseCommandGroup


class Client(discord.Client):
    COMMANDS = set()
    HANDLERS = set()
    GROUPS = set()
    INFO = set()
    VARS = {}

    try:
        PREFIX = os.environ['PREFIX']
    except KeyError:
        PREFIX = "x!"

    def __init__(self):
        # logging idiocy
        logger = logging.getLogger('client')
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        self.logger = logger

        self.DEFAULT_GROUP = BaseCommandGroup(self, "Ungrouped")

        logger.info("================= START =================")
        start = time.process_time()
        super().__init__()
        init = time.process_time()

        for module_name in os.listdir(os.path.dirname("commands/")):
            if module_name == '__init__.py' or module_name[-3:] != '.py':
                continue
            module = importlib.import_module("commands." + module_name.replace(".py", ""))
            if module.Main:
                logger.info(f"Loading command {module_name}")
                module.Main(self)
            else:
                logger.warning(f"Skipping command {module_name} as it does not have a main class")
        logger.info("============ LOADED COMMANDS ============")
        commands = time.process_time()

        for handler_name in os.listdir(os.path.dirname("handlers/")):
            if handler_name == '__init__.py' or handler_name[-3:] != '.py':
                continue

            handler = importlib.import_module("handlers." + handler_name.replace(".py", ""))
            try:
                if handler.Main:
                    main_class = handler.Main(self)
                    logger.info(f"Loading handler {handler_name} ({main_class.event})")

                    # registering the handler with the client
                    setattr(self, main_class.event, main_class.handle)

                    self.HANDLERS.add(main_class)
                else:
                    logger.warning(f"Skipping handler {handler_name} because it does not have a main class")
            except AssertionError as error:
                logger.error(f"An assertion error was raised while loading {handler_name}: {error}")
                logger.error("Continuing anyway.")
            except BaseException as error:
                logger.fatal(f"An unknown error was raised while loading {handler_name}: {error}")
                logger.fatal("Exiting.")
                exit(1)
        logger.info("============ LOADED HANDLERS ============")
        handlers = time.process_time()
        logger.info(f"Loaded in {handlers - start}s")
        logger.debug(f"Initial load time: {init - start}s")
        logger.debug(f"BaseCommand load time: {commands - init}s")
        logger.debug(f"Handler load time: {handlers - commands}s")

    async def on_message(self, message: discord.Message):
        logger = self.logger
        if message.author == self.user or message.content[0:len(self.PREFIX)] != self.PREFIX:
            return

        logger.info("Received command " + message.content)

        command = message.content.replace(self.PREFIX, "").split()[0]
        available = [x for x in self.COMMANDS if x.command == command]

        for handler in available:
            result = await handler.handle(message)
            if result:
                break

    def register_command(self, command: CommandHandler, group: BaseCommandGroup):
        assert isinstance(command, CommandHandler), "Command is not a CommandHandler!"
        assert isinstance(group, BaseCommandGroup), "Group is not a BaseCommandGroup!"
        assert group in self.GROUPS, "Group is not registered!"
        self.COMMANDS.add(command)

    def register_group(self, group: BaseCommandGroup):
        assert isinstance(group, BaseCommandGroup), "Group is not a BaseCommandGroup!"
        self.GROUPS.add(group)
