import discord
import os
import importlib
import logging
import time


class Client(discord.Client):
    COMMANDS = set()
    HANDLERS = set()
    VARS = {}

    try:
        PREFIX = os.environ['PREFIX']
    except KeyError:
        PREFIX = "x!"

    def __init__(self, *args, loop=None, **kwargs):

        # logging idiocy
        logger = logging.getLogger('client')
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        self.logger = logger

        logger.info("================= START =================")
        start = time.process_time()
        super().__init__(*args, loop=loop, **kwargs)
        init = time.process_time()

        for module in os.listdir(os.path.dirname("commands/")):
            if module == '__init__.py' or module[-3:] != '.py':
                continue
            logger.info("Loading command " + module)
            module = importlib.import_module("commands." + module.replace(".py", ""))
            mclass = module.Main(self)

            self.COMMANDS.add(mclass)
        logger.info("============ LOADED COMMANDS ============")
        commands = time.process_time()

        for handler in os.listdir(os.path.dirname("handlers/")):
            if handler == '__init__.py' or handler[-3:] != '.py':
                continue

            name = handler
            handler = importlib.import_module("handlers." + handler.replace(".py", ""))
            mclass = handler.Main(self)
            logger.info(f"Loading handler {name} ({mclass.event})")

            # registering the handler with the client
            setattr(self, mclass.event, mclass.handle)

            self.HANDLERS.add(mclass)
        logger.info("============ LOADED HANDLERS ============")
        handlers = time.process_time()
        logger.info(f"Loaded in {handlers - start}s")
        logger.debug(f"Initial load time: {init - start}s")
        logger.debug(f"Command load time: {commands - init}s")
        logger.debug(f"Handler load time: {handlers - commands}s")

    async def on_message(self, message: discord.Message):
        logger = self.logger
        if message.author == self.user or message.content[0:len(self.PREFIX)] != self.PREFIX:
            return

        logger.info("Recieved command " + message.content)

        command = message.content.replace(self.PREFIX, "").split()[0]
        available = [x for x in self.COMMANDS if x.command == command]

        for handler in available:
            result = await handler.handle(message)
            if result:
                break


