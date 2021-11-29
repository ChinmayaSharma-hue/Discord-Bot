import discord
from discord.ext import commands
import random
import requests
import os
import openai

# initializing the client which is the bot.
client = commands.Bot(command_prefix="$")

# removing the default help command in order to define a custom one.
client.remove_command("help")

openai.api_key = "open_ai_key_goes_here"


# Defining a Word class in order to encapsulate all the commands that are called for the word.
class Word:
    def __init__(self, word):
        self.word = word

    # Gets the json file from the site and returns the dictionary from it.
    def get_json(self, word):
        link = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        definition_dict = requests.get(link).json()
        return definition_dict[0]

    # To return the phonetic of the word.
    def phonetic(self):
        definition_dict = self.get_json(self.word)
        phonetic = definition_dict["phonetic"]
        return phonetic

    # To return the origin of the word.
    def origin(self):
        definition_dict = self.get_json(self.word)
        origin = definition_dict["origin"]
        return origin

    # If there are multiple parts of speech of a word, then a random one is selected and returned back.
    def pos(self, index=-1):
        definition_dict = self.get_json(self.word)
        if index == -1:
            max_ind = 0
            for pos in definition_dict["meanings"]:
                max_ind += 1
            index = random.randint(0, max_ind - 1)
        part_of_speech = definition_dict["meanings"][index]["partOfSpeech"]
        return part_of_speech

    # There will be multiple definitions for multiple parts of speech in a word, therefore a random pos is
    # selected and a random definition within that is selected to be returned.
    def definition(self, index=-1):
        try:
            definition_dict = self.get_json(self.word)
            def_list = []
            if index == -1:
                max_ind = 0
                for i in definition_dict["meanings"]:
                    max_ind += 1
                index = random.randint(0, max_ind - 1)
            max_index = 0
            for i in definition_dict["meanings"][index]["definitions"]:
                max_index += 1
            index_2 = random.randint(0, max_index - 1)
            definition = f'{definition_dict["meanings"][index]["definitions"][index_2]["definition"]}'
        except:
            definition = f"The word '{self.word}' does not exist."
        return definition

    # To return a sentence where the word is used. Similar to definitions, there will be multiple pos for a
    # word and multiple examples for each pos, so one is selected at random and returned.
    def usage(self, index=-1):
        try:
            definition_dict = self.get_json(self.word)
            usage_list = []
            if index == -1:
                max_ind = 0
                for pos in definition_dict["meanings"]:
                    max_ind += 1
                index = random.randint(0, max_ind - 1)

            max_index = 0
            for i in definition_dict["meanings"][index]["definitions"]:
                max_index += 1
            index_2 = random.randint(0, max_index - 1)
            usg = definition_dict["meanings"][index]["definitions"][index_2]["example"]
        except:
            usg = f"No sentences found for '{self.word}'."
        return usg

    # To return synonyms within a range for a word from a randomly selected pos of the word.
    def syn(self, index=-1):
        try:
            definition_dict = self.get_json(self.word)
            syn_list = []
            if index == -1:
                max_ind = 0
                for pos in definition_dict["meanings"]:
                    max_ind += 1
                index = random.randint(0, max_ind - 1)
            for syns in definition_dict["meanings"][index]["definitions"]:
                syn_list.append(syns["synonyms"])
            synonyms = f""
            for i in range(len(syn_list)):
                if len(syn_list[i]) > 0:
                    for j in range(len(syn_list[i])):
                        synonyms = synonyms + f"'{syn_list[i][j]}'  "
                        if j > 1:
                            break
            if synonyms == "":
                synonyms = f"No synonyms found for {self.word}."
        except:
            synonyms = f"The word '{self.word}' does not exist."
        return synonyms

    # To return antonyms within a range for a word from a randomly selected pos of the word.
    def ant(self, index=-1):
        try:
            definition_dict = self.get_json(self.word)
            ant_list = []
            if index == -1:
                max_ind = 0
                for i in definition_dict["meanings"]:
                    max_ind += 1
                index = random.randint(0, max_ind - 1)
            for ants in definition_dict["meanings"][index]["definitions"]:
                ant_list.append(ants["antonyms"])
            antonyms = f""
            a = 2
            for i in range(len(ant_list)):
                if len(ant_list[i]) > 0:
                    for j in range(len(ant_list[i])):
                        antonyms = antonyms + f"'{ant_list[i][j]}'  "
                        if j > 1:
                            break
            if antonyms == "":
                antonyms = f"No antonyms found for {self.word}."
        except:
            antonyms = f"The word '{self.word}' does not exist."
        return antonyms

    # To define the all function, a random number is generated in this function so that the same random number can
    # be sent to each of the above mentioned functions so that the pos will match in each function.
    def get_index(self):
        definition_dict = self.get_json(self.word)
        max_ind = 0
        for i in definition_dict["meanings"]:
            max_ind += 1
        index = random.randint(0, max_ind - 1)
        return index


# To know when the bot is online
@client.event
async def on_ready():
    print("Online")


# To send back the phonetic in case of the "$phonetic" command
@client.command()
async def phonetic(ctx, arg):
    word = Word(arg)
    embed = discord.Embed(title=arg, description=word.phonetic())
    await ctx.send(embed=embed)


# To send back the phonetic in case of the "$org" command
@client.command()
async def org(ctx, arg):
    word = Word(arg)
    embed = discord.Embed(title=arg, description=word.origin())
    await ctx.send(embed=embed)


# To send back the part of speech in case of the "$pos" command
@client.command()
async def pos(ctx, arg):
    word = Word(arg)
    embed = discord.Embed(title=arg, description=word.pos())
    await ctx.send(embed=embed)


# To send back the definition in case of the "$definition" command
@client.command()
async def definition(ctx, arg):
    word = Word(arg)
    embed = discord.Embed(title=arg, description=word.definition())
    await ctx.send(embed=embed)


# To send back an example in case of the "$usage" command
@client.command()
async def usage(ctx, arg):
    word = Word(arg)
    embed = discord.Embed(title=arg, description=word.usage())
    await ctx.send(embed=embed)


# To send back the synonyms in case of the "$synonym" command
@client.command()
async def syn(ctx, arg):
    word = Word(arg)
    embed = discord.Embed(title=arg, description=word.syn())
    await ctx.send(embed=embed)


# To send back the antonym in case of the "$definition" command
@client.command()
async def ant(ctx, arg):
    word = Word(arg)
    embed = discord.Embed(title=arg, description=word.ant())
    await ctx.send(embed=embed)


# Calls all the functions defined till now
@client.command()
async def all(ctx, arg):
    word = Word(arg)
    ind = word.get_index()
    embed = discord.Embed(title=arg, description=word.definition(index=ind))
    embed.add_field(name="Part of Speech", value=word.pos(index=ind))
    embed.add_field(name="Origin", value=word.origin())
    embed.add_field(name="Phonetic", value=word.phonetic())
    embed.add_field(name="Usage", value=word.usage(index=ind))
    embed.add_field(name="Synonyms", value=word.syn(index=ind))
    embed.add_field(name="Antonyms", value=word.ant(index=ind))
    await ctx.send(embed=embed)


# Defining the "$help" command
@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="DICTIONARY BOT",
        description="Welcome to the help section. Type the following commands,",
    )
    embed.add_field(name="$all", value="To get all the information about the word.")
    embed.add_field(name="$definition", value="To get the meaning of the word.")
    embed.add_field(name="$pos", value="To get the part of speech the word belongs to.")
    embed.add_field(name="$org", value="To find out the word's origin.")
    embed.add_field(name="$phonetic", value="To get the phonetics of the word.")
    embed.add_field(name="$usage", value="To see how the word is used in sentences.")
    embed.add_field(name="$syn", value="To get the synonyms of the word.")
    embed.add_field(name="$ant", value="To get the antonyms of the word.")
    embed.add_field(name="$query", value="To talk to a witty bot when you're lonely.")

    await ctx.send(embed=embed)


# getting a responseopenai AI model through API
@client.command()
async def query(ctx, *args):
    arg = " ".join(list(args))
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Human: {arg} \nAI:",
        temperature=0.7,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.6,
        presence_penalty=0,
        stop=["\n", " Human:", " AI:"],
    )
    await ctx.send(response["choices"][0]["text"])


client.run("bot_code_goes_here")
