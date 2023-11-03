import os, sys
import discord, requests, re, base64
import textwrap
from dotenv import load_dotenv
from urlextract import URLExtract
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
if TOKEN is None:
    print("Error: Discord bot token not found. Set DISCORD_TOKEN in .env file")
    sys(exit(1))
intents = discord.Intents(messages=True, guilds=True)
intents.message_content = True
extractor = URLExtract()

"""Parse URL and store them in a dictionary

Parameters:
    url: url for the specified github file
Returns:
    dict of the parsed data if there is a match, otherwise None
"""
def match_url(url: str) -> dict:
    github_match = re.match(r"^(http://|https://)?github.com/(.+)/(.+)/blob/(.+)/(.+)#(.+)", url)
    gitlab_match = re.match(r"^(http://|https://)?gitlab.com/(.+)/(.+)/(.+)/blob/(.+)/(.+)#(.+)", url)
    if github_match:
        data = {}
        data["owner"] = github_match.group(2)
        data["repo"] = github_match.group(3)
        data['branch'] = github_match.group(4)
        data["path"] = github_match.group(5)
        data["content"] = github_match.group(6)
        data["line_numbers"] = re.findall(r"\d+", data['content'])
        data["filetype"] = re.search(r"\.(\w+)$", data['path']).group(1)
        data["api_url"] = f"https://api.github.com/repos/{data['owner']}/{data['repo']}/contents/{data['path']}"
        return data
    
    if gitlab_match:
        data = {}
        data["owner"] = gitlab_match.group(2)
        data["repo"] = gitlab_match.group(3)
        data["branch"] = gitlab_match.group(5)
        data["path"] = re.match(r"([^?]+)", gitlab_match.group(6)).group(1) #strip off anything after question mark
        data["content"] = gitlab_match.group(7)
        data["line_numbers"] = re.findall(r"\d+", data['content'])
        data["filetype"] = re.search(r"\.(\w+)$", data['path']).group(1)
        data["api_url"] = f"https://gitlab.com/api/v4/projects/{data['owner']}%2F{data['repo']}/repository/files/{data['path']}?ref={data['branch']}"
        return data
    return None



class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        
        for url in extractor.find_urls(message.content):
            match = match_url(url)
            if match:
                response = requests.get(match['api_url'])
                data = response.json()

                content = data['content']
                decoded_content = base64.b64decode(content).decode('utf-8').split('\n')
                joined_lines = '\n'.join(decoded_content[int(match['line_numbers'][0])-1:int(match['line_numbers'][1])])
                # fix indendation
                joined_lines = textwrap.dedent(joined_lines)

                reply = f"""```{match['filetype']}
{joined_lines}```"""
                await message.reply(reply, mention_author=False)

client = MyClient(intents=intents)

client.run(TOKEN)