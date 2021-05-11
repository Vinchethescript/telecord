import aiogram
import asyncio
import discord
from discord.ext.commands import Bot as Discord
from aiogram import Bot as Telegram


class Bot(discord.ext.commands.Bot, aiogram.Bot):
    def __init__(*args, **kwargs):
        tgtk = kwargs.pop("telegram", None)
        dstk = kwargs.pop("discord", None)
        prefix = kwargs.pop("command_prefix", None)
        self.loop = kwargs.pop("loop", asyncio.get_event_loop())
        super(Discord, self).__init__(
            command_prefix=command_prefix, loop=self.loop, *args, **kwargs
        )
        super(Telegram, self).__init__(token=tgtk, loop=self.loop, *args, **kwargs)
        self.telegram_token = tgtk
        self.discord_token = dstk
