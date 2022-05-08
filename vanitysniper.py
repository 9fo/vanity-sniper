import json
import re
import requests
from time import sleep
import colorama
import os
from colorama import Fore

joinTiming = False

rtoken = "" ## Token goes here
rguild = "" ## Guild ID goes here

def start():
    foundD = False
    os.system(f"title Vanity Sniper ; Made by obama#8083")

    claimuser = input(f"{Fore.LIGHTBLUE_EX}User > ")
    while foundD == False:
        res = requests.get(f'https://discord.com/invite/{claimuser}')
        if 'og:image:type' in res.text:
            print(f"{Fore.LIGHTBLUE_EX}Unavailable | {claimuser}")
        else:
            print(f"{Fore.LIGHTBLUE_EX}Available | {claimuser}")
            print(f"{Fore.LIGHTBLUE_EX}Sniping | {claimuser}")
            headers = {
                "Content-Type":"application/json",
                "Authorization":rtoken
            }
            respns = requests.patch(f'https://canary.discord.com/api/v9/guilds/{rguild}/vanity-url', data={"code":claimuser}, headers=headers)
            if 'invalid or taken' in respns:
                print(f"{Fore.LIGHTBLUE_EX}Failed Snipe ;; Retrying | {claimuser}")
            else:
                print(f"{Fore.LIGHTBLUE_EX}Sniped | {claimuser}")
                foundD = True

start()