import discord
from classes.Client import Client


class Command:
    command = "undefined"
    description = "undefined"
    usage = "undefined"
    isNsfw = False

    def __init__(self, client: Client):
        self.CLIENT = client

    async def handle(self, message: discord.Message):
        await message.channel.send("Not implemented")