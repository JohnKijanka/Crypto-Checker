from fastapi import FastAPI
import aiohttp
import asyncio

app = FastAPI()

CRYPTO_API_URL = "https://api.coingecko.com/api/v3/simple/price"

async def fetch_price(session, crypto):
    params = {
        'ids': crypto,
        'vs_currencies': 'usd'
    }
    async with session.get(CRYPTO_API_URL, params=params) as response:
        return await response.json()

@app.get("/prices")
async def get_prices(cryptos: str):
    crypto_list = cryptos.split(',')
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_price(session, crypto) for crypto in crypto_list]
        prices = await asyncio.gather(*tasks)
        return {crypto: price for crypto, price in zip(crypto_list, prices)}
