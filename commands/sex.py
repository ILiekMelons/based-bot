from classes.BaseRoleplayCommand import BaseRoleplayCommand


# look at what you've reduced me to
class Main(BaseRoleplayCommand):
    command = "sex"
    description = "look what you've reduced me to"
    usage = "sex <user>"
    no_mention_response = "Maybe you're just not ready yet. We'll wait."
    self_response = "No."
    bot_response = "*moans*"
    action = "{author} had sex with {mentioned} :smirk:"
