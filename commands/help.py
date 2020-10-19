import discord
from classes.BaseCommand import BaseCommand
from classes.CommandInfo import CommandInfo


class Main(BaseCommand):
    info = CommandInfo(
        "help",
        "help <command?>",
        short_description="lists commands or gets specific command info"
    )

    async def handle(self, message: discord.Message):
        try:
            command = message.content.split()[1]
            command = [x for x in self.CLIENT.COMMANDS if x.command == command]
            if len(command) != 0:
                command = command[0]
                info: CommandInfo = command.info
                await message.channel.send(f'{self.CLIENT.PREFIX}{info.command}:\ndescription: {info.long_description}\nusage: {self.CLIENT.PREFIX}{info.usage}')
            else:
                await message.channel.send(f'Invalid command, type {self.CLIENT.PREFIX}help for a list of commands')
            return True

        except IndexError:
            commands = [f'{self.CLIENT.PREFIX}{x.info.command}: {x.info.short_description}' for x in self.CLIENT.COMMANDS]
            await message.channel.send("\n".join(commands) + f'\nType {self.CLIENT.PREFIX}help <command> for usage')
            return True
