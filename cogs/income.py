import discord
from discord.ext import commands
import random
import time
from income.balance import balance
from income.deposit import deposit
from income.withdraw import withdraw
from income.work import work
from income.pay import pay
from discord.ext.commands.core import command



class income(commands.Cog, balance, work, deposit, withdraw, pay):
    def __init__(self, client):
        self.client = client
        self.balance = balance
        self.work = work
        self.deposit = deposit
        self.withdraw = withdraw
        self.pay = pay

        
def setup(client):
    client.add_cog(income(client))