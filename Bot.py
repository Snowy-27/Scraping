import aiocron
import discord
from discord.ext import commands


class BotDiscord:
    def __init__(self, token, message):
        self.token = token
        self.message = message

    def Bot(self):
        print("Lancement en cours")
        bot = commands.Bot(command_prefix='!')

        @bot.event
        async def on_ready():
            print('Bot pret')
            await bot.change_presence(status=discord.Status.idle, activity=discord.Game("Ecole direct"))

        @aiocron.crontab('00 16 * * mon,tue,wed,thu,fri,sun')
        async def notes():
            channel = bot.get_channel(749590466437185597)
            await channel.send(self.message)

        bot.run(self.token)
        print("Lancement en cours")


