from classes.BaseRoleplayCommand import BaseRoleplayCommand


class Main(BaseRoleplayCommand):
    command = "punch"
    description = "punch your friends"
    usage = "punch <user>"
    no_mention_response = "Mention someone to punch!"
    self_response = "You punched yourself!"
    bot_response = "Ouch."
    action = "{author} punched {mentioned}!"
