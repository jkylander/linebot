# linebot
Final project for CS50x

Discord bot that grabs a URL and returns relevant code lines from GitHub as a code block message. 

It analyzes the URL using regex and replies with a markdown code block

## Usage

Post any github link to a file, with the line numbers at the end like this:

`https://github.com/jkylander/linebot/blob/main/bot.py#L19-L20`

(https://i.imgur.com/GP5wpIy.png)

The bot will try to read the language and use syntax highlighting. The repository must be public.

## Installing
```
git clone https://github.com/jkylander/linebot
cd linebot
```
Inside the linebot folder, install `pipenv` and the required packages with:
```
python -m pip install pipenv
python -m pipenv install --python 3.10
```

### Creating a token for the bot
* Go to the [Discord developer portal](https://discord.com/developers/applications), and login/signup
* Create a new Application
* In the Bot tab, under `Privileged Gateway Intents`, the `Message Content Intent` must be enabled
* Follow the [Official](https://discordjs.guide/preparations/setting-up-a-bot-application.html#creating-your-bot) guide for more information
* Make a `.env.local` file in the linebot directory and add the token like this (this token is invalidated):
```
DISCORD_TOKEN=NzkyNzE1NDU0MTk2MDg4ODQy.X-hvzA.Ovy4MCQywSkoMRRclStW4xAYK7I
```
## Running the bot
After installing, you can run the bot with
```
python -m pipenv run bot
```
