from classes.BaseRoleplayCommand import BaseRoleplayCommand


class Main(BaseRoleplayCommand):
    command = "kill"
    description = "kill your friends"
    usage = "kill <user>"
    no_mention_response = "You take a knife out, only to realize you haven't mentioned anyone"
    self_response = "Please don't."
    action = "{author} murdered {mentioned} :knife:"
