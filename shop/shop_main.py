import discord
from discord.ext import commands
from discord.ext.commands.core import command
import time
import random
import json
import os
from food import food_shop

os.chdir("C:\\Users\\Admin\\OneDrive\\Desktop\\Programing\\Discord\\V-Economy")


async def get_bank_data():
    with open('users_data.json', 'r') as f:
        users = json.load(f)
    return users

async def update_bank(user, change = 0, mode = 'wallet'):
    users = await get_bank_data()
    users[str(user.id)][mode] += change
    with open('users_data.json', 'w') as f:
        json.dump(users, f)
    bal = [users[str(user.id)]['wallet'], users[str(user.id)]['bank']] 
    return bal



