""" 
Handles asynchronous API calls: 
- Fetch multiple GitHub users concurrently 
- Fetch GitHub + Weather data together 
- Async retry & logging support 

""" 
 
import asyncio 
import aiohttp 
from api_utils import fetch_github_user, fetch_weather, fetch_with_retry, log_result_async 
 
# Async Part B: Multiple GitHub Users 
 
async def fetch_multiple_github_users(usernames): 
    """Fetch multiple GitHub users concurrently and sort by repo count.""" 
    
    async with aiohttp.ClientSession() as session: 
        tasks = [fetch_github_user(session, user) for user in usernames] 
        results = await asyncio.gather(*tasks) 
        results = [r for r in results if r["public_repos"] is not None] 
        sorted_results = sorted(results, key=lambda x: x["public_repos"], reverse=True) 

        print("\n   Part B GitHub Users Sorted by Public Repos   ") 
        for r in sorted_results: 
            print(f"{r['login']}: {r['public_repos']} repos - {r['html_url']}") 
        return sorted_results 
 

# Async Part C: GitHub + Weather Together 


async def fetch_github_and_weather(usernames): 
    """Run GitHub and weather API calls concurrently.""" 
   
    async with aiohttp.ClientSession() as session: 
        github_tasks = [fetch_github_user(session, user) for user in usernames] 
        weather_task = fetch_weather(session) 
        results = await asyncio.gather(*github_tasks, weather_task) 
        *users, weather = results 
        top_user = max(users, key=lambda x: x["public_repos"]) 
        
        print("\n   Part C Combined Summary  ") 
        print(f"Top User: {top_user['login']} ({top_user['public_repos']} repos)") 
        print(f"Profile: {top_user['html_url']}") 
        print(f"Weather → Temp: {weather['temperature']}°C, Wind: {weather['windspeed']} km/h @ {weather['time']}") 
        
        return {"top_user": top_user, "weather": weather} 
 

# Async Bonus: Retry + Logging 


async def async_retry_and_log_demo(): 
    """Demonstrate async retry on failed request and async logging.""" 
    
    async with aiohttp.ClientSession() as session: 
        print("\n   Async Retry + Logging Demo   ") 
        url = "https://api.github.com/users/rmjovia"  # my github account
        data = await fetch_with_retry(session, url, retries=3) 
        await log_result_async("async_log.txt", data or {"error": "Failed after retries"}) 
        
        print("Logged result to async_log.txt")