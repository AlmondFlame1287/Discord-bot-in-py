from discord.ext.commands import Bot
import os


token = os.environ['TOKEN']


comandi = ['aiuto', 'bw', 'minecraft', 'dib', 'pag', 'gruz', 'server', 'lillo', 'arrotino', 'ale', 'skammettino', 'tommasino']
bot = Bot(command_prefix="!", case_insensitive=True)


@bot.event
async def on_ready():
    print("so lillo")

# Help


@bot.command(name = comandi[0])
async def aiu(ctx):
    await ctx.send(comandi)

# Bedwars


@bot.command(name = comandi[1])
async def bw(ctx):
    await ctx.send('@everyone Bedwarsina?')

# Minecraft


@bot.command(name = comandi[2])
async def mc(ctx):
    await ctx.send('@everyone Vuoi giocare a minecraft?')

# Dib


@bot.command(name = comandi[3])
async def db(ctx):
    await ctx.send('Gruz sei proprio inaffidabile')

# Pagano


@bot.command(name = comandi[4])
async def pg(ctx):
    await ctx.send('Nu pazzariell allor ja')

# Grusio


@bot.command(name = comandi[5])
async def gruz(ctx):
    await ctx.send('Che finocchio!!')

# Server


@bot.command(name = comandi[6])
async def serv(ctx):
    await ctx.send('Grusio, apri sto cazz di server')

# Posaman


@bot.command(name = comandi[7])
async def lillo(ctx):
    await ctx.send('https://www.youtube.com/watch?v=jZbUnwjEcz0&ab_channel=AtleticoVescovioAtleticoVescovio')
    await ctx.send('so lillo')

# Arrotino


@bot.command(name = comandi[8])
async def arro(ctx):
    await ctx.send('https://www.youtube.com/watch?v=MKsxkO9qn_Q&ab_channel=SocialStories')
    await ctx.send("Sveglia donne, è arrivato l'arrotino")

# Zi


@bot.command(name = comandi[9])
async def zi(ctx):
    await ctx.send('Bella zi, te se ama')

# Skam


@bot.command(name = comandi[10])
async def skam(ctx):
    await ctx.send('Nu frat a me ja')

# Tommaso


@bot.command(name = comandi[11])
async def tom(ctx):
    await ctx.send('Tommaso schiavo del governo')

bot.run(token)