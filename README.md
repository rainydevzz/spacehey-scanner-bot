# Spacehey Scanner Bot

This is a derivative of my other project, [Spacehey Scanner](https://github.com/rainydevzz/spacehey-scanner). In this project I have integrated its functionality into a Discord Bot that you can host yourself.

### How It Works

It uses the exact same webscraping mechanism as Spacehey Scanner (although it has been tweaked slightly to comply with the asynchronous nature of Discord bots) but now sends links inside a channel of your choice.

This guide will be a little lengthier than the Spacehey Scanner because setting up Discord bots is a process in its own right.

### Getting Started

I recommend getting the Discord business out of the way 1st, AKA setting up a bot application. Follow [this guide](https://discordjs.guide/preparations/setting-up-a-bot-application.html#creating-your-bot) provided by Discord.JS to set up the bot account. Fear not however, there will be no coding required. Make sure you get access to the token and paste it somewhere for the time being (like a text file, NOT where anyone else can access it). Make sure you invite the bot to the same server as the channel you want it to send messages in.

You will also need to download and install [Python](https://www.python.org/downloads/). Make sure to check the Add to PATH option in the installer.

Download the repository by clicking the green "Code" button at the top of the page. If you have git installed, you can clone the repo, or you can just download the zip file and extract it.

Once the folder is ready and extracted, navigate to it with File Explorer and edit the file called `example.env`. Here, you will want to replace the text next to BOT_TOKEN (`BOT_TOKEN=...`) with the token you stored earlier. You will replace the CHANNEL_ID value with a channel ID if your choice. To get a channel ID, right click on a channel in Discord and select Copy ID. Lastly, you can edit the WORDS value according to how it is formatted, separating words and phrases with a comma then a space. Now, rename the file to `.env`.

Assuming you still have File Explorer open and are still inside the folder, right click inside the folder and select "Open In Terminal". Then, type the following commands.

`pip install -r requirements.txt`

`python main.py`

Assuming everything is correct, you should see a log like this:

(sorry if the formatting looks weird lol)

```
 oooo         o8o  oooo                            o8o       光 2.0.0.dev122 [5961d1a3]
  `888         `"'  `888                            `"'       © 2021-present, davfsa - MIT license
   888 .oo.   oooo   888  oooo   .oooo.   oooo d8b oooo       interpreter:   CPython 3.11.7
   888P"Y88b  `888   888 .8P'   `P  )88b  `888""8P `888       running on:    x86_64 Linux 6.7.4-arch1-1
   888   888   888   888888.     .oP"888   888      888       installed at:  /home/rainy/.local/lib/python3.11/site-packages/hikari
   888   888   888   888 `88b.  d8(  888   888      888       documentation: https://docs.hikari-py.dev/en/2.0.0.dev122
  o888o o888o o888o o888o o888o `Y888""8o d888b    o888o      support:       https://discord.gg/Jx4cNGG

Thank you for using lightbulb!

```

Congratulations, you have successfully set up a Discord bot that will scan Spacehey profiles and post them in a channel.

I understand that this might be a bit heavy or hard-to-follow so feel free to forward any questions or issues to me, I will be happy to help.