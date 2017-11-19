  import discord
    import asyncio

    client = discord.Client()

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    @client.event
    async def on_message(message):
        if message.content == "Hello":
            await client.send_message(message.channel, "World")

    client.run(<MzgxODA3MDkwNjUxMzY1Mzk3.DPM08A.FKjLUeQSU2Ujcg-c2wB9r55aDu0
>)
