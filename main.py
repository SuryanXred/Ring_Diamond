import asyncio

from diamond_ring import main


try:
    loop = asyncio.get_running_loop()
except RuntimeError:
    asyncio.run(main())
else:
    loop.create_task(main())
