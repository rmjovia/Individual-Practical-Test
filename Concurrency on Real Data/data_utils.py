""" 
Helper functions for concurrent data fetching and analysis (using threading or multiprocessing). 
""" 
 
import urllib.request 
import csv 
from functools import reduce 
 
# Dataset URLs 
URL_POPULATION = "https://raw.githubusercontent.com/datasets/population/master/data/population.csv" 
URL_COVID = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.csv" 
URL_TEMP = "https://datahub.io/core/global-temp/r/annual.csv" 
 
def download_dataset(name, url): 
    """Download CSV dataset from a URL and return list of dicts.""" 
    print(f"[{name}] Starting download...") 
    response = urllib.request.urlopen(url) 
    data = [line.decode("utf-8") for line in response.readlines()] 
    rows = list(csv.DictReader(data)) 
    print(f"[{name}] Download complete. Rows: {len(rows)}") 
    return rows 
 
 
# ANALYSIS FUNCTIONS  
 
def compute_population(data): 
    """Compute total world population for year 2020.""" 
    data_2020 = list(filter(lambda r: r["Year"] == "2020", data)) 
    pops = map(lambda r: int(float(r["Value"])), data_2020) 
    total = reduce(lambda a, b: a + b, pops, 0) 
    print(f"[Population] Total (2020): {total:,}") 
    return total 
 
 
def compute_covid(data): 
    """Compute total new COVID cases.""" 
    cases = [float(r["new_cases"]) for r in data if r["new_cases"] not in ("", None)] 
    total = sum(cases) 
    print(f"[COVID] Total New Cases: {total:,.0f}") 
    return total 
 
 
def compute_temperature(data): 
    """Compute average global temperature.""" 
    temps = [float(r["Mean"]) for r in data if r["Mean"] not in ("", None)] 
    avg = sum(temps) / len(temps) 
    print(f"[Temperature] Average Global Temp: {avg:.3f}°C") 
    return avg 