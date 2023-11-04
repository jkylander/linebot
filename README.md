# linebot
Final project for CS50x

Discord bot that grabs a URL from da discord message and returns relevant code lines as a code block message. 

Supported websites:
 - GitHub
 - GitLab
 - BitBucket

It analyzes the URL using regex and replies with a markdown code block, with the appropriate syntax highlighting

## Usage

Post any GitHub or GitLab link to a file, with the line numbers at the end like this:

`https://github.com/jkylander/linebot/blob/main/bot.py#L19-L20`


The bot will try to read the language and use syntax highlighting. The repository must be public.

(https://i.imgur.com/kpUeufD.png)

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
* Make a `.env` file in the linebot directory and add the token like this (this token is invalidated):
```
DISCORD_TOKEN=NzkyNzE1NDU0MTk2MDg4ODQy.X-hvzA.Ovy4MCQywSkoMRRclStW4xAYK7I
```
## Running the bot
After installing, you can run the bot with
```
python -m pipenv run bot
```

## Struggles/Issues

Learning how Regex works was complicated for me. I had to learn pattern matching from scratch. Learning about groups and Match.groupdict() helped me reduce a lot of code repetition.
It was too hard for me to match URL's in a way that accounted for every special character. 

I ended up using [URLExtract](https://pypi.org/project/urlextract/) to save development time.

## Future Development

Add more public source code providers