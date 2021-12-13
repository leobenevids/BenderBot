import discord
from discord.ext import commands

class Talks(commands.Cog):
    """Talks with user"""

    def __init__(self, bot):
        self.bot = bot

    # função Dizer Oi
    #bot.command => commands.command
    @commands.command(name="oi", help="- Envia uma saudação || (Não requer argumentos)")
    async def saudacoes(self, ctx):
        await ctx.send(f'Olá, {ctx.author.name}!')


    # função mandar mensagem direta
    @commands.command(name='segredo', help="- Envia um segredo no privado || (Não requer argumentos)")
    async def secret(self, ctx):
        try:
            await ctx.author.send("oi")
            await ctx.author.send("vo ti conta um segredo meia noite")

        except discord.errors.Forbidden:
            await ctx.send(
                "Não posso te contar o segredo, habilite receber mensagens de qualquer pessoa do servidor (Opções > Privacidade)"
            )

def setup(bot):
    bot.add_cog(Talks(bot))