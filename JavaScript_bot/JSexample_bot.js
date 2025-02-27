import dotenv from 'dotenv'
import { Client, GatewayIntentBits, VoiceChannel } from 'discord.js'
import ytdl from 'ytdl-core'
import { joinVoiceChannel, createAudioPlayer, createAudioResource,
   NoSubscriberBehavior, AudioPlayerStatus } from '@discordjs/voice';
import { ytSearch } from 'yt-search'


dotenv.config({path: '../.env'})
const TOKEN = process.env.DISCORD_TOKEN

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.GuildVoiceStates,
    GatewayIntentBits.MessageContent
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
    const voiceChannel = message.member?.voice?.channel
    if (!voiceChannel) {
      message.channel.send('You need to be in a voice channel to play music')
      return
    }
    if (args.length === 0) {
      message.channel.send('You need to provide a song name or URL')
      return
    }
    const query = args.join(' ')


    ////////////////////////// continue from here
  }
})




client.login(TOKEN)