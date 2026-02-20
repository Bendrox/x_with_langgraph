import asyncio
import time

async def tache(time: int, name:str):
     print(f"Starting {name}")
     await asyncio.sleep(time)
     print(f"{name} operation finished ! ")

async def main():
    start=time.time()
    await asyncio.gather(
        tache(2, "training"),
        tache(3, "evaluating")
    ) 
    end=time.time()
    duration=end-start
    print(f'the function lasted {duration}')

asyncio.run(main())

     
