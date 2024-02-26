import hikari, lightbulb, aiohttp, bs4, dotenv, asyncio, os

dotenv.load_dotenv()

words = os.environ["WORDS"].split(", ")
token = os.environ["BOT_TOKEN"]
channel = os.environ["CHANNEL_ID"]

with open('cool.txt', 'w'):
    pass

class MyBot(lightbulb.BotApp):
    def __init__(self):
        self.is_scanning = False
        super().__init__(token=token)

async def get_links(bot: MyBot):
    while True:
        p = 1
        links = []
        try:
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f'https://spacehey.com/browse?page={p}') as resp:
                    page
                    page = await resp.text()            
        except:
            p = 1
            break

        soup = bs4.BeautifulSoup(page.text, "html.parser")
        results = soup.find("div", class_="inner").find_all("a")

        for res in results:
            if "profile?id" in res["href"]:
                links.append(res["href"])

        for link in links:
            while bot.is_scanning is False:
                await asyncio.sleep(20)
            await asyncio.sleep(6.5)
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f'https://spacehey.com{link}') as resp:
                    profile = await resp.text()
                    for w in words:
                        found = profile.lower().find(w)
                        if found != -1:
                            print(link)
                            print(w)
                            with open('cool.txt', 'r') as f:
                                if link in f.read():
                                    break
                            with open('cool.txt', 'a') as f:
                                f.write(f'https://spacehey.com{link} - {w}\n')
                                channel_object: hikari.TextableChannel = bot.cache.get_guild_channel(channel)
                                await channel_object.send(f'https://spacehey.com{link} - {w}')
                            break
                    print("keywords not found! next...")
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
