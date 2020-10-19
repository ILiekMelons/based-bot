from classes.BaseCommand import BaseCommand
from classes.CommandInfo import CommandInfo
import discord


class BaseResponseCommand(BaseCommand):
    def __init__(self, client, command, response, group=None, description=None):
        self.command = command
        self.response = response
        self.info = CommandInfo(
            command,
            short_description=description
        )
        super().__init__(client, group)

    async def handle(self, message: discord.Message):
        await message.channel.send(self.response.format(author=message.author.mention))
