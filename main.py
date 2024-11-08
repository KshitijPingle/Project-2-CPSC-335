from schedule import *
import json

# Parse JSON input from input.txt
with open('input.json') as f:
    data = json.load(f)        

# 'data' is a list of dictionaries, where each dictionary represents a person
    # data = [ {person1}, {person2}, ... ]
# Each person dictionary has the following keys
    # person = { 'schedule': [ [busy_slot1], [busy_slot2], ... ], 'daily_activity': [start, end] }

# Extract data from JSON input
number_of_people = len(data)
people = []     # Make a list to hold all people
for i in range(number_of_people):
    people.append(data[i])

# Doing this for now to test the json stuff
person1_schedule = people[0]['Schedule']
person1_DailyAct = people[0]['DailyAct']

person2_schedule = people[1]['Schedule']
person2_DailyAct = people[1]['DailyAct']

duration_of_meeting = 30

busy_slots = [person1_schedule, person2_schedule]
working_period = [person1_DailyAct, person2_DailyAct]

common_free_times = find_common_free_times(busy_slots, working_period, duration_of_meeting)
print(common_free_times)


# Correct Output
    # [['10:30', '12:00'], ['13:30', '14:00'], ['15:00', '16:00']]