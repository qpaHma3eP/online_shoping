import asyncio
import aiohttp
from bs4 import BeautifulSoup


url = 'https://quotes.toscrape.com/'


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.text()
            soup = BeautifulSoup(result, 'html.parser')
            quotes = soup.find_all('span', {'class': 'text'})
            authors = soup.find_all('small', {'class': 'author'})
            tags = soup.find_all('meta', {'class': 'keywords'})

            for i in range(len(quotes)):

                print(f'{quotes[i].text}\n'
                      f'{authors[i].text}\n'
                      f'Tags: {tags[i].get('content')}\n'
                      f'***********************************************')


asyncio.run(main())