import discord
from classes.BaseCommand import Command


class Main(Command):
    command = "hug"
    description = "hug someone"
    usage = "hug <user>"

    async def handle(self, message: discord.Message):
        if len(message.mentions) == 0:
            await message.channel.send('You can\'t hug air.')
            return True

        author = message.author
        hugged = message.mentions[0]

        if author == hugged:
            await message.channel.send('It\'s okay, you\'ll find someone soon..')
            return True

        if hugged == self.CLIENT.user:
            await message.channel.send('I\'m here for you.')
            return True

        await message.channel.send(f'{author.mention} hugged {hugged.mention} :heart:')
        return True
