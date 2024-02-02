import discord
from discord.ext import commands
from src.classes.types.config import Config


class DBot(commands.Bot):
    def __init__(self, config: Config) -> None:
        super().__init__(
            command_prefix=config.command_prefix,
            intents=discord.Intents.all()
        )
        self.token = config.token
        self.owner_id = config.owner

    async def on_ready(self):
        print(f"Logged in as {self.user}!")

    def run(self):
        return super().run(self.token)
