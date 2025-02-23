import discord
from discord.ext import commands
import os
import asyncio
import yt_dlp
from dotenv import load_dotenv

def run_bot():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(command_prefix='/', intents=intents)

    voice_clients = {}
    yt_dl_options = {"format": "bestaudio/best"}
    ytdl = yt_dlp.YoutubeDL(yt_dl_options)

    ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn -filter:a "volume=0.35"'}

    @client.event
    async def on_ready():
        print(f'{client.user} is now jamming')

    
    @client.command(name='play', help='Plays a song from youtube')
    async def play(ctx, link):
        try:
            voice_client = await ctx.author.voice.channel.connect()
            voice_clients[voice_client.guild.id] = voice_client
        except Exception as e:
            print(f"error with /play command: {e}")

        try:
            query = ctx.content.split(maxsplit=1)[1]

            search_url = f"ytsearch:{query}"

            loop = asyncio.get_event_loop()

            data = await loop.run_in_executor(
                None, lambda:ytdl.extract_info(search_url, download=False))
            
            if 'entries' in data and len(data['entries']) > 0:
                song_info = data['entries'][0]
            else:
                await ctx.channel.send("No results found for your query.")
                return
            
            song_url = song_info['url']

            player = discord.FFmpegOpusAudio(song_url, **ffmpeg_options)
            voice_clients[ctx.guild.id].play(player)
        except Exception as e:
            print(f"error loading music from YT: {e}")

        try:
            voice_clients[ctx.guild.id].pause()
        except Exception as e:
            print(f"error with /pause command: {e}")

        try:
            voice_clients[ctx.guild.id].resume()
        except Exception as e:
            print(f"error with /resume command: {e}")

        try:
            voice_clients[ctx.guild.id].stop()
            await voice_clients[ctx.guild.id].disconnect()
        except Exception as e:
            print(f"error with /stop command: {e}")

    client.run(TOKEN)