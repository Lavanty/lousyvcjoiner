import discord


# Function to connect to voice channel
async def join_voice_channel(token, guild_id):
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'Bot {client.user} has connected to Discord!')
        guild = discord.utils.get(client.guilds, id=guild_id)

        if guild is not None:
            voice_channel = discord.utils.get(guild.voice_channels, bitrate=64000)

            if voice_channel is not None:
                vc = await voice_channel.connect()
            else:
                print(f'No suitable voice channels found in guild {guild.name}')
                await client.close()
        else:
            print(f'Guild with ID {guild_id} not found!')
            await client.close()

    client.run(token)


# Input bot tokens and guild ID from a file
def read_tokens_from_file():
    try:
        with open('tokens.txt', 'r') as file:
            tokens = file.readlines()
            return [token.strip() for token in tokens]
    except FileNotFoundError:
        print("tokens.txt file not found. Please create a file named tokens.txt and add your bot tokens.")
        return []


def main():
    tokens = read_tokens_from_file()

    if tokens:
        guild_id = int(input("Enter guild ID: "))

        for token in tokens:
            print(f"Connecting with token: {token}")
            join_voice_channel(token, guild_id)


if __name__ == "__main__":
    main()