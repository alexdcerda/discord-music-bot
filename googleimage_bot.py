import discord
from discord.ext import commands
import os, shutil
from google_images_download import google_images_download
import random


class image_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

