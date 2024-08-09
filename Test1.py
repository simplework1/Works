import asyncio

# Your asynchronous code here
async def my_async_function():
    print("Hello, World!")

# This code is outside of the main function
try:
    loop = asyncio.get_running_loop()
except RuntimeError:  # No event loop currently running
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

# Now run the asynchronous function
loop.run_until_complete(my_async_function())
