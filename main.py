from schedule import *
import json

def arrange_meeting(input_file, output_file) :
    # Parse JSON input from input.txt
    with open(input_file) as f:
        json_data = json.load(f)

    # 'json_data' is a list of all test cases
    # 'test' is a list of test cases
        # last element of 'test' is the duration of the meeting
        # each 'test' object represents one test case
            # test = [ {person1}, {person2}, ... , duration_of_meeting ]
    # Each person dictionary has the following keys
        # person = { 'schedule': [ [busy_slot1], [busy_slot2], ... ], 'daily_activity': [start, end] }

    output_str = "Number of Tests: " + str(len(json_data)) + "\n"
    test_num = 1

    # Run through all test cases
    for test in json_data :
        group = test[:-1] # This seperates the intended index of where duration_of_meeting will usually be at.
        duration_of_meeting = int(test[-1]) # duration of meetings required for the people

        # Created two individual lists in order to tackle multiple group members.
        busy_schedule = []
        working_period = []

        # Iterating through each "member" within our dictionary and appending their 'Schedule' and 'DailyAct' to busy_schedule, working_period list respectfully.
        # This was to ensure that there can be multiple memebers within a group, not limiting to two individuals and having those two people only be compared.
        for member in group:
            busy_schedule.append(member['Schedule'])
            working_period.append(member['DailyAct'])

        # Call function find_common_free_times with the new inputs busy_schedule, working_period, duration_of_meeting and find all the members common time to arrange a meeting
        common_free_times = find_common_free_times(busy_schedule, working_period, duration_of_meeting)
        output_str += "\nTest Case " + str(test_num) + " Output:\n" + str(common_free_times) + "\n"
        test_num += 1

    # Print results in output.txt
    with open(output_file, "w") as f:
        f.write(output_str)
# End of arrange_meeting() function


if (__name__ == "__main__") :
    arrange_meeting("input.json", "output.txt")