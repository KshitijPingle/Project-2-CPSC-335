from datetime import datetime, timedelta    

def parse_time(time_str):
    # Using the datetime library, we can quickly compute the time where 60m = 1hr.
    return datetime.strptime(time_str, "%H:%M")

def calculate_free_slots(busy_intervals, login, logout):
    # Create a empty list to record "free" times the two people are allowed to work together.
    free_slots = []
    current_login = login
    
    # Iterate through each busy_intervals that the people have.
    for login, logout in busy_intervals:
        
        # Append the free time between current time and the start of the busy time slot.
        if current_login < login:
            free_slots.append((current_login, login))
            
        # Update the iteration to start AFTER a busy_interval, to ensure that we don't iterate through a busy_interval.
        current_login = max(current_login, logout)
        
    # If there are no more busy_intervals, however there are still time remaining before a person clocks out, add the remaining interval.
    if current_login < logout:
        free_slots.append((current_login, logout))
        
    # Returns a list of available free time slots for us to work with.
    return free_slots

def intersect_slots(slot_lists):
    # Allow the first person's free available slot time as the starting point of our iteration.
    common_slots = slot_lists[0]
    
    # We iterate through all the free times that both people have.
    for slots in slot_lists[1:]:
        
        # Create a new list to store free times that both people have in common
        updated_common_slots = []
        i, j = 0, 0
        
        # Compare and iterate through the free times from both lists
        while i < len(common_slots) and j < len(slots):
            
            # Classify the current time slots from each individual time slots.
            login1, logout1 = common_slots[i]
            login2, logout2 = slots[j]
            
            # Find the latest_login and earlist logout between the two individual time slots.
            latest_login = max(login1, login2)
            earliest_logout = min(logout1, logout2)
            
            # If the free time slots have a common similarity, append the common time slot.
            if latest_login < earliest_logout:
                updated_common_slots.append((latest_login, earliest_logout))
                
            # Move to the next slot in the list that has a earlier logout time
            if logout1 < logout2:
                # Iterate through the first person's free time slots 
                i += 1
            else:
                # Iterate through the second person's free time slots
                j += 1
        
    # Return the new updated_common_slots
    return updated_common_slots

def find_common_free_times(busy_schedule, working_period, duration_of_meeting):
    # Use the function timedelta in library datetime to convert the minutes in duration_of_meeting for easier comparison.
    duration_of_meeting = timedelta(minutes=duration_of_meeting)
    # Create a list to hold the free time slots for all people.
    member_free_times = []
    
    # Iterate over each person's busy_schedule to compute their free time slots
    for i, slots in enumerate(busy_schedule):
        # Call the 
        login, logout = map(parse_time, working_period[i])
        member_slots = [(parse_time(start), parse_time(end)) for start, end in slots]
        
        free_slots = calculate_free_slots(member_slots, login, logout)
        member_free_times.append(free_slots)
        
    common_free_times = intersect_slots(member_free_times)
    
    result = [(start, end) for start, end in common_free_times if (end - start) >= duration_of_meeting]
    
    return [[start.strftime("%H:%M"), end.strftime("%H:%M")] for start, end in result]