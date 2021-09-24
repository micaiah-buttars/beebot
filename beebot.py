'''BeeBot is picky. Make sure to run these to make it work:
        source venv/bin/activate
        source secrets.sh
'''


import discord
import os
from random import choice


client = discord.Client()

def open_and_read_file(file_path):
    contents = open(file_path).read().replace("\n", " ")

    return contents


def make_chains(text_string):
    chains = {}

    words = text_string.split()
    for i in range(len(words) - 2):
        if (words[i], words[i + 1]) not in chains:
            chains[(words[i], words[i + 1])] = [words[i + 2]]
        else:
            chains[(words[i], words[i + 1])].append(words[i + 2])
    
    return chains


def make_text(chains):
    words = [list(chains)[0][0], list(chains)[0][1]]

    i = 0
    while '.' not in words[-1]:
        words.append(choice(chains[(words[i], words[i + 1])]))
        i += 1

    return ' '.join(words)

input_path = 'beemovie.txt'
input_text = open_and_read_file(input_path)
chains = make_chains(input_text)




@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    msg = message.content.lower()


    if message.author == client.user:
        return

    if any(e in msg for e in ['bee', 'honey']):
        await message.channel.send(f"🐝 {make_text(chains)} 🐝")

    if any(e in msg for e in ['jazz', 'hello', 'music', 'song']):
        await message.channel.send("🐝 Ya like jazz? 🐝")

    if 'good bot' in msg:
        await message.channel.send("🐝 The Bee Movie was written and produced by Jerry Seinfeld, who also plays the protagonist, Barry B. Benson. 🐝")
    elif 'bad bot' in msg:
        await message.channel.send("🐝 Can you feel your heart burning? Can you feel the struggle within? The fear within me is beyond anything your soul can make. You cannot kill me in a way that matters. 🐝")
    


client.run(os.environ.get('DISCORD_TOKEN'))