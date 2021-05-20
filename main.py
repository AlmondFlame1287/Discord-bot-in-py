import discord
from discord.ext.commands import Bot
import time as t
client = discord.Client()

bot = Bot(command_prefix="!")

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith("Dib"):
        await message.channel.send("finocchio")

    if message.content.startswith("Python"):
        await message.channel.send("Minchia cazz mi chiami a fare dio can")

    if message.content.startswith("Minecraftata?"):
        await message.channel.send("Ehhhh bohhhhh")

    if message.content.startswith("We fratmo come stai?"):
        await message.channel.send("T'appost, a te?")

    if message.content.startswith("Ehy tu, vuoi fare una call"):
        t.sleep(0.4)
        await message.channel.send("No fra guarda voglio segarmi")

    if message.content.startswith("Non dire ste cose"):
        t.sleep(0.4)
        await message.channel.send("Ma come? Non le dici pure tu?")

    if message.content.startswith("no") or message.content.startswith("No"):
        await message.channel.send("Eccolo quel mongoloide di merda che non vuole"
                                   "mai fare un cazzo")


@bot.command(name = "dio")
async def send_message(message):
    await message.channel.send("Borco Bio")
