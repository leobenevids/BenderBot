from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument

class Manager(commands.Cog):
    """Managing the bot"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Entramos como {0.user.name}'.format(self.bot))
        # current_time.start()


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if "palavrão" in message.content:
            await message.channel.send(f'Ó o palavrão, {message.author.name}!!')

            await message.delete()



    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("favor enviar todos os Argumentos. Digite .help para ver os parâmetros de cada comando")
        elif isinstance(error, CommandNotFound):
            await ctx.send("O comando não existe")
        else:
            raise error



def setup(bot):
    bot.add_cog(Manager(bot))