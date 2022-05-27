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

class rps():
    @commands.command()
    async def rps(self, ctx, amount = None, scale = 2, arg = None):
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
        mes = ''
        if arg == 'kéo' or arg == 'Kéo':
            randomChoose = random.randint(0, 2)
            if randomChoose == 0: 
                em = discord.Embed(title='**Kết quả**', description=f'**Bot chọn đấm**\n**{ctx.author.name}** - :smiling_face_with_tear: ****Hòa****\nTài khoản của bạn bị trừ đi **{amount}VND**', color=ctx.author.color)
                await ctx.send(embed = em)
                await update_bank(ctx.author, -(scale*amount)//2)
            if randomChoose == 1:
                em = discord.Embed(title='**Kết quả**', description=f'**Bot chọn lá**\n**{ctx.author.name}** - :trophy: **Bạn thắng**\nTài khoản của bạn được cộng thêm **{scale*amount}VND**', color=ctx.author.color)
                await ctx.send(embed = em)
                await update_bank(ctx.author, scale*amount)
            if randomChoose == 2:
                em = discord.Embed(title='**Kết quả**', description=f'**Bot chọn kéo**\n**{ctx.author.name}** - :slight_smile: Hòa\nTài khoản của bạn **được giữ nguyên**', color=ctx.author.color)
                await ctx.send(embed = em)
        elif arg == 'lá' or arg == 'Lá':
            randomChoose = random.randint(0, 2)
            if randomChoose == 0: 
                em = discord.Embed(title='**Kết quả**', description=f'**Bot chọn đấm**\n**{ctx.author.name}** - :trophy: **Bạn thắng**\nTài khoản của bạn được cộng thêm **{scale*amount}VND**', color=ctx.author.color)
                await ctx.send(embed = em)
                await update_bank(ctx.author, scale*amount)
            if randomChoose == 1:
                em = discord.Embed(title='**Kết quả**', description=f'**Bot chọn lá**\n**{ctx.author.name}** - :slight_smile: Hòa\nTài khoản của bạn **được giữ nguyên**', color=ctx.author.color)
                await ctx.send(embed = em)
            if randomChoose == 2:
                em = discord.Embed(title='**Kết quả**', description=f'**Bot chọn kéo**\n**{ctx.author.name}** - :smiling_face_with_tear: ****Hòa****\nTài khoản của bạn bị trừ đi **{amount}VND**', color=ctx.author.color)
                await ctx.send(embed = em)
                await update_bank(ctx.author, -(scale*amount)//2)
        elif arg == 'đấm' or arg == 'Đấm':
            randomChoose = random.randint(0, 2)
            if randomChoose == 0: 
                em = discord.Embed(title='**Kết quả**', description=f'**Bot chọn đấm**\n**{ctx.author.name}** - :slight_smile: Hòa \nTài khoản của bạn **được giữ nguyên**', color=ctx.author.color)
                await ctx.send(embed = em)
            if randomChoose == 1:
                em = discord.Embed(title='**Kết quả**', description=f'**Bot chọn lá**\n**{ctx.author.name}** - :smiling_face_with_tear: ****Hòa****\nTài khoản của bạn bị trừ đi **{amount}VND**', color=ctx.author.color)
                await ctx.send(embed = em)
                await update_bank(ctx.author, -(scale*amount)//2)
            if randomChoose == 2:
                em = discord.Embed(title='**Kết quả**', description=f'**Bot chọn kéo**\n**{ctx.author.name}** - :trophy: **Bạn thắng**\nTài khoản của bạn được cộng thêm **{scale*amount}VND**', color=ctx.author.color)
                await ctx.send(embed = em)
                await update_bank(ctx.author, scale*amount)

