class CommandInfo:
    def __init__(self, command, usage=False, short_description="No description given.", long_description=False, is_nsfw=False):
        self.command = command
        self.usage = usage or command
        self.short_description = short_description
        self.long_description = long_description or short_description
        self.is_nsfw = is_nsfw