import discord
import responses
import secretkey

async def sendMessage(message, userMessage, is_private):
    try:
        response = responses.handleResponse(userMessage)
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)
    except Exception as e:
        print(e)

def runDiscordBOT():
    TOKEN = secretkey.key
    intents = discord.Intents(messages=True, guilds=True)
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print('Logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            print('Bot: {0}'.format(message.content))
            return

        username = str(message.author)
        user_message = message.content
        channel = str(message.channel)
        print('User: {0} | Message: {1} | Channel: {2}'.format(username, user_message, channel))

        if channel.lower().startswith('direct'):
            await sendMessage(message, user_message, True)
        else:
            await sendMessage(message, user_message, False)

    client.run(TOKEN)