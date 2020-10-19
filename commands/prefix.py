import discord
from classes.BaseCommand import BaseCommand
from classes.CommandInfo import CommandInfo


class Main(BaseCommand):
    info = CommandInfo(
        "changeprefix",
        "changeprefix <prefix>",
        short_description="Changes this server's prefix."
    )