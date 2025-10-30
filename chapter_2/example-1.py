import asyncio

async def add_one(number: int) -> int:
    return number + 1

async def main():
    one_plus_one = await add_one(1)
    two_plus_one = await add_one(2)

    print(f'one_plus_one = {one_plus_one}')
    print(f'two_plus_one = {two_plus_one}')

asyncio.run(main())