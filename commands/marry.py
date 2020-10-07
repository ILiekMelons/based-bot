from classes.BaseRoleplayCommand import BaseRoleplayCommand


class Main(BaseRoleplayCommand):
    command = "marry"
    description = "marry your friends"
    usage = "marry <user>"
    no_mention_response = "If you can't mention someone to marry this relationship may be doomed"
    self_response = "That's sad."
    bot_response = "I don't :broken_heart:"
    action = "{author} married {mentioned} :ring:"
