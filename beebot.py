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
    if message.author == client.user:
        return

    if message.content.startswith('$bee'):
        await message.channel.send(f"{make_text(chains)}")

client.run(os.environ.get('DISCORD_TOKEN'))