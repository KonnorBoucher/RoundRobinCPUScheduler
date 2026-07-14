import random # imported for random integer generation

def get_avg(my_list): # basic function to calcuate the average value of a list
    total = 0
    n = len(my_list)
    for time in my_list:
        total += time
    return total / n

def get_interarrival_times(lowB, UpB): # takes a lower bound and upper bound, and outputs 99 numbers between those 2 values
    interarrival_list = [0]
    for i in range(99):
        my_rand = random.randint(lowB, UpB)
        interarrival_list.append(my_rand)
    return interarrival_list

def get_service_times(lowB, upB): # takes a lower bound and upper bound, and outputs 100 numbers between the 2 values
    service_list = []
    for i in range(100):
        my_rand = random.randint(lowB, upB)
        service_list.append(my_rand)
    return service_list

def get_arrival_times(my_list): # uses the interarrival times to get the arrival times
    arrival_list = []
    for time in my_list:
        if time == 0:
            arrival_list.append(time)
        else:
            last_element = arrival_list[-1]
            new_element = time + last_element
            arrival_list.append(new_element)
    return arrival_list