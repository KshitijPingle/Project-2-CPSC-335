from schedule import *
import json

# Parse JSON input from input.txt
with open('input.json') as f:
    json_data = json.load(f)

# json_data is a list of two elements
    # 1st element is the number of tests
    # 2nd element is the data  

# 'data' is a list of dictionaries, where each dictionary represents a person
    # data = [ {person1}, {person2}, ... ]
# Each person dictionary has the following keys
    # person = { 'schedule': [ [busy_slot1], [busy_slot2], ... ], 'daily_activity': [start, end] }

# Extract data from JSON input
number_of_tests = int(json_data[0])
data = json_data[1]
number_of_people = len(data)
people = []     # Make a list to hold all people
for i in range(number_of_people):
    people.append(data[i])

# Doing this for now to test the json stuff
person1_schedule = people[0]['Schedule']
person1_DailyAct = people[0]['DailyAct']

person2_schedule = people[1]['Schedule']
person2_DailyAct = people[1]['DailyAct']

# Last element of data is always the duration of the meeting
duration_of_meeting = int(data[-1])

busy_slots = [person1_schedule, person2_schedule]
working_period = [person1_DailyAct, person2_DailyAct]

header = "Number of Tests: " + str(number_of_tests) + "\n"
common_free_times = find_common_free_times(busy_slots, working_period, duration_of_meeting)

with open("output.txt", "w") as f:
    f.write(header)
    f.write(str(common_free_times))