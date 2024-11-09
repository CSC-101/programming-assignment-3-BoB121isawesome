from build_data import get_data
from data import CountyDemographics

#Part 1
# Purpose: Calculates the total population across a list of counties
# Input: `somelist` - a list of `CountyDemographics` objects
# Output: Integer representing the sum of the population for each county
# Data Representation: Each `CountyDemographics` object includes a dictionary `population`
#                      with key `"2014 Population"` indicating the population for 2014
def population_total(somelist:list[CountyDemographics])->int:
    population = 0
    for county in somelist:
        population += county.population["2014 Population"]
    return population

#Part 2
#Purpose: Filters counties by a specified state
# Input: `demographics` - a list of `CountyDemographics` objects,
#        `state` - string specifying the state
# Output: List of `CountyDemographics` objects in the specified state
# Data Representation: Each `CountyDemographics` object has an attribute `state`
def filter_by_state(demographics:list[CountyDemographics], state:str)->list[CountyDemographics]:
    county_list=[]
    for county in demographics:
        if county.state == state:
            county_list.append(county)
    return county_list

#Part 3
# Purpose: Calculates the total population by a specified education level across all counties
# Input: `demographics` - a list of `CountyDemographics` objects,
#        `educ` - string specifying the education level
# Output: Float representing the total population with the specified education level.
# Data Representation: Each `CountyDemographics` object contains a dictionary `education` with
#                      education levels as keys, storing percentages. The `population` dictionary
#                      contains the `"2014 Population"`
def population_by_education(demographics:list[CountyDemographics], educ:str) -> float:
    pop = 0
    for county in demographics:
        if educ in county.education:
            pop = pop + county.population["2014 Population"] * (county.education[educ]/100)
    return pop

# Purpose: Calculates the total population by a specified ethnicity across all counties
# Input: `demographics` - a list of `CountyDemographics` objects,
#        `eth` - string specifying the ethnicity
# Output: Float representing the total population of the specified ethnicity
# Data Representation: Each `CountyDemographics` object contains a dictionary `ethnicities`
#                      with ethnicity names as keys, storing percentages.
#                      The `population` dictionary contains the `"2014 Population"`
def population_by_ethnicity(demographics:list[CountyDemographics], eth:str) -> float:
    pop = 0
    for county in demographics:
        if eth in county.ethnicities:
            pop = pop + county.population["2014 Population"] * (county.ethnicities[eth]/100)
    return pop

# Purpose: Calculates the population below the poverty level across all counties
# Input: `demographics` - a list of `CountyDemographics` objects
# Output: Float representing the total population below the poverty level.
# Data Representation: Each `CountyDemographics` object contains a dictionary `income`
#                      with the key `"Persons Below Poverty Level"`, storing a percentage.
#                      The `population` dictionary contains the `"2014 Population"`
def population_below_poverty_level(demographics:list[CountyDemographics]) -> float:
    pop = 0
    for county in demographics:
        pop = pop + county.population["2014 Population"] * (county.income["Persons Below Poverty Level"] / 100)
    return pop

#Task 4
# Purpose: Calculates the percentage of the population with a specified education level
# Input: `demographics` - a list of `CountyDemographics` objects,
#        `educ` - string specifying the education level.
# Output: Float representing the percentage of the population with the specified education level
# Data Representation: Each `CountyDemographics` object contains a dictionary `education`
#                      with education levels as keys, storing percentages.
#                      The `population` dictionary contains the `"2014 Population"`
def percent_by_education(demographics:list[CountyDemographics], educ:str) -> float:
    pop = 0
    total_pop=0
    for county in demographics:
        if educ in county.education:
            pop = pop + county.population["2014 Population"] * (county.education[educ]/100)
            total_pop += county.population["2014 Population"]
    return (pop/total_pop)*100

# Purpose: Calculates the percentage of the population with a specified ethnicity
# Input: `demographics` - a list of `CountyDemographics` objects,
#        `eth` - string specifying the ethnicity
# Output: Float representing the percentage of the population with the specified ethnicity
# Data Representation: Each `CountyDemographics` object contains a dictionary `ethnicities`
#                      with ethnicity names as keys, storing percentages.
#                      The `population` dictionary contains the `"2014 Population"`
def percent_by_ethnicity(demographics:list[CountyDemographics], eth:str) -> float:
    pop = 0
    total_pop=0
    for county in demographics:
        if eth in county.ethnicities:
            pop = pop + county.population["2014 Population"] * (county.ethnicities[eth]/100)
            total_pop += county.population["2014 Population"]
    return (pop/total_pop)*100

# Purpose: Calculates the percentage of the population below the poverty level
# Input: `demographics` - a list of `CountyDemographics` objects
# Output: Float representing the percentage of the population below the poverty level.
# Data Representation: Each `CountyDemographics` object contains a dictionary `income`
#                      with the key `"Persons Below Poverty Level"`, storing a percentage.
#                      The `population` dictionary contains the `"2014 Population"`
def percent_below_poverty_level(demographics:list[CountyDemographics]) -> float:
    pop = 0
    total_pop=0
    for county in demographics:
        pop = pop + county.population["2014 Population"] * (county.income["Persons Below Poverty Level"] / 100)
        total_pop += county.population["2014 Population"]
    return (pop/total_pop)*100

#Part 5
# Purpose: Filters counties with a specified education level percentage greater than a threshold
# Input: `demographics` - a list of `CountyDemographics` objects,
#        `educ` - string specifying the education level, `thresh` - float threshold
# Output: List of `CountyDemographics` objects with the specified education level above the threshold
# Data Representation: Each `CountyDemographics` object contains a dictionary `education`
#                      with education levels as keys, storing percentages
def education_greater_than(demographics:list[CountyDemographics], educ:str, thresh:float) -> list[CountyDemographics]:
    county_list=[]
    for county in demographics:
        if county.education[educ]>thresh:
            county_list.append(county)
    return county_list

# Purpose: Filters counties with a specified education level percentage greater than a threshold
# Input: `demographics` - a list of `CountyDemographics` objects,
#        `educ` - string specifying the education level, `thresh` - float threshold
# Output: List of `CountyDemographics` objects with the specified education level below the threshold
# Data Representation: Each `CountyDemographics` object contains a dictionary `education`
#                      with education levels as keys, storing percentages
def education_lesser_than(demographics:list[CountyDemographics], educ:str, thresh:float) -> list[CountyDemographics]:
    county_list = []
    for county in demographics:
        if county.education[educ] < thresh:
            county_list.append(county)
    return county_list

# Purpose: Filters counties with a specified ethnicity percentage greater than a threshold
# Input: `demographics` - a list of `CountyDemographics` objects,
#        `eth` - string specifying the ethnicity,
#        `thresh` - float threshold
# Output: List of `CountyDemographics` objects where the specified ethnicity percentage is above the threshold.
# Data Representation: Each `CountyDemographics` object contains a dictionary `ethnicities`
#                      with ethnicity names as keys, storing percentages
def ethnicity_greater_than(demographics:list[CountyDemographics], eth:str, thresh:float) -> list[CountyDemographics]:
    county_list = []
    for county in demographics:
        if county.ethnicities[eth] > thresh:
            county_list.append(county)
    return county_list

# Purpose: Filters counties with a specified ethnicity percentage less than a threshold
# Input: `demographics` - a list of `CountyDemographics` objects,
#        `eth` - string specifying the ethnicity,
#        `thresh` - float threshold
# Output: List of `CountyDemographics` objects where the specified ethnicity percentage is below the threshold.
# Data Representation: Each `CountyDemographics` object contains a dictionary `ethnicities`
#                      with ethnicity names as keys, storing percentages
def ethnicity_lesser_than(demographics:list[CountyDemographics], eth:str, thresh:float) -> list[CountyDemographics]:
    county_list = []
    for county in demographics:
        if county.ethnicities[eth] < thresh:
            county_list.append(county)
    return county_list

# Purpose: Filters counties where the percentage of the population below the poverty level is greater than a threshold.
# Input: `demographics` - a list of `CountyDemographics` objects,
#        `thresh` - float threshold
# Output: List of `CountyDemographics` objects where the percentage below the poverty level is above the threshold
# Data Representation: Each `CountyDemographics` object contains a dictionary `income` with the key
#                      `"Persons Below Poverty Level"` that stores a percentage
def below_poverty_level_greater_than(demographics:list[CountyDemographics], thresh:float) -> list[CountyDemographics]:
    county_list=[]
    for county in demographics:
        if county.income["Persons Below Poverty Level"]>thresh:
            county_list.append(county)
    return county_list

# Purpose: Filters counties where the percentage of the population below the poverty level is less than a threshold.
# Input: `demographics` - a list of `CountyDemographics` objects,
#        `thresh` - float threshold
# Output: List of `CountyDemographics` objects where the percentage below the poverty level is below the threshold
# Data Representation: Each `CountyDemographics` object contains a dictionary `income` with the key
#                      `"Persons Below Poverty Level"` that stores a percentage
def below_poverty_level_lesser_than(demographics:list[CountyDemographics], thresh:float) -> list[CountyDemographics]:
    county_list = []
    for county in demographics:
        if county.income["Persons Below Poverty Level"] < thresh:
            county_list.append(county)
    return county_list
