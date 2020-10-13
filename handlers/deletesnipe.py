from classes.BaseEventHandler import BaseEventHandler
import discord


class Main(BaseEventHandler):
    event = "on_message_delete"

    async def handle(self, message: discord.Message):
        if not message.guild:
            return

        client_vars = self.CLIENT.VARS

        if "recently_deleted" not in client_vars:
            client_vars["recently_deleted"] = {}

        recently_deleted = client_vars["recently_deleted"]
        recently_deleted[message.guild.id] = message
