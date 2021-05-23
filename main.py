#import packages
import discord
from discord import embeds
from discord.ext import commands
from random import random, choice
from datetime import datetime

#our bot
client = commands.Bot(command_prefix="+")

#content
@client.event
async def on_ready():
    general =  client.get_channel(845321330021761046)
    await general.send("mn online awa yaluwane")

@client.event
async def on_disconnect():
    general =  client.get_channel(845321330021761046)
    await general.send("good bye kastiya")

@client.command(name = "server")
async def server(context):
    pusa = discord.Embed(
        title = "hello",
        description = "this is my server",
        color = 0x00ff00
        )
    await context.message.channel.send(embed = pusa)

@client.command(name = "info")
async def info(ctx):
    colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF0808, 0xC71585, 0xFFB6C1, 0x00CED1]


    haraka = discord.Embed(
        title = "admin",
        description = "eshan \ndumindu",
        color = choice(colors),
        timestamp = datetime.utcnow()
        )
    haraka.add_field(name="partner",value= "bunny",inline=False)
    haraka.add_field(name = "co leaders", value= "waruna \nrukshan",inline=False)
    haraka.add_field(name="date released", value="march 21, 2019", inline=False)
    haraka.set_image(url ="https://media.discordapp.net/attachments/381963689470984203/845710377773563944/giphy.gif")
    haraka.set_author(name="Realm of Ceylon")
    haraka.add_field(name="Join my server",value="[click here](https://discord.gg/r9aE54n6eb)")
    haraka.set_footer(text=f"thank you have a nice day | rerquested by {ctx.author}")
    haraka.set_thumbnail(url="https://media.discordapp.net/attachments/753250382167146567/845439938739961937/maxresdefault.jpg?width=1247&height=701")


    await ctx.message.channel.send(embed = haraka)



#run the bot
client.run("TOKEN")

