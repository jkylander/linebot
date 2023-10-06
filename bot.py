import os
import discord, requests, re, base64
from dotenv import load_dotenv
load_dotenv('.env.local')

TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents(messages=True, guilds=True)
intents.message_content = True


"""Parse URL for needed variables and store them in a dictionary

Parameters:
    url: url for the specified github file
Returns:
    dict of the parsed data if there is a match, otherwise None
"""
def match_url(url: str) -> dict:
    match = re.match(r"https://github.com/([^/]+)/([^/]+)/blob/(\w+)(/[^#]+)#(.+)", url)
    if match:
        data = {}
        data["owner"] = match.group(1)
        data["repo"] = match.group(2)
        data['branch'] = match.group(3)
        data["path"] = match.group(4)
        data["content"] = match.group(5)
        data["line_numbers"] = re.findall(r"\d+", data['content'])
        data["filetype"] = re.search(r"\.(\w+)$", data['path']).group(1)
        data["api_url"] = f"https://api.github.com/repos/{data['owner']}/{data['repo']}/contents/{data['path']}"
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
        print(message.content)

        if re.match(r"https://github.com/([^/]+)/([^/]+)/blob/(\w+)(/[^#]+)#(.+)", message.content):
            url = match_url(message.content)
            response = requests.get(url['api_url'])
            data = response.json()
            content = data['content']
            decoded_content = base64.b64decode(content).decode('utf-8').split('\n')
            joined_lines = '\n'.join(decoded_content[int(url['line_numbers'][0]):int(url['line_numbers'][1])])
            # strip trailing and ending whitespace
            joined_lines = '\n'.join([line.strip() for line in joined_lines.splitlines()])
            reply = f"""```{url['filetype']}
{joined_lines}
```"""
            await message.reply(reply, mention_author=False)

client = MyClient(intents=intents)

client.run(TOKEN)