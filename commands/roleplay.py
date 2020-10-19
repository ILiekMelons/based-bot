from classes.BaseCommandGroup import BaseCommandGroup
from classes.BaseRoleplayCommand import BaseRoleplayCommand
from classes.BaseResponseCommand import BaseResponseCommand
from classes.Client import Client


class Main:
    group_name = "Roleplay"

    def __init__(self, client: Client):
        self.GROUP = BaseCommandGroup(client, self.group_name)
        commands = [
            BaseRoleplayCommand(
                client,
                "hug",
                "{author} hugged {mentioned} :heart:",
                description="hug your friends",
                self_response="You can't hug yourself, unfortunately.",
                bot_response="I'm here for you :heart:",
                no_mention_response="Mention someone to hug them!",
                group=self.GROUP
            ),
            BaseRoleplayCommand(
                client,
                "kiss",
                "{author} kissed {mentioned} :heart:",
                description="kiss your friends",
                self_response="That's sad.",
                bot_response="No.",
                group=self.GROUP
            ),
            BaseRoleplayCommand(
                client,
                "kill",
                "{author} murdered {mentioned} :knife:",
                description="kill your friends",
                self_response="Please don't.",
                bot_response="*dies*",
                no_mention_response="Who are you trying to kill?",
                group=self.GROUP
            ),
            BaseRoleplayCommand(
                client,
                "marry",
                "{author} married {mentioned} :ring:",
                description="marry your friends",
                self_response="No.",
                bot_response="I don't :broken_heart:",
                no_mention_response="If you can't mention someone to marry this relationship may be doomed",
                group=self.GROUP
            ),
            BaseRoleplayCommand(
                client,
                "divorce",
                "{author} divorced {mentioned} :broken_heart:",
                description="divorce your friends",
                self_response="You can't divorce yourself.",
                bot_response=":sob:",
                no_mention_response="Are you willing to let go?",
                group=self.GROUP
            ),
            BaseRoleplayCommand(
                client,
                "sex",
                "{author} divorced {mentioned} :broken_heart:",
                description="look what you've reduced me to",
                self_response="No.",
                bot_response="*moans*",
                no_mention_response="You don't have to.",
                group=self.GROUP
            ),
            BaseRoleplayCommand(
                client,
                "sex",
                "{author} divorced {mentioned} :broken_heart:",
                description="look what you've reduced me to",
                self_response="No.",
                bot_response="*moans*",
                no_mention_response="You don't have to.",
                group=self.GROUP
            ),
            BaseRoleplayCommand(
                client,
                "punch",
                "{author} punched {mentioned} :fist:",
                description="punch your friends",
                self_response="Punch yourself.",
                bot_response="Ouch.",
                group=self.GROUP
            ),
            BaseResponseCommand(
                client,
                "cry",
                "{author} is crying.",
                group=self.GROUP
            )
        ]