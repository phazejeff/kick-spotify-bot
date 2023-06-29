import kick
import os
from dotenv import load_dotenv
from spotify import sp

load_dotenv()
KICK_SLUG = os.environ["KICK_SLUG"]
KICK_BOT_USERNAME = os.environ["KICK_BOT_USERNAME"]
KICK_BOT_PASSWORD = os.environ["KICK_BOT_PASSWORD"]

client = kick.Client()
global user

@client.event
async def on_message(message: kick.Message):
    if message.content.startswith("!songrequest"):
        track_url = message.content.split()[1]
        try:
            track = sp.track(track_url)
        except:
            await user.chatroom.send("Not a valid Spotify URL!")
            return
        
        try:
            sp.add_to_queue(track_url)
        except:
            return # likely no active device playing
        message_author = await message.author.to_user()
        await user.chatroom.send("@" + message_author.username + ": Adding " + track["name"] + " by " + track["artists"][0]["name"] + " to the queue.")

    elif message.content.startswith("!song"):
        message_author = await message.author.to_user()
        track = sp.currently_playing()["item"]
        await user.chatroom.send("@" + message_author.username + ": Current song is " + track["name"] + " by " + track["artists"][0]["name"])

@client.event
async def on_ready():
    print("Ready.")

    global user
    user = await client.fetch_user(KICK_SLUG)
    await user.chatroom.connect()


credentials = kick.Credentials(
        username=KICK_BOT_USERNAME,
        password=KICK_BOT_PASSWORD
    )
client.run(credentials)