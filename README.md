# Discord bot for fun

This bot was created to have fun and practice, not for real usage.

You can suggest features or report bugs via discussions/issues respectively

## Installation

Create virtual environment and install packages specified in the requirements.txt

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

After it create `config.toml` by providing next fields:

- `bot.TOKEN`: token of your bot.
- `bot.OWNER`: bot owner's id.
- `bot.COMMAND_PREFIX`: bot's prefix. If you going to use slash commands - set to "/",
otherwise provide command prefix

Examples can be found at `config_example.toml`

## Starting

Just run start.sh script

```sh
chmod +x start.sh
./start.sh
```

or python module directly

```sh
python -m src
```

## Usage

Use `/help` slash command to see list of commands
