from datetime import datetime
from logging import error
import discord
import os
from discord import guild
from discord import colour
from discord.ext import commands
from discord import client
from discord import embeds
from discord.colour import Color
from discord.embeds import E
from discord.ext import commands, tasks
from discord.ext.commands.help import MinimalHelpCommand
from discord.role import R
from discord.ext.commands import Bot, has_permissions, CheckFailure
from discord import user
import time
import random
from youtube_dl import YoutubeDL
from discord.channel import VoiceChannel
import asyncio
import json
from TOKEN import TOKEN

os.chdir("C:\\Users\\Admin\\OneDrive\\Desktop\\Programing\\Discord\\V-Economy")

client = commands.Bot(command_prefix='v')

client.remove_command('help')
client.remove_command('invite')

# Help tổng
@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title='**V-Economy Help**', description='''Một con bot tài chính hoạt động trên discord do người Việt Nam tạo ra nhằm mục đích đem lại sự giải trí và niềm vui cho người Việt :flag_vn:
    Gõ `vbalance` để tạo mã định danh và chơi game ngay nào :smiling_face_with_3_hearts:
    ''', color=ctx.author.color, colour=ctx.author.color)        
    em.add_field(name='Các lệnh cơ bản', value='`vhelp common`')
    em.add_field(name='Games', value='`vhelp games`')
    em.add_field(name='Shop', value='`vhelp shop`')
    em.add_field(name='Invite', value='`invite`')
    await ctx.send(embed = em)

# Help category
@help.command()
async def common(ctx):
    em = discord.Embed(title='**Các lệnh cơ bản**', description='''Chi tiết các lệnh cơ bản nhất của game\n
    `vbalance/vbal/vb` - Kiểm tra tài khoản của bạn
    `vwork/vw` - Làm việc để kiếm tiền
    `vdeposit/vdep` - Chuyển tiền từ ví vào tài khoản ngân hàng
    `vwithdraw/vdraw` - Rút tiền từ ngân hàng
    `vpay` - Chuyển tiền cho người khác
    ''', colour=ctx.author.color)
    await ctx.send(embed = em)
@help.command()
async def game(ctx):
    em = discord.Embed(title='**Games**', description='''Một số game nhỏ để giải trí giết thời gian trong lúc chờ thời gian đếm ngược của các lệnh khác\n
    `vgamble/vgam/vg` - Cá cược
    `vrps` - Chơi oẳn tù tì với bot
    ''', colour=ctx.author.color)
    await ctx.send(embed = em)
@help.command()
async def games(ctx):
    em = discord.Embed(title='**Games**', description='''Một số game nhỏ để giải trí giết thời gian trong lúc chờ thời gian đếm ngược của các lệnh khác\n
    `vgamble/vgam/vg` - cá cược
    `vrps` - chơi oẳn tù tì
    ''', colour=ctx.author.color)
    await ctx.send(embed = em)

# Help lệnh chi tiết

# Balance
@help.command()
async def balance(ctx):
    em = discord.Embed(title='**Balance**', description='Kiểm tra tài khoản của bạn', colour=ctx.author.color)
    em.add_field(name='Lệnh chi tiết', value='`vbalance [@member]`')
    await ctx.send(embed = em)
@help.command()
async def bal(ctx):
    em = discord.Embed(title='**Balance**', description='Kiểm tra tài khoản của bạn', colour=ctx.author.color)
    em.add_field(name='Lệnh chi tiết', value='`vbal [@member]`')
    await ctx.send(embed = em)
@help.command()
async def b(ctx):
    em = discord.Embed(title='**Balance**', description='Kiểm tra tài khoản của bạn', colour=ctx.author.color)
    em.add_field(name='Lệnh chi tiết', value='`vb [@member]`')
    await ctx.send(embed = em)

# Deposit
@help.command()
async def deposit(ctx):
    em = discord.Embed(title='**Deposit**', description='Chuyển tiền từ ví vào tài khoản ngân hàng', colour=ctx.author.color)
    em.add_field(name='Lệnh chi tiết', value='`vdeposit <số tiền/all>`')
    await ctx.send(embed = em)
@help.command()
async def dep(ctx):
    em = discord.Embed(title='**Balance**', description='''Kiểm tra tài khoản của bạn
    ''', colour=ctx.author.color)
    em.add_field(name='Lệnh chi tiết', value='`vdep <số tiền/all>`')
    await ctx.send(embed = em)

# Withdraw
@help.command()
async def withdraw(ctx):
    em = discord.Embed(title='**Withdraw**', description='Rút tiền từ ngân hàng', colour=ctx.author.color)
    em.add_field(name='Lệnh chi tiết', value='`vwithdraw <số tiền/all>`')
    await ctx.send(embed = em)
@help.command()
async def draw(ctx):
    em = discord.Embed(title='**Withdraw**', description='Rút tiền từ ngân hàng', colour=ctx.author.color)
    em.add_field(name='Lệnh chi tiết', value='`vdraw <số tiền/all>`')
    await ctx.send(embed = em)

# Pay
@help.command()
async def pay(ctx):
    em = discord.Embed(title='**Pay**', description='Chuyển tiền cho người khác', colour=ctx.author.color)
    em.add_field(name='Lệnh chi tiết', value='`vpay <@member> <số tiền/all>`')
    await ctx.send(embed = em)

# Gamble
@help.command()
async def gamble(ctx):
    em = discord.Embed(title='**Gamble**', description='Cá cược', colour=ctx.author.color)
    em.add_field(name='Lệnh chi tiết', value='''`vgamble <số tiền> [tỉ lệ]`
    - **Thắng**: Bạn nhận số tiền bằng số tiền bạn cược nhân với tỉ lệ
    - **Thua**: Tài khoản của bạn bị trừ đi số tiền mà bạn đã cược''')
    await ctx.send(embed = em)
@help.command()
async def gam(ctx):
    em = discord.Embed(title='**Gamble**', description='Cá cược', colour=ctx.author.color)
    em.add_field(name='Lệnh chi tiết', value='''`vgam <số tiền> [tỉ lệ]`
    - **Thắng**: Bạn nhận số tiền bằng số tiền bạn cược nhân với tỉ lệ
    - **Thua**: Tài khoản của bạn bị trừ đi số tiền mà bạn đã cược''')
    await ctx.send(embed = em)
@help.command()
async def g(ctx):
    em = discord.Embed(title='**Gamble**', description='Cá cược', colour=ctx.author.color)
    em.add_field(name='Lệnh chi tiết', value='''`vg <số tiền> [tỉ lệ]`
    - **Thắng**: Bạn nhận số tiền bằng số tiền bạn cược nhân với tỉ lệ
    - **Thua**: Tài khoản của bạn bị trừ đi số tiền mà bạn đã cược''')
    await ctx.send(embed = em)

# RPS
@help.command()
async def rps(ctx):
    em = discord.Embed(title='**Oẳn tù tì**', description='Chơi oẳn tù tì với bot', colour=ctx.author.color)
    em.add_field(name='Lệnh chi tiết', value='''`vrps <số tiền> <tỉ lệ> <kéo/lá/đấm>`\n
    - **Thắng**: Bạn nhận số tiền bằng số tiền bạn cược nhân với tỉ lệ
    - **Hòa**: Số tiền bạn cược được giữ nguyên
    - **Thua**: Tài khoản của bạn bị trừ đi số tiền mà bạn đã cược nhân với tỉ lệ rồi chia đôi''')
    await ctx.send(embed = em)


async def open_account(user):
    users = await get_bank_data()
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]['wallet'] = 0
        users[str(user.id)]['bank'] = 0
    with open('users_data.json', 'w') as f:
        json.dump(users, f)
    return True

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





@client.event
async def on_ready():
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
async def load(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)

#https://discord.com/api/oauth2/authorize?client_id=927009128054931547&permissions=137439267840&scope=bot