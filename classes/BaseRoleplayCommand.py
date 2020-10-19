import discord
from classes.BaseCommand import BaseCommand
from classes.CommandInfo import CommandInfo
from classes.Client import Client


class BaseRoleplayCommand(BaseCommand):
    no_mention_response = "Please mention someone!"
    self_response = False
    bot_response = False
    action = "Not implemented"

    def __init__(self,
                 client: Client,
                 command: str,
                 action: str,
                 description=None,
                 self_response=False,
                 bot_response=False,
                 no_mention_response="Please mention someone!",
                 group=None):
        self.CLIENT = client
        self.action = action
        self.self_response = self_response
        self.bot_response = bot_response
        self.no_mention_response = no_mention_response
        self.info = CommandInfo(
            command,
            short_description=description,
        )
        super().__init__(client, group)

    async def handle(self, message: discord.Message):
        if len(message.mentions) == 0:
            await message.channel.send(self.no_mention_response)
            return True

        author = message.author
        mentioned = message.mentions[0]

        if author == mentioned and type(self.self_response) is str:
            await message.channel.send(self.self_response)
            return True

        if mentioned == self.CLIENT.user and type(self.bot_response) is str:
            await message.channel.send(self.bot_response)
            return True

        await message.channel.send(self.action.format(author=author.mention, mentioned=mentioned.mention))
        return True
