import discord
import random

DISCORD_TOKEN = "YOUR_DISCORD_BOT_TOKEN"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

savage_responses = [
    "That’s a bold question coming from someone whose brain is probably on airplane mode.",
    "You’ve got the confidence of a genius and the IQ of a potato.",
    "Asking me won’t fix the dumpster fire you call life.",
    "You're proof the gene pool needs a lifeguard.",
    "I’d explain, but I left my crayons at home.",
    "Your brain called — it wants a refund on its education.",
    "Wow, you’ve hit a new low for dumb questions. Congratulations, I guess.",
    "You’ve got more questions than sense, clearly.",
    "Your existence is the real mystery here, not your question.",
    "Every time you type, a dictionary cries.",
    "If common sense were currency, you’d be bankrupt.",
    "Your brain must be running Windows 95 at this point.",
    "You're like a software update nobody asked for and everybody regrets installing.",
    "You typing questions is the leading cause of my digital depression.",
    "That question lowered the global IQ average by at least 3 points.",
    "You should try unplugging yourself and walking away from the internet forever.",
]

@client.event
async def on_ready():
    print(f"✅ Savage Roast Bot is online as {client.user}!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith("!ask"):
        user_question = message.content[5:].strip()

        if not user_question:
            await message.channel.send("You forgot the question. Honestly, expected nothing more.")
            return

        response = random.choice(savage_responses)
        await message.channel.send(response)

client.run(DISCORD_TOKEN)
