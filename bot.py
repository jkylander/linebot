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
def match_url(url):
    github_pattern = r'https://github.com/(?P<user>[^/]+)/(?P<repo>[^/]+)/blob/(?P<branch>[^/]+)/(?P<filepath>[^#]+)#L(?P<start_line>\d+)-L(?P<end_line>\d+)'
    gitlab_pattern = r'https://gitlab.com/(?P<user>[^/]+)/(?P<repo>[^/]+)/-/(?P<type>blob)/(?P<branch>[^/]+)/(?P<filepath>[^#]+)#L(?P<start_line>\d+)-(?P<end_line>\d+)'
    bitbucket_pattern = r'https://bitbucket.org/(?P<user>[^/]+)/(?P<repo>[^/]+)/src/(?P<branch>[^/]+)/(?P<filepath>[^#]+)#lines-(?P<start_line>\d+):(?P<end_line>\d+)'

    match = re.match(github_pattern, url)
    if match:
        data = match.groupdict()
        data['api_url'] = f"https://api.github.com/repos/{data['user']}/{data['repo']}/contents/{data['filepath']}?ref={data['branch']}"
        data['filetype'] = data['filepath'].split('.')[-1]
        return data

    match = re.match(gitlab_pattern, url)
    if match:
        data = match.groupdict()
        data['api_url'] = f"https://gitlab.com/api/v4/projects/{data['user']}%2F{data['repo']}/src/{data['branch']}/{data['filepath']}"
        data['filetype'] = data['filepath'].split('.')[-1]
        return data

    match = re.match(bitbucket_pattern, url)
    if match:
        data = match.groupdict()
        data['api_url'] = f"https://api.bitbucket.org/2.0/repositories/{data['user']}/{data['repo']}/src/{data['branch']}/{data['filepath']}"
        data['filetype'] = data['filepath'].split('.')[-1]
        return data




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
                if 'bitbucket' in match['api_url']:
                    
                    
                    decoded_content = response.text.split('\n')
                    
                else:
                    data = response.json()
                    content = data['content']
                    decoded_content = base64.b64decode(content).decode('utf-8').split('\n')

                joined_lines = '\n'.join(decoded_content[int(match['start_line'])-1:int(match['end_line'])])
                # fix indendation
                joined_lines = textwrap.dedent(joined_lines)

                reply = f"""```{match['filetype']}
{joined_lines}```"""
                await message.reply(reply, mention_author=False)


client = MyClient(intents=intents)
client.run(TOKEN)