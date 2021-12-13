from discord.ext import commands

class Reactions(commands.Cog):
    """Work with reactions"""

    def __init__(self, bot):
        self.bot = bot

    # função Reação
    # events => commands.Cog.listener
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        print(reaction.emoji)
        if reaction.emoji == "👍":
            role = user.guild.get_role(919959106150891530)
            await user.add_roles(role)
        elif reaction.emoji == "💩":
            role = user.guild.get_role(919959262745219122)
            await user.add_roles(role)

def setup(bot):
    bot.add_cog(Reactions(bot))