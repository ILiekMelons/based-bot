import discord
from classes.BaseCommand import Command


class Main(Command):
    command = "kick"
    description = "kick people you don't like"
    usage = "kick <user>"

    async def handle(self, message: discord.Message):
        permissions = message.channel.permissions_for(message.author)
        try:
            to_kick = message.mentions[0]
            if permissions.kick_members:
                await message.guild.kick(to_kick)
                await message.channel.send("Kicked")
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