import discord
from classes.BaseCommand import Command


class Main(Command):
    command = "changeprefix"
    description = "change the prefix"
    usage = "changeprefix <newprefix>"