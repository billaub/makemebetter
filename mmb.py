import discord
import os

client = discord.Client()

classes_color = {
    "Death Knight": 0xC41F3B,
    "Demon Hunter": 0xA330C9,
    "Druid": 0xFF7D0A,
    "Hunter": 0xABD473,
    "Mage": 0x40C7EB,
    "Monk": 0x00FF96,
    "Paladin": 0xF58CBA,
    "Priest": 0xFFFFFF,
    "Rogue": 0xFFF569,
    "Shaman": 0x0070DE,
    "Warlock": 0x8787ED,
    "Warrior": 0xC79C6E,
}

classes_name = {
    "Death Knight": ["dk", "deathknight"],
    "Demon Hunter": ["dh", "demonhunter"],
    "Druid": ["drood", "druide", "druid"],
    "Hunter": ["hunter", "chasseur", "hunt"],
    "Mage": ["mage",],
    "Monk": ["moine", "monk"],
    "Paladin": ["paladin", "pal", "palouf"],
    "Priest": ["priest", "prêtre"],
    "Rogue": ["rogue", "fufu", "voleur"],
    "Shaman": ["chaman", "shaman", "cham", "sham"],
    "Warlock": ["demo", "démo", "lock", "warlock"],
    "Warrior": ["war", "warrior", "guerrier"],
}

classes = (
    '!mage',
    '!demo', '!démo', '!lock', '!warlock',
    '!druid', '!drood', '!druide',
    '!monk', '!moine',
    '!deathknight', '!dk',
    '!rogue', '!voleur', '!fufu',
    '!demonhunter', '!dh',
    '!priest', '!prêtre',
    '!warrior', '!war', '!guerrier',
    '!shaman', '!cham', '!sham', '!chaman',
    '!hunter', '!chasseur', '!hunt'
    '!paladin', '!pal', '!palouf',
)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.channel.name != 'role-request':
        return

    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith(classes):
        role = get_role(message.content.split(' ')[0].strip('!'))
        msg = '{0.author.mention} your requested the role {1}'.format(message, role)
        await client.send_message(message.channel, msg)
        add_role(server=message.server, role=role, user=message.author)

def get_role(start):
    for key in classes_name.keys():
        for values in classes_name.get(key):
            if start == values:
                return key
    return None

async def add_role(server, role, user):
    userRole = await client.create_role(server=server, name=role, colour=discord.Colour(classes_color.get(role)), hoist=False,
                       mentionable=True)
    await client.add_roles(user, userRole)

token = os.environ.get("DISCORD_BOT_TOKEN")
client.run(token)