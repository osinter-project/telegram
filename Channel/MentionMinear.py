from telethon.sync import TelegramClient
import appconfig as ac

tclient = TelegramClient('../sessions/my', ac.api_id, ac.api_hash)


def get_comments(client, channel, message_id):
    data = {}

    async def crawl_comments():
        async for message in client.iter_messages(channel, reply_to=message_id):
            try:
                data[message.id] = message.from_id.user_id
            except:
                pass

    with client:
        client.loop.run_until_complete(crawl_comments())

    return data


post_link = "https://t.me/MohammadZarchi/111"
cd = post_link.split('/')
post_id = int(cd[4])
user_ids = []
cmd = get_comments(tclient, cd[3], post_id)
f = open(f"Channel/ChannelMention/{cd[3]}-{post_id}.txt", "a")
for i, p in enumerate(cmd):
    if not cmd[p] in user_ids:
        msg = f"{i+1} - https://t.me/{cd[3]}/{post_id}?comment={p}"
        user_ids.append(cmd[p])
        f.write(msg + "\n")
        print(msg)

f.close()
