import discord
from classes.BaseCommand import Command


class Main(Command):
    command = "deletesnipe"
    description = "ruin your friendships with this command"
    usage = "deletesnipe <channel id>"

    async def handle(self, message: discord.Message):
        if not message.guild:
            return

        try:
            cid = int(message.content.split()[1])
        except IndexError:
            cid = message.channel.id
        except ValueError:
            await message.channel.send("Please specify a correct channel ID.")
            return True

        try:
            del_message = self.CLIENT.VARS["recently_deleted"][message.guild.id][cid]
            del_author = del_message.author
            author_formatted = f"{del_author.name}#{del_author.discriminator}"
            date_formatted = str(del_message.created_at) + "UTC"
            await message.channel.send(f"Last deleted message:\n{author_formatted}: {del_message.clean_content}\nSent at {date_formatted}")
        except KeyError:
            await message.channel.send("No recently deleted messages for that channel.")

