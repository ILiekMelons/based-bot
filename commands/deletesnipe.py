import discord
from classes.BaseCommand import Command


class Main(Command):
    command = "deletesnipe"
    description = "ruin your friendships with this command"
    usage = "deletesnipe"

    async def handle(self, message: discord.Message):
        if not message.guild:
            return
        try:
            del_message = self.CLIENT.VARS["recently_deleted"][message.guild.id]
            del_author = del_message.author
            author_formatted = f"{del_author.name}#{del_author.discriminator} ({del_author.id})"
            date_formatted = str(del_message.created_at)
            await message.channel.send(f"Last deleted message:\n{author_formatted}: {del_message.clean_content}\nSent at {date_formatted}")
        except ValueError:
            await message.channel.send("No recently deleted messages.")

