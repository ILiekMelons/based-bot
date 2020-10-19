import discord
from classes.BaseCommand import BaseCommand
from classes.CommandInfo import CommandInfo


class Main(BaseCommand):
    info = CommandInfo(
        "test",
        short_description="testing testing"
    )

    async def handle(self, message: discord.Message):
        await message.channel.send('hello')
        return True
