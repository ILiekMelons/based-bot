from classes.BaseRoleplayCommand import BaseRoleplayCommand


class Main(BaseRoleplayCommand):
    command = "kiss"
    description = "kiss your friends"
    usage = "kiss <user>"
    no_mention_response = "Mention someone to kiss!"
    self_response = "That's sad."
    bot_response = "No thanks."
    action = "{author} kissed {mentioned} :kissing_heart:"
