from schedule import *
import json

def arrange_meeting(input_file, output_file) :
    # Parse JSON input from input.txt
    with open(input_file) as f:
        json_data = json.load(f)

    # 'json_data' is a list of all test cases
    # 'data' is a list of test cases
    # last element of 'data' is the duration of the meeting
    # each 'data' object represents one test case
        # data = [ {person1}, {person2}, ... , duration_of_meeting ]
    # Each person dictionary has the following keys
        # person = { 'schedule': [ [busy_slot1], [busy_slot2], ... ], 'daily_activity': [start, end] }

    output_str = "Number of Tests: " + str(len(json_data)) + "\n"
    test_num = 1

    # Run through all test cases
    for test in json_data :
        people = []
        for i in range(len(test)):
            people.append(test[i])

        # Doing this for now to test the json stuff
        person1_schedule = people[0]['Schedule']
        person1_DailyAct = people[0]['DailyAct']

        person2_schedule = people[1]['Schedule']
        person2_DailyAct = people[1]['DailyAct']

        # Last element of 'test' is always the duration of the meeting
        duration_of_meeting = int(test[-1])

        busy_slots = [person1_schedule, person2_schedule]
        working_period = [person1_DailyAct, person2_DailyAct]

        common_free_times = find_common_free_times(busy_slots, working_period, duration_of_meeting)
        output_str += "\nTest Case " + str(test_num) + " Output:\n" + str(common_free_times) + "\n"
        test_num += 1

    
    with open(output_file, "w") as f:
        f.write(output_str)
# End of arrange_meeting() function


if (__name__ == "__main__") :
    arrange_meeting("input.json", "output.txt")