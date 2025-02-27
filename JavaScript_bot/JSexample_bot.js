import { Client, GatewayIntentBits } from "discord.js";
import fs from "fs";
import path from "path";
import dotenv from "dotenv";
import ytdl from "ytdl-core";
import url from "url";



require("dotenv").config();

const { Client, GatewayIntentBits } = require("discord.js");

const TOKEN = process.env.DISCORD_TOKEN;


const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent
  ]
})


client.once('bot resady ---- im alive sir', () => {
  console.log(`Logged in as ${client.user.tag}`)
})


client.login(TOKEN)


