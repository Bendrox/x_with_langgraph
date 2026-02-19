import asyncio
import time


async def tache_async(nom_tache: str ,duree:int):
    print(f"Début opération : {nom_tache}")
    await asyncio.sleep(duree)
    print(f"Fin opération: {nom_tache}")

async def main():
    start_time= time.time()
    
    await asyncio.gather(
            tache_async("Collecte",2), 
            tache_async("Enregistrement", 4)) 
        
    end_time= time.time()
    
    duree= end_time - start_time
    
    print(f"Total run : {duree} sec")
        
asyncio.run(main())