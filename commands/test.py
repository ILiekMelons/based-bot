import discord
from classes.BaseCommand import Command


class Main(Command):
    command = "test"
    description = "testing testing"
    usage = "test"

    async def handle(self, message: discord.Message):
        await message.channel.send('hello')
        return True
