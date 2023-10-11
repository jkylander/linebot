# linebot
Final project for CS50


## Creating a token for the bot
* Go to the [Discord developer portal](https://discord.com/developers/applications), and login/signup
* Create a new Application
* Follow the [Official](https://discordjs.guide/preparations/setting-up-a-bot-application.html#creating-your-bot) guide for more information
* Make a `.env.local` file in the root directory and add the token like this (the token is invalidated):
```
DISCORD_TOKEN=NzkyNzE1NDU0MTk2MDg4ODQy.X-hvzA.Ovy4MCQywSkoMRRclStW4xAYK7I
```

## Installing and running
```
git clone https://github.com/jkylander/linebot
cd linebot
```
Inside the linebot folder, install `pipenv` and the required packages with:
```
python -m pip install pipenv
python -m pipenv install --python 3.10
```
After installing, you can run the bot with
```
python -m pipenv run bot
```