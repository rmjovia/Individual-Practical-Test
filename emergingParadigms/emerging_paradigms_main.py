""" 
Main driver combining synchronous and asynchronous API usage: 
- Part A: Basic API interaction 
- Part B: Async GitHub calls 
- Part C: GitHub + Weather integration 
- Part D: Bonus async retry + logging 

""" 
 
import asyncio 
from api_utils import fetch_github_user_sync 
from async_api_demo import ( 
    fetch_multiple_github_users, 
    fetch_github_and_weather, 
    async_retry_and_log_demo 
) 
 
# Part A: Basic API Interaction 

def part_a_basic(): 
    print("\n Part A: Basic GitHub API Interaction  ") 
    user = fetch_github_user_sync("octocat") 
    print(f"User: {user['login']}") 
    print(f"Public Repos: {user['public_repos']}") 
    print(f"Profile URL: {user['html_url']}") 


# Run async parts using event loop 

def main(): 
    part_a_basic() 
 
    # Part B: Concurrent GitHub user fetching 
    
    usernames = ["octocat", "torvalds", "mojombo", "pjhyett", "defunkt"] 
    asyncio.run(fetch_multiple_github_users(usernames)) 
 
    # Part C: Concurrent GitHub + Weather 
    
    asyncio.run(fetch_github_and_weather(usernames)) 
 
    # Bonus: Async retry & logging 
    
    asyncio.run(async_retry_and_log_demo()) 
 
if __name__ == "__main__": 
    main()