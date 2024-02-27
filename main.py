import hikari, lightbulb, aiohttp, bs4, dotenv, asyncio, os, logging

dotenv.load_dotenv()

words = os.environ["WORDS"].split(", ")
token = os.environ["BOT_TOKEN"]
channel = os.environ["CHANNEL_ID"]

with open('cool.txt', 'w'):
    pass

class MyBot(lightbulb.BotApp):
    def __init__(self):
        self.is_scanning = False
        super().__init__(token=token, logs="INFO")

async def get_links(bot: MyBot):
    while True:
        logging.debug("rahh")
        p = 1
        links = []
        try:
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f'https://spacehey.com/browse?page={p}') as resp:
                    page = await resp.text()            
        except:
            p = 1
            break

        soup = bs4.BeautifulSoup(page, "html.parser")
        results = soup.find("div", class_="inner").find_all("a")

        logging.debug("loop 2")
        for res in results:
            if "profile?id" in res["href"]:
                links.append(res["href"])

        logging.debug("loop 3")
        for link in links:
            while bot.is_scanning is False:
                logging.debug("False")
                await asyncio.sleep(20)
            await asyncio.sleep(6.5)
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f'https://spacehey.com{link}') as resp:
                    profile = await resp.text()
                    logging.debug("here?")
                    for w in words:
                        found = profile.lower().find(w)
                        if found != -1:
                            logging.debug(link)
                            logging.debug(w)
                            with open('cool.txt', 'r') as f:
                                if link in f.read():
                                    break
                            with open('cool.txt', 'a') as f:
                                f.write(f'https://spacehey.com{link} - {w}\n')
                                channel_object: hikari.TextableChannel = bot.cache.get_guild_channel(int(channel))
                                await channel_object.send(f'https://spacehey.com{link} - {w}')
                            break
                    logging.debug("keywords not found! next...")
                p += 1

bot = MyBot()

@bot.command
@lightbulb.command("scan", "starts the scanner")
@lightbulb.implements(lightbulb.SlashCommand)
async def start_scan(ctx: lightbulb.Context):
    bot.is_scanning = True
    await ctx.respond(content="Started Scanning")
    await get_links(bot)

@bot.command
@lightbulb.command("stop-scan", "stops the scanner")
@lightbulb.implements(lightbulb.SlashCommand)
async def stop_scan(ctx: lightbulb.Context):
    bot.is_scanning = False
    await ctx.respond(content="Stopped Scanning")

bot.run()
