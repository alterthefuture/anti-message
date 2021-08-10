from discord.ext import commands
import discord

bot = commands.Bot(command_prefix="!")

whitelisted_users = []

@bot.event
async def on_ready():
    print("Bot is online.") 

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if "@everyone" in message.content:
        if message.author.id not in whitelisted_users:
            muted = discord.utils.get(message.guild.roles, name="Muted")
            await message.delete()
            await message.author.add_roles(muted,reason="User mentioned @everyone.")
        else:
            pass

    if "https://" in message.content:
        if message.author.id not in whitelisted_users:
            await message.delete()
            return await message.channel.send(f"{message.author.mention} No links allowed.",delete_after=2)
        else:
            pass

    await bot.process_commands(message)
            

bot.run("") 