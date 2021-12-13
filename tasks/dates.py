import datetime
from discord.ext import commands, tasks

class Dates(commands.Cog):
    """Work with dates"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.current_time.start()
    
    # tarefa Mostrar Hora
    @tasks.loop(hours=1)
    async def current_time(self):
        now = datetime.datetime.now()

        now = now.strftime("%d/%m/%Y às %H:%M:%S")

        channel = self.bot.get_channel(918567213772984361)

        await channel.send("Data neste momento: " + now)

def setup(bot):
    bot.add_cog(Dates(bot))