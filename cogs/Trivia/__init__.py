"""Package for Trivia cog."""
from .Trivia import *
from .session import *
from .log import *


def setup(bot):
    """Load Trivia."""
    cog = Trivia()
    bot.add_cog(cog)
