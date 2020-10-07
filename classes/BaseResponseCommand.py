from classes.BaseCommand import Command
import discord


class BaseResponseCommand(Command):
    response = "Not implemented"

    async def handle(self, message: discord.Message):
        await message.channel.send(self.response.format(author=message.author.mention))
