import discord
from classes.Client import Client
from classes.CommandHandler import CommandHandler


class BaseCommand:
    def __init__(self, client: Client, group=None):
        self.CLIENT = client

        if not group:
            group = client.DEFAULT_GROUP
        if not hasattr(self, "command"):
            self.command = self.info.command
        # Registering our command
        command = CommandHandler(self.command, self.handle, self.info)
        group.register_command(command)

    async def handle(self, message: discord.Message):
        await message.channel.send("Not implemented")
