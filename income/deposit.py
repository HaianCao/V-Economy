import discord
from discord.ext import commands
from discord.ext.commands.core import command
import time
import random
import json
import os

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

class deposit():
    @commands.command()
    async def deposit(self, ctx, amount = None):
        users = await get_bank_data()
        if str(ctx.author.id) not in users:
            await ctx.send('Gõ `vbalance` trước')
            return
        if amount == None or amount == 0:
            return
        bal = await update_bank(ctx.author)
        if amount == 'all':
            amount = str(bal[0])
        def convert_str_to_number(x):
            total_stars = 0
            num_map = {'k':1000, 'K':1000, 'm':1000000, 'M':1000000, 'b':1000000000, 'B':1000000000}
            if x.isdigit():
                total_stars = int(x)
            else:
                if amount == bal[0]: return
                if len(x) > 1:
                    total_stars = float(x[:-1]) * num_map.get(x[-1].upper(), 1)
            return int(total_stars)
        amount = convert_str_to_number(amount)
        if amount > bal[0]:
            await ctx.send('Vượt lượng tiền trong wallet')
            return
        if amount < 0:
            await ctx.send('Lượng tiền không thể bé hơn 0')
            return
        await update_bank(ctx.author, -1*amount)
        await update_bank(ctx.author, amount, 'bank')
        await ctx.send(f'Chuyển {amount}VND vào ngân hàng')

    @commands.command()
    async def dep(self, ctx, amount = None):
        users = await get_bank_data()
        if str(ctx.author.id) not in users:
            await ctx.send('Gõ `vbalance` trước')
            return
        if amount == None or amount == 0:
            return
        bal = await update_bank(ctx.author)
        if amount == 'all':
            amount = str(bal[0])
        def convert_str_to_number(x):
            total_stars = 0
            num_map = {'k':1000, 'K':1000, 'm':1000000, 'M':1000000, 'b':1000000000, 'B':1000000000}
            if x.isdigit():
                total_stars = int(x)
            else:
                if amount == bal[0]: return
                if len(x) > 1:
                    total_stars = float(x[:-1]) * num_map.get(x[-1].upper(), 1)
            return int(total_stars)
        amount = convert_str_to_number(amount)
        if amount > bal[0]:
            await ctx.send('Vượt lượng tiền trong wallet')
            return
        if amount < 0:
            await ctx.send('Lượng tiền không thể bé hơn 0')
            return
        await update_bank(ctx.author, -1*amount)
        await update_bank(ctx.author, amount, 'bank')
        await ctx.send(f'Chuyển {amount}VND vào ngân hàng')