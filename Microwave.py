# Discord API
import discord
import random
from googletrans import Translator

translator = Translator()


def token():
    with open("Token.txt") as secretToken:
        return secretToken.read()


def id():
    with open("ID.txt") as idtxt:
        return idtxt.read()


class MyClient(discord.Client):
    async def on_ready(self):
        print('client ready')

    async def on_message(self, message):
        if "!microwave" in message.content:
            if message.author.id == id():  # El id de yessi
                await message.channel.send("Yessi mato un microondas :c")
                await message.channel.send("Pero estaba rica el posole")
                await message.channel.send(":drooling_face:")
                print("Yessi mando un mensaje")

            # Abre primero la lista de sustantivos y los lee
            with open("nounlist.txt") as word_file:
                nouns = word_file.read().split()
            # Selecciona una palabra
            palabra = random.choice(nouns)
            print(f"selecting word {palabra}")
            palabraesp = translator.translate(palabra, dest="es", src="auto")

            #Con esto se lo manda al servidor
            await message.channel.send(f"MMMMMMMMMMMMMMMMMMMMMMMMM\nBEEP BEEP BEEP\nHuele a: {palabraesp.text}")
            print("Messages sent")


Bot = MyClient()
Bot.run(token())
