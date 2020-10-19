import asyncio
from classes.CommandInfo import CommandInfo


class CommandHandler:
    def __init__(self, command: str, handler: asyncio.coroutine, info: CommandInfo):
        self.command = command
        self.handle = handler
        self.info = info
