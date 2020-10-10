from classes.BaseRoleplayCommand import BaseRoleplayCommand


class Main(BaseRoleplayCommand):
    command = "moan"
    description = "pervert"
    usage = "moan <user>"
    no_mention_response = "*moans*"
    self_response = ":smirk:"
    bot_response = "*moans*"
    action = "*{mentioned} moans*"
