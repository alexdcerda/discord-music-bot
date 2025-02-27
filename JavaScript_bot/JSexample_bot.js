import dotenv from 'dotenv'
import { Client, GatewayIntentBits } from 'discord.js'
import ytdl from 'ytdl-core'
import { joinVoiceChannel, createAudioPlayer, createAudioResource } from '@discordjs/voice';
import { ytSearch } from 'yt-search'


dotenv.config({path: '../.env'})
const TOKEN = process.env.DISCORD_TOKEN

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.GuildVoiceStates,
  ]
})


const prefix = '!'
const server = {}

client.once('ready', () => {
  console.log(`${client.user.tag} is now jamming`)
})


client.on('messageCreate', async (message) => {
  if (message.author.bot) return
  if (!message.content.startsWith(prefix)) return

  const args = message.content.slice(prefix.length).trim().split(/ +/)
  const command = args.shift().toLowerCase()

  if (command === 'play') {

  }
})




client.login(TOKEN)