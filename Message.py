'''
    Copyright (c) 2023 MysteriousBlob

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
'''

import requests
from time import sleep

TOKEN = "YOU DISCORD TOKEN HERE"
CHANNEL = "DISCORD CHANNEL ID"
MAX_MESSAGE_LEN = 1900

def discordSendMessage(channel, token, msg):
    if len(msg) > MAX_MESSAGE_LEN:
        exit(1)
    requests.post(f"https://discord.com/api/v9/channels/{channel}/messages", headers={"authorization":f"{token}"}, data={"content":f"{msg}", "flags": 0, "tts": False})

def waitAndType(channel, token, secondsTyping):
    for i in range(secondsTyping):
        try:
            requests.post(f"https://discord.com/api/v9/channels/{channel}/typing", headers={"authorization":f"{token}"})
        except:
            break
        finally:
            sleep(1)

print("(Leave empty if none)")
initiatorMessage = input("Enter the initiator message: ")

print()
print("(Leave empty if none)")
finalMessage = input("What should be the final message: ")

print()
secondsTyping = int(input("Enter for how many seconds to type: "))

if initiatorMessage != "":
    discordSendMessage(CHANNEL, TOKEN, initiatorMessage)

waitAndType(CHANNEL, TOKEN, secondsTyping)

if finalMessage != "":
    discordSendMessage(CHANNEL, TOKEN, finalMessage)