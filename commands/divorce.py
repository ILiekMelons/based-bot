from classes.BaseRoleplayCommand import BaseRoleplayCommand


class Main(BaseRoleplayCommand):
    command = "divorce"
    description = "divorce your friends"
    usage = "divorce <user>"
    no_mention_response = "You don't have to sign the paperwork."
    self_response = "No."
    bot_response = ":sob:"
    action = "{author} divorced {mentioned} :broken_heart:"
