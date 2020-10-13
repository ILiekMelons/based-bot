from classes.Client import Client
import discord

class Main:
    event = "on_message"

    def __init__(self, client: Client):
        self.CLIENT = client

    async def handle(self, *args):
        self.CLIENT.logger.debug("I just recieved an event!")

