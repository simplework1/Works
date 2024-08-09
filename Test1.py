import asyncio
from concurrent.futures import ThreadPoolExecutor

async def my_async_function():
    print("Hello from async function!")

def start_async_task():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(my_async_function())
    loop.close()

def main():
    with ThreadPoolExecutor() as executor:
        # Run the async function in a separate thread
        loop = asyncio.get_event_loop()
        loop.run_in_executor(executor, start_async_task)

if __name__ == "__main__":
    main()
