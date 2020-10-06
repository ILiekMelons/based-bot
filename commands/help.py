import discord
from classes.BaseCommand import Command


class Main(Command):
    command = "help"
    description = "lists commands or gets specific command info"
    usage = "help <command?>"

    async def handle(self, message: discord.Message):
        try:
            command = message.content.split()[1]
            command = [x for x in self.CLIENT.COMMANDS if x.command == command]
            if len(command) != 0:
                command = command[0]
                await message.channel.send(f'{self.CLIENT.PREFIX}{command.command}:\nusage: {self.CLIENT.PREFIX}{command.usage}')
            else:
                await message.channel.send(f'Invalid command, type {self.CLIENT.PREFIX}help for a list of commands')
            return True

        except IndexError:
            commands = [f'{self.CLIENT.PREFIX}{x.command}: {x.description}' for x in self.CLIENT.COMMANDS]
            await message.channel.send("\n".join(commands) + f'\nType {self.CLIENT.PREFIX}help <command> for usage')
            return True
