import pytz
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.combining import AndTrigger

from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
from discord import Embed


class AurorianCR(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.scheduler = AsyncIOScheduler(timezone=pytz.timezone('US/Eastern'))
        self.scheduler.start()
        thirdAurorianCR = AndTrigger([CronTrigger(hour=21, minute=10, day_of_week='mon,tue,wed,thu,fri,sat,sun', timezone=pytz.timezone('US/Eastern'))])

        self.scheduler.add_job(self.send_message, thirdAurorianCR)

    async def send_message(self):
        channel = self.client.get_channel(1105751148356456500)  # replace with your channel ID
        embed = Embed(title="Hello World", description="**Spawns in 10 Minutes**", color=0xff0000)
        self.client.loop.create_task(channel.send(embed=embed))

    @commands.Cog.listener()
    async def on_ready(self):
        print("Grimghast Rift Timer Loaded")
        self.scheduler.start()


async def setup(client):
    await client.add_cog(AurorianCR(client))
