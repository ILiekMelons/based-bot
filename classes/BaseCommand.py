import discord


class Command:
    command = "undefined"
    description = "undefined"
    usage = "undefined"
    isNsfw = False

    def __init__(self, client: discord.Client):
        self.CLIENT = client