import discord
import random
import time
from classes.BaseCommand import BaseCommand
from classes.CommandInfo import CommandInfo

responses = [
        "As I see it, yes",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don’t count on it",
        "It is certain",
        "It is decidedly so",
        "Most likely",
        "My reply is no",
        "My sources say no",
        "Outlook good",
        "Outlook not so good",
        "Reply hazy, try again",
        "Signs point to yes",
        "Very doubtful",
        "Without a doubt",
        "Yes",
        "Yes definitely",
        "You may rely on it"
]


class Main(BaseCommand):
    info = CommandInfo(
        "8ball",
        short_description="decide your fate"
    )

    random.seed(time.time())

    async def handle(self, message: discord.Message):
        await message.channel.send(f'{message.author.mention}: {random.choice(responses)}')
