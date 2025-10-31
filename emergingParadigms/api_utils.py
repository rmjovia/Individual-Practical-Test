""" 
Utility functions for basic and asynchronous API interaction. 
Demonstrates: 
- Synchronous fetch using requests 
- Asynchronous fetch using aiohttp 
- Async retry mechanism 

""" 
 
import asyncio 
import aiohttp
import aiofiles 
import requests 
import json 
 
# Part A: Basic API Interaction 
 
def fetch_github_user_sync(username="octocat"): 
    """Fetch GitHub user data synchronously using requests.""" 
    
    url = f"https://api.github.com/users/{username}" 
    print(f"Fetching data for {username}...") 
    response = requests.get(url) 
    data = response.json() 
    return { 
        "login": data.get("login"), 
        "public_repos": data.get("public_repos"), 
        "html_url": data.get("html_url") 
    } 
 
# Part B: Async API Interaction 
 
async def fetch_github_user(session, username): 
    """Asynchronously fetch GitHub user data with aiohttp.""" 
    
    url = f"https://api.github.com/users/{username}" 
    async with session.get(url) as resp: 
        data = await resp.json() 
        return { 
            "login": data.get("login"), 
            "public_repos": data.get("public_repos"), 
            "html_url": data.get("html_url") 
        } 
 
async def fetch_with_retry(session, url, retries=3, delay=1): 
    """Fetch with async retries and basic error handling.""" 
    
    for attempt in range(1, retries + 1): 
        try: 
            async with session.get(url) as resp: 
                if resp.status == 200: 
                    return await resp.json() 
                else: 
                    print(f"Attempt {attempt}: HTTP {resp.status}") 
        except Exception as e: 
            print(f"Attempt {attempt}: {e}") 
        await asyncio.sleep(delay) 
    return None 
 
async def log_result_async(filename, data): 
    """Log JSON data asynchronously using aiofiles.""" 
    
    async with aiofiles.open(filename, mode='a') as f: 
        await f.write(json.dumps(data, indent=2) + "\n") 
 

# Part C: Cloud API (Open-Meteo) 
 
async def fetch_weather(session, lat=0.3, lon=32.6): 
    """Fetch current weather data from Open-Meteo API.""" 
    
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true" 
    async with session.get(url) as resp: 
        data = await resp.json() 
        current = data.get("current_weather", {}) 
        return { 
            "temperature": current.get("temperature"), 
            "windspeed": current.get("windspeed"), 
            "time": current.get("time") 
        } 