import discord
from discord.ext import commands
import random
import time
from games.gamble import gamble
from games.rps import rps


class game(commands.Cog, gamble, rps):
    def __init__(self, client):
        self.client = client
        self.gamble = gamble
        self.rps = rps

        
def setup(client):
    client.add_cog(game(client))