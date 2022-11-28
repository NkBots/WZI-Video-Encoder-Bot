import dns.resolver
from pyrogram import idle
from aiohttp import web

from web import web_server
from . import app, log

dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = [
    '8.8.8.8']  # this is a google public dns

port = os.environ.get("PORT", "8080")

async def main():
    await app.start()
    tech = web.AppRunner(await web_server())
    await tech.setup()
    bind_address = "0.0.0.0"

    await web.TCPSite(tech, bind_address, port).start()
    await app.send_message(chat_id=log, text=f'<b>Bot Started! @{(await app.get_me()).username}</b>')
    await idle()
    await app.stop()

app.loop.run_until_complete(main())
