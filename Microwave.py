# Discord API
import discord
import random
from googletrans import Translator

translator = Translator()


def token():
    with open("Token.txt") as secretToken:
        return secretToken.read()

with open("ID.txt") as idtxt:
    id = idtxt.read()
print(f"Special friends ID: ",id)


class MyClient(discord.Client):
    async def on_ready(self):
        print('client ready')

    async def on_message(self, message):
        if "!microwave" in message.content:
            print(message.author.id)
            print(id)
            if (message.author.id == int(id)):  # El id de yessi
                await message.channel.send("Yessi mato un microondas :c")
                await message.channel.send("Pero estaba rica el ⓟⓞⓩⓞⓛⓔ")
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
        elif "te quiero" in message.content and not message.author.bot:
            await message.channel.send(f"Yo tambien te quiero :3")

#starts and runs the bot
Bot = MyClient()
Bot.run(token())
