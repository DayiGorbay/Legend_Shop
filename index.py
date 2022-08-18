from typing import Optional

import discord
from discord import app_commands

id= 994131948597432412

MY_GUILD = discord.Object(id=993909178894651505)  # replace with your guild id


class client(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.all()
bot = client(intents=intents)

token = "token"

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"Legend Shop"))
    print(discord.__version__)

@bot.tree.command()
@app_commands.describe(
    member='kharidar',
    product='kala',
    image='aks payin'
)
async def kharidar(interaction: discord.Interaction, member: discord.Member, product: str, image: str):
    embed=discord.Embed(title=f"**با تشکر از خرید شما :rose:\n\n**", description=f"**خریدار :shopping_cart:**\n<@{member.id}>", color=discord.Color.blue())
    embed.set_image(url=image)
    embed.set_thumbnail(url=member.avatar)
    embed.set_footer(text="لجند  شاپ ارزان سریع مطمئن 🎁", icon_url="https://cdn.discordapp.com/attachments/1009816795164721183/1009822313518223450/logolegendshop.png")
    embed.set_author(name=f"{product}", icon_url="https://cdn.discordapp.com/emojis/997231060393934918.gif?size=96&quality=lossless")
    await bot.get_channel(id).send(embed=embed)
    await interaction.response.send_message(f"** با موفقیت انجام شد :white_check_mark:**")

bot.run(token)