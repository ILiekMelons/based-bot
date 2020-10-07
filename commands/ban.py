import discord
from classes.BaseCommand import Command


class Main(Command):
    command = "ban"
    description = "ban people you don't like"
    usage = "ban <user>"

    async def handle(self, message: discord.Message):
        permissions = message.channel.permissions_for(message.author)
        try:
            to_ban = message.mentions[0]
            if permissions.ban_members:
                await message.guild.ban(to_ban)
                await message.channel.send("Banned")
                return True
            else:
                await message.channel.send("You're not allowed to do that.")
                return True
        except IndexError:
            await message.channel.send("Please mention a user.")
            return True
        except discord.Forbidden as e:
            print(e)
            await message.channel.send("I'm not allowed to do that.")
            return True
        return False