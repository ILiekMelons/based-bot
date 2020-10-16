from classes.BaseEventHandler import BaseEventHandler
import discord


class Main(BaseEventHandler):
    event = "on_message_edit"

    async def handle(self, old_message: discord.Message, new_message: discord.Message):
        if not old_message.guild:
            return

        client_vars = self.CLIENT.VARS

        if "recently_edited" not in client_vars:
            client_vars["recently_edited"] = {}

        recently_edited = client_vars["recently_edited"]

        if old_message.guild.id not in recently_edited:
            recently_edited[old_message.guild.id] = {}

        server_edited = recently_edited[old_message.guild.id]
        server_edited[old_message.channel.id] = [old_message, new_message]
