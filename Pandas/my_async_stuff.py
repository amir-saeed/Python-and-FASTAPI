import asyncio
import aiohttp

async def download_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    page1 = asyncio.create_task(download_page("https://www.microsoft.com"))
    page2 = asyncio.create_task(download_page("https://www.google.com"))

    results = await asyncio.gather(page1, page2)
    print(results[0][:50]) #print the first 50 characters of the first downloaded webpage.
    print(results[1][:50]) #print the first 50 characters of the second downloaded webpage.

if __name__ == "__main__":
    asyncio.run(main())