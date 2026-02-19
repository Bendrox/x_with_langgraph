import asyncio


async def tache_async(duree:int):
    print("Début opération")
    await asyncio.sleep(duree)
    print("Fin opération")

async def main():
    await tache_async(2)
    
asyncio.run(main())