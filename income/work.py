import discord
from discord import client
from discord.ext import commands
from discord.ext.commands.core import command
from discord.ext.commands import cooldown, BucketType
import time
import random
import json
import os
from datetime import datetime, timedelta    

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

id_work_on_cooldown = {} # Dictionary with user IDs as keys and datetime as values     
work_cooldown = 900 # cooldown of the move command in seconds
class work(): 
    @commands.command()
    async def work(self, ctx):
        users = await get_bank_data()
        if str(ctx.author.id) not in users:
            await ctx.send('Bạn chưa có định danh. Gõ `vbalance` trước tiên để tạo mã định danh')
            return
        user = ctx.author
        # author = ctx.author.id
        try:
            # calculate the amount of time since the last (successful) use of the command
            last_move = datetime.now() - id_work_on_cooldown[user.id] 
        except KeyError:
            # the key doesn't exist, the player used the command for the first time
            # or the bot has been shut down since
            last_move = None
            id_work_on_cooldown[user.id] = datetime.now()
        if last_move is None or last_move.seconds > work_cooldown:
            earning = random.randint(100000, 300000)
            await ctx.send(f'Bạn thăm ngàn và nhận được {earning}VND')
            users[str(user.id)]['wallet'] += earning
            with open('users_data.json', 'w') as f:
                json.dump(users, f)
        else:
            time_left = work_cooldown-last_move.seconds
            if time_left >= 3600:
                time_left_hours = round((time_left // 60) // 60) 
                await ctx.send(f"Bạn chỉ có thể sử dụng lại command `work` sau {time_left_hours} giờ")    
            if 60 <= time_left < 3600:
                time_left_minutes = round(time_left // 60) 
                await ctx.send(f"Bạn chỉ có thể sử dụng lại command `work` sau  {time_left_minutes} phút")    
            if time_left < 60:
                time_left_seconds = round(time_left) 
                await ctx.send(f"Bạn chỉ có thể sử dụng lại command `work` sau  {time_left_seconds} giây")    

    @commands.command()
    async def w(self, ctx):
        users = await get_bank_data()
        if str(ctx.author.id) not in users:
            await ctx.send('Bạn chưa có định danh. Gõ `vbalance` trước tiên để tạo mã định danh')
            return
        user = ctx.author
        # author = ctx.author.id
        try:
            # calculate the amount of time since the last (successful) use of the command
            last_move = datetime.now() - id_work_on_cooldown[user.id] 
        except KeyError:
            # the key doesn't exist, the player used the command for the first time
            # or the bot has been shut down since
            last_move = None
            id_work_on_cooldown[user.id] = datetime.now()
        if last_move is None or last_move.seconds > work_cooldown:
            earning = random.randint(100000, 300000)
            await ctx.send(f'Bạn thăm ngàn và nhận được {earning}VND')
            users[str(user.id)]['wallet'] += earning
            with open('users_data.json', 'w') as f:
                json.dump(users, f)
        else:
            time_left = work_cooldown-last_move.seconds
            if time_left >= 3600:
                time_left_hours = round((time_left // 60) // 60) 
                await ctx.send(f"Bạn chỉ có thể sử dụng lại command `work` sau {time_left_hours} giờ")    
            if 60 <= time_left < 3600:
                time_left_minutes = round(time_left // 60) 
                await ctx.send(f"Bạn chỉ có thể sử dụng lại command `work` sau  {time_left_minutes} phút")    
            if time_left < 60:
                time_left_seconds = round(time_left) 
                await ctx.send(f"Bạn chỉ có thể sử dụng lại command `work` sau  {time_left_seconds} giây")    