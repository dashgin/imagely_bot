from typing import Optional

import aiohttp


def thread_check(threads: Optional[int]) -> None:
    if threads is not None:
        from anyio import CapacityLimiter
        from anyio.lowlevel import RunVar

        RunVar("_default_thread_limiter").set(CapacityLimiter(threads))


async def aget(url: str) -> bytes:
    """Asynchronously get a file from an URL."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            file = await response.read()
            return file
