# Kick Spotify Bot
A Kick.com bot that will allow chatters to add songs to your spotify queue.

This requires you to have [Go](https://go.dev/) and [Python](https://www.python.org/) installed.

## Setup

1. Run `pip install -r requirements.txt` in the folder.
2. Create a Kick account for your bot. Make that account a moderator in your chat.
3. Remove ".example" from the end of the [.env.example](.env) file so it's just .env
4. Fill in the KICK_SLUG with your stream username, make sure it is the one shown in your URL. Some characters get swapped, for example an underscore _ gets swapped with a dash -.
5. Fill in the KICK_BOT_USERNAME and KICK_BOT_PASSWORD with your bot username and password
6. Go to your [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) to create an app. Set the "Redirect URI" to "http://localhost". Fill in the SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET in [.env](.env) with your app id and secret.
7. Run `python -m kick bypass create` and `python -m kick bypass install`.

## Usage

### To start bot
1. Run `go run bypass.go`
2. Run `python main.py`

### Commands

- `!requestsong [Spotify URL]` - Adds a song to the queue. Spotify MUST be open and playing something for this to work.
- `!song` - Sends the current playing song to chat.