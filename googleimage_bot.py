import discord
from discord.ext import commands
import os, random, tempfile
from google_images_download import google_images_download
import random

from dotenv import load_dotenv


class image_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='image')
    async def image(self, ctx, *, query: str):
    
        with tempfile.TemporaryDirectory() as tempdir:
            response = google_images_download.googleimagesdownload()
            arguments = {
                "keywords": query,
                "limit": 10,
                "print_urls": True,    # change to false once working
                "output_directory": tempdir,
                "no_directory": True
                }
            
            try:
                results = response.download(arguments)
            except Exception as e:
                await ctx.send("There was an error during the google image search")

            if query in results and results[query]:
                image_path = random.choice(results[query])
            else:
                await ctx.send("No image were found for that query")
                return
            
            file = discord.File(image_path, filename=os.path.basename(image_path))
            embed = discord.Embed(title=f"Image result for: {query}")
            embed.set_image(url=f"attachment://{os.path.basename(image_path)}")

            await ctx.send(embed=embed, file=file)

def setup(bot):
    bot.add_cog(image_cog(bot))




