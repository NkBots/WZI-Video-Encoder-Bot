# VideoEncoder - a telegram bot for compressing/encoding videos in h264/h265 format.
# Copyright (c) 2021 WeebTime/VideoEncoder
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import dns.resolver
from pyrogram import idle
from aiohttp import *
from web import *

from . import app, log, port

dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = [
    '8.8.8.8']  # this is a google public dns



import logging
import time
import os
import nest_asyncio
from pyrogram import Client
from pyromod import listen
from pyromod import listen
import os
import pytz
import datetime
from uploader.database.database import Database
from uploader.config import Config

nest_asyncio.apply()

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


BOT = Client(
    name=Config.SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="VideoEncoder"),
)

Start_Time = time.time()



