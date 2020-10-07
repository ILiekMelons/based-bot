from classes.BaseRoleplayCommand import BaseRoleplayCommand


class Main(BaseRoleplayCommand):
    command = "hug"
    description = "hug your friends"
    usage = "hug <user>"
    no_mention_response = "Mention someone to hug them!"
    self_response = "It's okay, you'll find someone soon.."
    bot_response = "I'm here for you."
    action = "{author} hugged {mentioned} :heart:"
