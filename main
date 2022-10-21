import os, asyncio, random, discord
from keep_alive import keep_alive
from discord.ext import commands
from jabebot import ask, append_interaction_to_chat_log


client = discord.Client()
bot = commands.Bot(
	command_prefix="$",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 972352387647942676  # Change to your discord id!!!

@bot.event 
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier
    file_to_delete = open("cv.txt", 'w') #erase text file
    file_to_delete.close()

async def embed(ctx):
    embed = discord.Embed(
        title = 'Please Accept the terms of usage',
        description = 'Hi! To talk to this bot, please type $Accept to show that you understand the conditions of usage',
        colour = discord.Colour.blue()
    )
    embed.add_field(name='Usage Conditions', value='By using this bot,'
                                                   'you understand that you understand this bot may say insensitive things '
                                                   'because the training data may have had unintended influences. You will not hold anything agaist the creator for what this bot says and should not take what it says too seriously.', inline=False)
    embed.set_image(url='https://media.giphy.com/media/GaynE6dZoVDkQ/giphy.gif')
    embed.set_footer(text='Brought to you by, Gubbas#1020')
    await ctx.channel.send(embed=embed)

@bot.event
async  def on_message(message):
    if message.author == (client.user or message.author.bot):
        return

    if not '$' in str(message.content):
        return
    if '$accept' in str(message.content).lower():
        file1 = open("auth.txt", "a")
        file1.write(f' {message.author.id}')
        await message.channel.send(":D")
        return
    if not message.channel.id == 1032541558291038278:
        pass
       # return


    file1 = open("cv.txt", "r")
    chat_log = file1.read()
    file1.close()

    file1 = open("auth.txt", "r")
    auth = file1.read()
    file1.close()

    if str(message.author.id) not in auth:
        await embed(message)
        return

    incoming_msg = str(message.content).replace('$','')
    answer = ask(incoming_msg, chat_log)

    file1 = open("cv.txt", "a")  # write mode
    if len(chat_log) > 250:
        file_to_delete = open("cv.txt", 'w')  # erase text file
        file_to_delete.close()
    file1.write(append_interaction_to_chat_log(incoming_msg, answer,))
    file1.close()
    await message.channel.send(answer)



extensions = [
	'cogs.cog_example'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.


async def change_stat():

   await bot.wait_until_ready()

   while not bot.is_closed():
       status = random.choice(['with your feelings', 'with your heart', 'with knives', 'with fire', 'hard to get'])
       await bot.change_presence(activity=discord.Game(status))

       await asyncio.sleep(1200)

bot.loop.create_task(change_stat())


keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("DISCORD_BOT_SECRET") 
bot.run(token)  # Starts the bot
