from aiohttp import web

from aio_tiny_healthcheck.checker import Checker

def some_sync_check():
    return True

async def some_async_check():
    return False

healthcheck_provider = Checker()
healthcheck_provider.add_check('sync_check_true', some_async_check)
healthcheck_provider.add_check('async_check_false', some_async_check)


app = web.Application()
app.router.add_get('/healthcheck', healthcheck_provider.aiohttp_handler)
web.run_app(app)
