import discord
import os
import importlib


class Client(discord.Client):
    COMMANDS = set()
    HANDLERS = set()
    VARS = []
    PREFIX = "x!"

    def __init__(self, *args, loop=None, **kwargs):
        super().__init__(*args, loop=loop, **kwargs)

        for module in os.listdir(os.path.dirname("commands/")):
            if module == '__init__.py' or module[-3:] != '.py':
                continue
            print("Loading module " + module)
            module = importlib.import_module("commands." + module.replace(".py", ""))
            mclass = module.Main(self)
            self.COMMANDS.add(mclass)
        print("loaded commands")

    async def on_message(self, message: discord.Message):
        if message.author == self.user or message.content[0:len(self.PREFIX)] != self.PREFIX:
            return

        command = message.content.replace(self.PREFIX, "").split()[0]
        available = [x for x in self.COMMANDS if x.command == command]

        for handler in available:
            result = await handler.handle(message)
            if result:
                break