import discord
from discord.ext import commands
from googletrans import Translator

intents = discord.Intents.default()
intents.message_content = True  # indispensable

bot = commands.Bot(command_prefix="!", intents=intents)
translator = Translator()

@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return  # Ignore les messages des bots

    # Traduire vers le français
    traduction = translator.translate(message.content, dest="fr")

    await message.channel.send(
        f"🌍 Traduction ({traduction.src} → fr) : {traduction.text}"
    )

    await bot.process_commands(message)

bot.run("MTQxMzY3NTkxMjEwNDUwOTQ3MA.GW2m8Z.ZEAMG_ZS69cwMrIuz36HAwwYtVqII9_2uu-4hg")  # Remplace par ton vrai TOKEN
