from classes.CommandHandler import CommandHandler


class BaseCommandGroup:
    group_name = "Ungrouped"
    commands = []

    def __init__(self, client, group_name: str):
        self.CLIENT = client
        self.group_name = group_name
        client.register_group(self)

        for command in self.commands:
            self.register_command(command)

    def register_command(self, command: CommandHandler):
        self.CLIENT.register_command(command, self)
