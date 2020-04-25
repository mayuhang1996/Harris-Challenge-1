# CHALLENGE PROBLEMS
# YOU MAY NOT USE ANY ADDITIONAL LIBRARIES OR PACKAGES TO COMPLETE THIS CHALLENGE
print('Yuhang Ma, 12244697')
# Divvy is Chicago's bike share system, which consists of almost 600 stations scattered
# around the city with blue bikes available for anyone to rent. Users begin a ride by removing
# a bike from a dock, and then they can end their ride by returning the bike to a dock at any Divvy 
# station in the city. You are going to use real data from Divvy collected at 1:30pm on 4/7/2020 
# to analyze supply and demand for bikes in the system. 

# NOTE ** if you aren't able to run this, type "pip install json" into your command line
import json

# do not delete; this is the data you'll be working with
divvy_stations = json.loads(open('divvy_stations.txt').read())

# PROBLEM 1
# find average number of empty docks (num_docks_available) and 
# available bikes (num_bikes_available) at all stations in the system
print('PROBLEM 1:')
#average number of empty docks
total=0
for i in range(len(divvy_stations)):
    total+=divvy_stations[i]['num_docks_available']
    # print(divvy_stations[i]['num_docks_available'])
    # print(total)
mean=total/len(divvy_stations)
result='The average number of empty docks is {}.'.format(mean)
print(result)

#average number of available bikes
total=0
for i in range(len(divvy_stations)):
    total+=divvy_stations[i]['num_bikes_available']
    # print(divvy_stations[i]['num_bikes_available'])
    # print(total)
mean=total/len(divvy_stations)
result='The average number of available bikes is {}.'.format(mean)
print(result)

# PROBLEM 2
# find ratio of bikes that are currently rented to total bikes in the system (ignore ebikes)
print('PROBLEM 2:')
total=0
avail=0
for i in range(len(divvy_stations)):
    total+=divvy_stations[i]['num_docks_available']+divvy_stations[i]['num_bikes_available']
    avail+=divvy_stations[i]['num_docks_available']
ratio=avail/total
result='Ratio of bikes that are currently rented to total bikes in the system is {}.'.format(ratio)
print(result)

# PROBLEM 3 
# Add a new variable for each divvy station's entry, "percent_bikes_remaining", that shows 
# the percentage of bikes available at each individual station (again ignore ebikes). 
# This variable should be formatted as a percentage rounded to 2 decimal places, e.g. 66.67%
print('PROBLEM 3:')
for i in range(len(divvy_stations)):
    divvy_stations[i]['percent_bikes_remaining']=str(round(divvy_stations[i]['num_bikes_available']/(divvy_stations[i]['num_bikes_available']+divvy_stations[i]['num_docks_available'])*100,2))+'%'
    # print(divvy_stations[i])
# print(divvy_stations[2])