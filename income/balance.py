import discord
from discord.ext import commands
from discord.ext.commands.core import command
import time
import random
import json
import os

os.chdir("C:\\Users\\Admin\\OneDrive\\Desktop\\Programing\\Discord\\V-Economy")

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

class balance():
    @commands.command()
    async def balance(self, ctx, *, member:discord.Member = None):
        if member==None:
            await open_account(ctx.author)
            user = ctx.author
            users = await get_bank_data()
            wallet_amt = users[str(user.id)]['wallet']
            bank_amt = users[str(user.id)]['bank']
            em = discord.Embed(title=f'{ctx.author.name}\'s balance', colour=ctx.author.color)
            em.add_field(name='Wallet', value=wallet_amt)
            em.add_field(name='Bank', value=bank_amt)
            await ctx.send(embed=em)
        if member != None:
            users = await get_bank_data()
            if str(member.id) not in users:
                await ctx.send('Người chơi này chưa có tài khoản')
                return
            wallet_amt = users[str(member.id)]['wallet']
            bank_amt = users[str(member.id)]['bank']
            em = discord.Embed(title=f'{member.name}\'s balance', colour=member.color)
            em.add_field(name='Wallet', value=wallet_amt)
            em.add_field(name='Bank', value=bank_amt)
            await ctx.send(embed=em)

    @commands.command()
    async def bal(self, ctx, *, member:discord.Member = None):
        if member==None:
            await open_account(ctx.author)
            user = ctx.author
            users = await get_bank_data()
            wallet_amt = users[str(user.id)]['wallet']
            bank_amt = users[str(user.id)]['bank']
            em = discord.Embed(title=f'{ctx.author.name}\'s balance', colour=ctx.author.color)
            em.add_field(name='Wallet', value=wallet_amt)
            em.add_field(name='Bank', value=bank_amt)
            await ctx.send(embed=em)
        if member != None:
            users = await get_bank_data()
            if str(member.id) not in users:
                await ctx.send('Người chơi này chưa có tài khoản')
                return
            wallet_amt = users[str(member.id)]['wallet']
            bank_amt = users[str(member.id)]['bank']
            em = discord.Embed(title=f'{member.name}\'s balance', colour=member.color)
            em.add_field(name='Wallet', value=wallet_amt)
            em.add_field(name='Bank', value=bank_amt)
            await ctx.send(embed=em)

    @commands.command()
    async def b(self, ctx, *, member:discord.Member = None):
        if member==None:
            await open_account(ctx.author)
            user = ctx.author
            users = await get_bank_data()
            wallet_amt = users[str(user.id)]['wallet']
            bank_amt = users[str(user.id)]['bank']
            em = discord.Embed(title=f'{ctx.author.name}\'s balance', colour=ctx.author.color)
            em.add_field(name='Wallet', value=wallet_amt)
            em.add_field(name='Bank', value=bank_amt)
            await ctx.send(embed=em)
        if member != None:
            users = await get_bank_data()
            if str(member.id) not in users:
                await ctx.send('Người chơi này chưa có tài khoản')
                return
            wallet_amt = users[str(member.id)]['wallet']
            bank_amt = users[str(member.id)]['bank']
            em = discord.Embed(title=f'{member.name}\'s balance', colour=member.color)
            em.add_field(name='Wallet', value=wallet_amt)
            em.add_field(name='Bank', value=bank_amt)
            await ctx.send(embed=em)
