import random
from discord.ext import commands

class Smarts(commands.Cog):
    """A lot of Smart Commands"""

    def __init__(self, bot):
        self.bot = bot

    # função Cálculo
    @commands.command(name="calc", help="- Calcula o valor de uma Expressão || (Argumentos: Expressão)")
    async def calculate_expression(self, ctx, *expression):
        expression = "".join(expression)

        print(expression)

        response = eval(expression)

        await ctx.send("A resposta é: " + str(response))

        
    # função Rolar Dado
    @commands.command(help="- Rola o valor de um dado || (Argumentos: números de lados)")
    async def dado(self, ctx, numero):
        variavel = random.randint(1, int(numero))
        await ctx.send(f'O número que saiu no dado é {variavel}')



def setup(bot):
    bot.add_cog(Smarts(bot))