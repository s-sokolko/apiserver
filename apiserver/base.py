__author__ = 'godzilla'

from aiohttp import web
from cli_logging import logger_from_cli_params


logger = logger_from_cli_params(__name__)


class APIServer:
    def __init__(self, addr, port, loop=None):
        self._app = web.Application(loop=loop)
        self._loop = loop if loop else self._app.loop
        self.addr = addr
        self.port = port
        self._init_routes()
        self._loop.run_until_complete(self._init_runner())

    def _init_routes(self):
        raise NotImplementedError

    async def _init_runner(self):
        runner = web.AppRunner(self.app)
        self.runner = runner
        await runner.setup()
        site = web.TCPSite(runner, self.addr, self.port)
        await site.start()

    def close(self):
        self.loop.run_until_complete(self.runner.cleanup())

    @property
    def app(self):
        return self._app

    @property
    def loop(self):
        return self._loop
