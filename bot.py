import os
from classes.Client import Client

TOKEN = os.environ['TOKEN']

Client().run(TOKEN)
