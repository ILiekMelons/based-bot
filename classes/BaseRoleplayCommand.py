import discord
from classes.BaseCommand import Command


class BaseRoleplayCommand(Command):
    no_mention_response = "Please mention someone!"
    self_response = False
    bot_response = False
    action = "Not implemented"

    async def handle(self, message: discord.Message):
        if len(message.mentions) == 0:
            await message.channel.send(self.no_mention_response)
            return True

        author = message.author
        mentioned = message.mentions[0]

        if author == mentioned and not self.self_response:
            await message.channel.send(self.self_response)
            return True

        if mentioned == self.CLIENT.user and not self.bot_response:
            await message.channel.send(self.self_response)
            return True

        await message.channel.send(self.action.format(author=author.mention, mentioned=mentioned.mention))
        return True
