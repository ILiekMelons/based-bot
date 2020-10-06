import discord


class Main:
    command = "test"

    def __init__(self, client: discord.Client):
        self.CLIENT = client

    async def handle(self, message: discord.Message):
        authormention = message.author.
        await message.channel.send('hello')
        return True
