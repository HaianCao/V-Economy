import discord
from discord import embeds
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

class gamble():
    @commands.command()
    async def gamble(self, ctx, amount = None, scale = 2):
        if scale < 2:
            await ctx.send('Tỉ lệ tối thiểu là 2')
            return
        users = await get_bank_data()
        if str(ctx.author.id) not in users:
            await ctx.send('Gõ `vbalance` trước')
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
                if len(x) > 1:
                    total_stars = float(x[:-1]) * num_map.get(x[-1].upper(), 1)
            return int(total_stars)
        amount = convert_str_to_number(amount)
        if amount < 50000:
            await ctx.send('Cần cá tối thiểu 50.000VND')
            return
        if amount>bal[0]:
            await ctx.send('Không đủ tiền để chơi')
            return
        if amount < 0:
            await ctx.send('Lượng tiền không thể bé hơn 0')
            return
        a = random.randint(0, scale-1)
        if a == 0:
            await update_bank(ctx.author, scale*amount)
            await ctx.send('Thắng')
        if a != 0:
            await update_bank(ctx.author, -1*amount)
            await ctx.send('Thua')

    @commands.command()
    async def gam(self, ctx, amount = None, scale = 2):
        if scale < 2:
            await ctx.send('Tỉ lệ tối thiểu là 2')
            return
        users = await get_bank_data()
        if str(ctx.author.id) not in users:
            await ctx.send('Gõ `vbalance` trước')
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
                if len(x) > 1:
                    total_stars = float(x[:-1]) * num_map.get(x[-1].upper(), 1)
            return int(total_stars)
        amount = convert_str_to_number(amount)
        if amount < 50000:
            await ctx.send('Cần cá tối thiểu 50.000VND')
            return
        if amount>bal[0]:
            await ctx.send('Không đủ tiền để chơi')
            return
        if amount < 0:
            await ctx.send('Lượng tiền không thể bé hơn 0')
            return
        a = random.randint(0, scale-1)
        if a == 0:
            await update_bank(ctx.author, scale*amount)
            await ctx.send('Thắng')
        if a != 0:
            await update_bank(ctx.author, -1*amount)
            await ctx.send('Thua')

    @commands.command()
    async def g(self, ctx, amount = None, scale = 2):
        if scale < 2:
            await ctx.send('Tỉ lệ tối thiểu là 2')
            return
        users = await get_bank_data()
        if str(ctx.author.id) not in users:
            await ctx.send('Gõ `vbalance` trước')
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
                if len(x) > 1:
                    total_stars = float(x[:-1]) * num_map.get(x[-1].upper(), 1)
            return int(total_stars)
        if amount != 'all':
            amount = convert_str_to_number(amount)
        if amount < 50000:
            await ctx.send('Cần cá tối thiểu 50.000VND')
            return
        if amount>bal[0]:
            await ctx.send('Không đủ tiền để chơi')
            return
        if amount < 0:
            await ctx.send('Lượng tiền không thể bé hơn 0')
            return
        a = random.randint(0, scale-1)
        if a == 0:
            await update_bank(ctx.author, scale*amount)
            em = discord.Embed(title='**Kết quả**', description=f'**{ctx.author.name}** - :trophy: Bạn thắng\nTài khoản của bạn được cộng thêm **{scale*amount}VND**', colour=ctx.author.color)
            em.add_field(name='Tỉ lệ cược', value=f'Bạn cần xúc ra 1 trong đoạn 1 đến {scale} để thắng và bạn đã xúc ra 1')
            await ctx.send(embed=em)
        if a != 0:
            await update_bank(ctx.author, -1*amount)
            em = discord.Embed(title='**Kết quả**', description=f'**{ctx.author.name}** - :smiling_face_with_tear: Bạn thua\nTài khoản của bạn bị trừ đi **{amount}VND**', colour=ctx.author.color)
            em.add_field(name='Tỉ lệ cược', value=f'Bạn cần xúc ra 1 trong đoạn 1 đến {scale} để thắng và bạn đã xúc ra {a}')
            await ctx.send(embed=em)

            