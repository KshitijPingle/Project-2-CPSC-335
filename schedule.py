from datetime import datetime, timedelta    

def parse_time(time_str):
    # Using the datetime library, we can quickly compute the time where 60m = 1hr.
    return datetime.strptime(time_str, "%H:%M")

def calculate_free_slots(busy_intervals, login, logout):
    free_slots = []
    current_start = login
    
    busy_intervals = sorted(busy_intervals)
    
    for start, end in busy_intervals:
        if current_start < start:
            free_slots.append((current_start, start))
        current_start = max(current_start, end)
        
    if current_start < logout:
        free_slots.append((current_start, logout))
        
    return free_slots

def intersect_slots(slot_lists):
    common_slots = slot_lists[0]
    
    for slots in slot_lists[1:]:
        updated_common_slots = []
        i, j = 0, 0
        
        while i < len(common_slots) and j < len(slots):
            login1, logout1 = common_slots[i]
            login2, logout2 = slots[j]
            
            latest_login = max(login1, login2)
            earliest_logout = min(logout1, logout2)
            
            if latest_login < earliest_logout:
                updated_common_slots.append((latest_login, earliest_logout))
                
            if logout1 < logout2:
                i += 1
            else:
                j += 1
                
        common_slots = updated_common_slots
        
    return common_slots

def find_common_free_times(busy_schedule, working_period, duration_of_meeting):
    duration_of_meeting = timedelta(minutes=duration_of_meeting)
    member_free_times = []
    
    for i, slots in enumerate(busy_schedule):
        login, logout = map(parse_time, working_period[i])
        member_slots = [(parse_time(start), parse_time(end)) for start, end in slots]
        
        free_slots = calculate_free_slots(member_slots, login, logout)
        member_free_times.append(free_slots)
        
    common_free_times = intersect_slots(member_free_times)
    
    result = [(start, end) for start, end in common_free_times if (end - start) >= duration_of_meeting]
    
    return [[start.strftime("%H:%M"), end.strftime("%H:%M")] for start, end in result]