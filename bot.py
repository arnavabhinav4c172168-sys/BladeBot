import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # Ye members ko track karne ke liye hai
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.event
async def on_member_join(member):
    # Apna Welcome Channel ID yahan daal dena
    channel_id = 1541067105246650391 
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(f"Welcome to Blade Kingdom, {member.mention}! 🎉 Enjoy your stay here with Blade Scarlett amd others.")

# Yahan apna Bot Token paste karna
bot.run("MTU0MzIxNjc1Mjk5NjEyMjYzNA.GXACqZ.GkKZUCPSZSNoJZTd7hvfqJgWZx9HmPddUXRrFc")
