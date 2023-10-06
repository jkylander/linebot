// import discord.js
import {Client, Events, GatewayIntentBits, Message, TextChannel, BaseInteraction} from 'discord.js';

// create a new Client instance
const client = new Client({intents: [GatewayIntentBits.Guilds]});

// listen for the client to be ready
client.once(Events.ClientReady, (c) => {
  console.log(`Ready! Logged in as ${c.user.tag}`);
});

// Read messages
client.on('message', () => {
  const channel = client.channels.cache.get(process.env.CHANNEL_ID as string) as TextChannel;
  if (channel) {
    channel.messages.fetch().then((messages) => {
      messages.forEach((message: Message) => {
        console.log(`Received message: ${message.content}`);
      });
    });
  }
});

client.on(Events.InteractionCreate, async interaction => {
  if (!interaction.isChatInputCommand()) return;

	const { commandName } = interaction;

	if (commandName === 'react') {
		const message = await interaction.reply({ content: 'You can react with Unicode emojis!', fetchReply: true });
		message.react('😄');
	}
});


// login with the token from .env.local
client.login(process.env.DISCORD_TOKEN);

