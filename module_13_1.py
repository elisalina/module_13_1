import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(10 / power)
        print(f'Силач {name} поднял {i}')
    print(f'Силач {name} закончил соревнования.')
async def start_tournament():
    first_task = asyncio.create_task(start_strongman('Pasha', 3))
    second_task = asyncio.create_task(start_strongman('Denis', 4))
    third_task = asyncio.create_task(start_strongman('Apollon', 5))
    await first_task
    await second_task
    await third_task

asyncio.run(start_tournament())







