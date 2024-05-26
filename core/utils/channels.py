from contextlib import asynccontextmanager

import grpc as g
from grpc.experimental import aio
from loguru import logger
from settings import settings

_SERVER_ADDR_CHANNEL = f"{settings.HOST_GRPC}:{settings.PORT_GRPC}"


@logger.catch
@asynccontextmanager
async def createClientChannelWithToken(token):
    channel = None
    token_credential = g.access_token_call_credentials(token)
    composite_credentials = g.composite_channel_credentials(
        g.local_channel_credentials(),
        token_credential,
    )
    try:
        channel = aio.secure_channel(_SERVER_ADDR_CHANNEL, composite_credentials)
        logger.info("Success opened channel...")
        yield channel
    finally:
        logger.info("Closing opened channel...")
        await channel.close()


@logger.catch
@asynccontextmanager
async def createClientChannel():
    channel = None
    try:
        channel = aio.insecure_channel(_SERVER_ADDR_CHANNEL)
        logger.info("Successfully opened channel...")
        yield channel
    finally:
        if channel:
            logger.info("Closing channel...")
            await channel.close()
