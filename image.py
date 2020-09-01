import time
from PIL import Image
import discord
from discord.ext import commands
from selenium import webdriver
from bs4 import BeautifulSoup
import os

print("Lancement en cours")
bot = commands.Bot(command_prefix='!')

    
def get_url_image(name):
    dir_name = "."
    test = os.listdir(dir_name)

    for item in test:
        if item.endswith(".png"):
            os.remove(os.path.join(dir_name, item))
    driver = webdriver.Chrome()
    driver.get(
        'https://www.google.com/search?q=' + name + '&safe=active&sxsrf=ALeKk021DGMp6pyDIBF9x6Y8zxh8SCZfQQ:1598801980133&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjl293AocPrAhUvyYUKHeAjD-YQ_AUoA3oECAsQBQ&cshid=1598802002909515')
    time.sleep(1)
    page = driver.page_source
    soup = BeautifulSoup(page, 'lxml')
    images = soup.find('div', {'class': 'islrc'})
    img = images.find_all('img')
    time.sleep(0.1)
    url = img[0]['src']
    driver.get(url)
    driver.save_screenshot(name + '.png')
    img = Image.open(name + '.png')
    box = (50, 50, 100, 100)
    area = img.crop(box)
    print(area)


@bot.event
async def on_ready():
    print('Bot pret')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("Ecole direct"))


@bot.command()
async def image(ctx, arg):
    get_url_image(arg)
    my_files = [
        discord.File(arg + '.png'),
    ]
    await ctx.send(files=my_files)


bot.run("NzQ3MDI5OTQyNTI4NjM5MDQ2.X0I72Q.JM_GCfWCC_dzfKqXRVTMr_oMXUw")
print("Lancement en cours")
