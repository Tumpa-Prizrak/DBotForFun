import tomli
from src.classes.types.config import Config


def parse_config():
    with open("config.toml", mode="rb") as fp:
        data = tomli.load(fp)
        return Config(
            token=data["bot"]["TOKEN"],
            owner=data["bot"]["OWNER"],
            command_prefix=data["bot"]["COMMAND_PREFIX"]
        )
