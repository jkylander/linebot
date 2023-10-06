const { SlashCommandBuilder } = require('discord.js');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('react')
		.setDescription('Messages you with a reaction'),
	async execute(interaction) {
		const message = await interaction.reply({ content: 'You can react with Unicode emojis!', fetchReply: true });
		message.react('😄');
	},
};