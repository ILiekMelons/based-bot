import discord
from classes.BaseCommand import Command


class Main(Command):
    command = "editsnipe"
    description = "ruin your friendships with this command"
    usage = "editsnipe"

    async def handle(self, message: discord.Message):
        if not message.guild:
            return

        try:
            cid = message.content.split()[1]
        except ValueError:
            cid = message.channel.id

        try:
            messages = self.CLIENT.VARS["recently_edited"][message.guild.id][cid]
            old_message = messages[0]
            new_message = messages[1]
            author = new_message.author
            author_formatted = f"{author.name}#{author.discriminator}"
            date_formatted = str(old_message.created_at) + "UTC"
            date_edited = str(new_message.edited_at) + "UTC"
            await message.channel.send(f"Last edited message by {author_formatted}:\n**Old message:** {old_message.clean_content}\n**New message:** {new_message.clean_content}\nSent at {date_formatted}\nEdited at {date_edited}")
        except ValueError:
            await message.channel.send("No recently edited messages.")

