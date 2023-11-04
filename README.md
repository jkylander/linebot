# linebot
Final project for CS50x
#### Video Demo: https://www.youtube.com/watch?v=ilZD_OAC6nE


This Discord bot is designed to fetch and highlight code from GitHub, GitLab, and Bitbucket repositories. When a user posts a URL from one of these platforms, the bot will fetch the code from the specified file and lines, then post it back to the Discord channel with syntax highlighting.

Supported websites:
 - GitHub
 - GitLab
 - BitBucket

### How it works

The bot uses regular expressions to parse the URLs and extract the necessary data, such as the username, repository name, branch, file path, and line numbers. It then uses the respective platform's API to fetch the code from the specified file and lines.

Once the code is fetched, it is indented properly and sent as a reply to the message with the URL. The bot uses Discord's built-in syntax highlighting feature to highlight the code in the posted message.

### Usage

Post a link to a source code file, with the line numbers at the end, like this:

`https://github.com/jkylander/linebot/blob/main/bot.py#L19-L20`

`https://bitbucket.org/rtfpessoa/bitbucket-scala-client/src/50eaaa768999c01c53e4621e990a959606440399/circle.yml#lines-1:5`

`https://gitlab.com/magnolia1234/bypass-paywalls-firefox-clean/-/blob/master/background.js#L152-163`


The bot will try to read the language and use syntax highlighting. The repository must be public.

![The message the bot returns when posting a link](https://i.imgur.com/kpUeufD.png)

## Installing
Clone this repository:
```
git clone https://github.com/jkylander/linebot
cd linebot
```
Inside the linebot folder, install `pipenv` and the required packages with:
```
python -m pip install pipenv
python -m pipenv install
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
### Running the bot
After installing, you can run the bot with
```
python -m pipenv run bot
```

## Struggles/Issues

Learning how Regex works was complicated for me. I had to learn pattern matching from scratch. Learning about groups and Match.groupdict() helped me reduce a lot of code repetition.
It was too hard for me to match URL's in a way that accounted for every special character. 

I ended up using [URLExtract](https://pypi.org/project/urlextract/) to save development time.

## Future Development

* More public source code providers
* Add a "message component" with a link to the code snippet

![Discord message component](https://i.imgur.com/zmE2umk.png)

### Note
This bot is intended for educational purposes and is not affiliated with Discord, GitHub, GitLab, or Bitbucket.