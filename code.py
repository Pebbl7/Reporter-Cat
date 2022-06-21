import discord
client = discord.Client()

modlist = [] #list user ids here

@client.event
async def on_ready():
    chan = client.get_channel() #put startup channel id here
    print("ready!")
    await chan.send("Erm... what the deuce??") #replace startup message here

@client.event
async def on_message(message):
    if message.author.id not in modlist:
        return  
    mess = " "
    msg = (message.content.lower()).split()
    if msg[0] == "msay":
        mess = mess.join(msg[1:])
        await message.delete()
        await message.channel.send(mess)
    if msg[0] == "msayin":
        mess = mess.join(msg[2:])
        await message.delete()
        try:
            chan = client.get_channel(int(msg[1][2:-1]))
            await chan.send(mess)
        except ValueError:
            await message.channel.send("That is not a valid channel. Try putting '<@[id]>' instead, or specify a channel.")

client.run("") #put bot token here
exit()