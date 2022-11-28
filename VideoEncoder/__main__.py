import dns.resolver
from pyrogram import idle
from aiohttp import web
import os
#from web import web_server
from . import app, log

from aiohttp import web

from aio_tiny_healthcheck.checker import Checker

#from flask import Flask

#cck = Flask(__name__)

dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = [
    '8.8.8.8']  # this is a google public dns

port = os.environ.get("PORT", "8080")
from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/healthcheck")
async def root_route_handler(request):
    #return web.json_response("Welcome to NkBots Community")
    text = "Hello From Nk Community"
    return web.json_response(text=text)

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

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






def some_sync_check():
    return True

async def some_async_check():
    return False

healthcheck_provider = Checker()
healthcheck_provider.add_check('sync_check_true', some_async_check)
healthcheck_provider.add_check('async_check_false', some_async_check)


mdk = web.Application()
mdk.router.add_get('/healthcheck', healthcheck_provider.aiohttp_handler)
web.run_app(app)
