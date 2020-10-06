import discord


class Main:
    command = "test"
    description = "testing testing"
    usage = "x!test"
    isNsfw = False

    def __init__(self, client: discord.Client):
        self.CLIENT = client

    async def handle(self, message: discord.Message):
        await message.channel.send('hello')
        return True
