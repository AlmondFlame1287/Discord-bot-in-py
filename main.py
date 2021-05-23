import discord
from discord.ext.commands import Bot
# import os
import random


token = os.environ['TOKEN']


comandi = ['aiuto', 'bw', 'minecraft', 'inaffidabile', 'pazzo', 'fin', 'server', 'lillo', 'arrotino', 'amo', 'fratm', 'schiavo', 'bestemmia']

test = ['aiutotest','bestemmia']
bestemmie = ['Porco dio', 'Mannaccia alla madonna', 'Quel cornuto di dio', 'Mannaccia a Gesù Cristo']

bot = Bot(command_prefix = "!", case_insensitive = True, activity = discord.Activity(type = discord.ActivityType.watching, name = "LOL, chi ride è fuori"), status = discord.Status.dnd)

@bot.event
async def on_ready():
    print("so lillo")


# Aiuto generale


@bot.command(name = comandi[0])
async def aiu(ctx):
    await ctx.send(comandi)


# Chiedi per una bedwars


@bot.command(name = comandi[1])
async def bw(ctx):
    await ctx.send('@everyone Bedwarsina?')

# Chiedi per giocare a minecraft


@bot.command(name = comandi[2])
async def mc(ctx):
    await ctx.send('@everyone Volete giocare a minecraft?')


# {member.mention} è inaffidabile


@bot.command(name = comandi[3])
async def inaff(ctx, member : discord.Member):
    await ctx.send(f'{member.mention} sei proprio inaffidabile')

# Frase tipica


@bot.command(name = comandi[4])
async def pazzo(ctx):
    await ctx.send('Nu pazzariell allor ja')

# Frase tipica di G.


@bot.command(name = comandi[5])
async def fino(ctx):
    await ctx.send('Che finocchio!!')

# Chiedi di aprire un server di minecraft


@bot.command(name = comandi[6])
async def serv(ctx, member : discord.Member):
    await ctx.send(f'{member.mention} apri sto cazz di server')

# Chiama lillo


@bot.command(name = comandi[7])
async def lillo(ctx):
    await ctx.send('https://www.youtube.com/watch?v=jZbUnwjEcz0&ab_channel=AtleticoVescovioAtleticoVescovio')
    await ctx.send('so lillo')

# Chiama l'arrotino


@bot.command(name = comandi[8])
async def arro(ctx):
    await ctx.send('https://www.youtube.com/watch?v=MKsxkO9qn_Q&ab_channel=SocialStories')
    await ctx.send("Sveglia donne, è arrivato l'arrotino")

# {member.mention} ti si vuole bene


@bot.command(name = comandi[9])
async def te_se_ama(ctx, member : discord.Member):
    await ctx.send(f'Bella {member.mention}, te se ama')

# {member.mention} sei uno di noi


@bot.command(name = comandi[10])
async def frat(ctx, member : discord.Member):
    await ctx.send(f'{member.mention} Nu frat a me ja')

# {member.mention} sei solo uno schiavo


@bot.command(name = comandi[11])
async def schiavetto(ctx, member : discord.Member):
    await ctx.send(f'{member.mention} schiavo del governo')

# Omaggio al linguaggio di programmazione


@bot.command(name = 'Python')
async def py(ctx):
    await ctx.send('Grazie Python per averci permesso di fare quello che state appena vedendo')


# Qualche bestemmia non ha mai fatto male a nessuno
######## TO DO: INSERIRE QUALCHE BESTEMMIA IN PIU' #########
@bot.command(name = comandi[12])
async def best(ctx):
    await ctx.send(f'{ctx.author.mention}, indovina.. {bestemmie[random.randint(0,3)]}')
######## TO DO: INSERIRE QUALCHE BESTEMMIA IN PIU' #########

# Parte test delle nuove funzioni

@bot.command(name = test[0])
async def aiuto_test(ctx):
    await ctx.send(test)



bot.run(token)