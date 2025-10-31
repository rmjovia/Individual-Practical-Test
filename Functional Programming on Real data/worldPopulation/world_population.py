"""
real data
demonstrates map, filter, reduce, higher-order funcs, and composition

"""
from functools import reduce
import time
from population_utils import (
    load_population_data, filter_year, to_country_pop, sort_by_pop_desc,
    total_population, africa_population_stats, apply_and_log, top_countries_pipeline
)

#load the dataset
URL =  "https://raw.githubusercontent.com/datasets/population/master/data/population.csv"
data = load_population_data(URL)

#a few rows to show immutabilitty before transformation
print ("\n     Original Data Sample   ")
for row in data[:3]:
    print(row)
 

#filter by year 2020 and map to (country, population)

data_2020 = list(filter_year(data, "2020"))
country_pop_2020 = list(to_country_pop(data_2020))

print ("\nFiltered for 2020:", len(country_pop_2020), "records")
print ("Sample:", country_pop_2020[:5])


#Sort and get top 5 most populated countries

top5 = sort_by_pop_desc(country_pop_2020)[:5]

print("\n   Top 5 Most Populated Countries (2020)")

for country, pop in top5:
    print(f"{country}: {pop: ,}")


#compute t/l world popln usinf reduce()

world_total = total_population(country_pop_2020)
print (f"\nTotal world Population (2020): {world_total:,}")


#total + avg popln fro african countries

africa_data, africa_total, africa_avg = africa_population_stats(country_pop_2020)

print (f"\nAfrican countries count: {len(africa_data)}")
print (f"\nTotal Africa Population (2020): {africa_total:,}")
print (f"\nAverage African Population (2020): {africa_avg:,.0f}")


#demonstrating immutability (original data unchanged)

print ("\n    Immutability check     ")
print ("Original dataset length:", len(data))
print ("Filtered dataset length:", len(data_2020))
print ("Original data remains unchanged")


#demonstrating higher-order func

apply_and_log(lambda x: (x[0], round(x[1] / 1_000_000, 2)), top5)


#composed func pipeline

print ("\n   Top 5 via functional Pipeline")
pipeline_result = top_countries_pipeline(data)
for country, pop in pipeline_result:
    print (f"{country}: {pop:,}")



#BONUS: functional vs list comprehension performance

print ("\n   Perfoormance Comparison    ")
start = time.time()
func_total = reduce(lambda acc, x: acc + x[1], country_pop_2020, 0)
func_time = time.time() - start

start = time.time()
comp_total = sum([x[1] for x in country_pop_2020])
comp_time = time.time() - start


print (f"Functional reduce() time: {func_time:.6f}s")
print (f"List Comprehension time: {comp_time:.6f}s")
print (f"Both results match? {func_total == comp_total}")

