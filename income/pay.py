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

class pay():
    @commands.command()
    async def pay(self, ctx, member: discord.Member, amount = None):
        users = await get_bank_data()
        if str(ctx.author.id) not in users:
            await ctx.send('Gõ `vbalance` trước')
            return
        if str(member.id) not in users:
            await ctx.send('Người chơi này chưa có tài khoản')
            return
        if amount == None or amount == 0:
            return
        bal = await update_bank(ctx.author)
        if amount == 'all':
            amount = str(bal[0])
        def convert_str_to_number(x): #x truyền vào phải là string
            total_stars = 0
            num_map = {'k':1000, 'K':1000, 'm':1000000, 'M':1000000, 'b':1000000000, 'B':1000000000}
            if x.isdigit():
                total_stars = int(x)
            else:
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
        await update_bank(ctx.author, -1*amount, 'wallet')
        await update_bank(member, amount, 'wallet')
        await ctx.send(f'Chuyển {amount}VND cho {member.mention}')