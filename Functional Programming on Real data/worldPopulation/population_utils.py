"""
contains utility functional programming tasks on the population data.
each function here is reusable, instead of crowding the world_population file

"""


import csv
from functools import reduce
from operator import itemgetter
import urllib.request

#1 load the data from the given url
def load_population_data (url) :
    response = urllib.request.urlopen(url)
    lines = [line.decode('utf-8') for line in response.readlines()]  
    reader = csv.DictReader(lines)    
    return list(reader)       #return a list of dictionaries


#2 filter rows by year

def filter_year (rows, year = "2020"):
    #filter rows for the given year
    return filter (lambda r: r["Year"] == str(year), rows)


#3 Map to tuples (Country Name, Population)

def to_country_pop (rows):
    return map (lambda r: (r["Country Name"], int(float(r["Value"]))), rows)


#4 Sort and print the top 5 most populated countries

def sort_by_pop_desc (pairs):
    return sorted (pairs, key=itemgetter(1), reverse=True)


#5 Compute total world population using reduce()

def total_population(pairs):  
    """compute t/l popln from (country, pop) pairs using reduce()"""
    return reduce (lambda acc, x: acc + x[1], pairs, 0)

#6 filter and reduce african countries

def africa_population_stats(pairs):
    african_countries = {
        "Nigeria", "Ethiopia", "Egypt", "DR Congo", "Tanzania", "South Africa",
        "Kenya", "Uganda", "Sudan", "Algeria", "Morocco", "Angola", "Ghana"
    }

    africa_data = list(filter(lambda x: x[0] in african_countries, pairs))
    total = reduce(lambda acc, x: acc + x[1], africa_data, 0)
    avg = total / len(africa_data) if africa_data else 0

    return africa_data, total, avg



#7 & 8 higher-order function apply_and_log(func, iterable).

def apply_and_log (func, iterable):

    """
    apply a func to each item in an iterable and log before/after
    demonstartes higher_order func concepts

    """

    print(f"\nApplying function: {func.__name__ if hasattr (func, '__name__') else func}")
    results = list(map(func, iterable))

    print (f" Applied to {len(iterable)} items. Sample result: {results[:3 ]}")
    return results


#9  composed functional pipeline for top 5 populated countries.

def top_countries_pipeline (data, year="2020", top_n=5):

    """ this pipeline combines filter - map - sort - slice to get top N ountries"""

    return list(sort_by_pop_desc(to_country_pop(filter_year(data, year)))) [:top_n] 