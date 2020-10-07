from classes.BaseResponseCommand import BaseResponseCommand


class Main(BaseResponseCommand):
    command = "cry"
    description = "cry"
    usage = "cry"
    response = "{author} is crying."
