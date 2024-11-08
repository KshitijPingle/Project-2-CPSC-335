from schedule import *

person1_schedule = [['7:00', '8:30'], ['12:00','13:00'], ['16:00','18:00']]
person1_DailyAct = ['9:00','19:00']

person2_schedule = [['9:00','10:30'], ['12:20','13:30'], ['14:00','15:00'], ['16:00','17:00']]
person2_DailyAct = ['9:00','18:30']

duration_of_meeting = 30

busy_slots = [person1_schedule, person2_schedule]
working_period = [person1_DailyAct, person2_DailyAct]

common_free_times = find_common_free_times(busy_slots, working_period, duration_of_meeting)
print(common_free_times)
