# Konnor Boucher, Operating Systems, Section 2 4-6:45 PM

from Process import Process # imports object to hold processes
from RandomProcessHelper import * # creates random times and has functions to get avg times
import pandas as pd # imports pandas to create the table and manage it

process_list = [] # contains all processes that aren't done yet
waiting = [] # queue
finished = [] # will make outputing much easier and more consistent
time = 0 # time starts at 0
q = 2 # quantum is 2 in this case
cs = 0 # context switch is 0 in this case

# interarrival times between 5 and 10
interarrival_lowB = 5
interarrival_upB = 10

# service times between 4 and 8
service_lowB = 4
service_upB = 8

interarrival_times = get_interarrival_times(interarrival_lowB, interarrival_upB) # uses bounds to generate 99 values 5 - 10
service_times = get_service_times(service_lowB, service_upB) # uses bounds to generate 100 values 4 - 8
arrival_times = get_arrival_times(interarrival_times) # uses interarrival times to get arrival times

for i in range(100):
    process_list.append(Process(i + 1, service_times[i], arrival_times[i])) # adds the 100 created processes to the list

finished = list(process_list) # copies all processes to finished list

while process_list: # while processes aren't done, yet queue is empty
    for process in process_list:
        if (process.a_time <= time) and (process.in_queue == False):
            waiting.append(process) # checks to see if processes arrived every quantum, adds them to the queue if they have
            process.in_queue = True

    if not waiting:
        time += 1 # increments time by 1 if CPU there is nothing for the CPU to do, yet there is still processes that will arrive later

    while waiting: # while processes are in the queue
        working_process = waiting[0] # grabs the process in the front of the queue
        
        if working_process.been_sent == False: # checks to see if process is on its first time on CPU
            working_process.get_i_wait(time) # gets initial wait now
            working_process.get_start(time) # gets start time now
            working_process.been_sent = True # switches to true as it has now been sent
        
        if working_process.time_left <= q: # checks if process will be done during this quantum
            time += working_process.time_left # all time left is added to time because an entire quantum isn't used
            working_process.get_end(time) # gets the end time and turnaround time
            working_process.get_t_wait(time) # gets the total wait time
            
            waiting.pop(0) # pops off the process that was just executed
            time += cs # adds in context switch time if necessary

            for i in range(len(process_list)): # removes the process that is now done from the process list
                my_process = process_list[i]
                if working_process.ID == my_process.ID:
                    process_list.pop(i)
                    break

        else:
            time += q # adds a quantum to the time
            working_process.time_left -= q # subtracts a quantum from the time left

            waiting.pop(0) #only pops it off the waiting list, as it still needs more CPU time
            time += cs # adds in context switch time if neccesary

    for process in process_list:
        if (process.a_time <= time) and (process.in_queue == False):
            waiting.append(process) # checks to see if processes arrived every quantum again, ensuring any 
            process.in_queue = True # arriving processes get on the queue before the Round Robin
    
    for process in process_list:
        process.in_queue = False # allows values previously added to the queue to be added again

ID_list = []
start_list = []
i_wait_list = []
end_list = [] # Collections of each of these attributes for all the processes
t_wait_list = []
turnaround_list = []

for process in finished:
    ID_list.append(process.ID)
    start_list.append(process.start)
    i_wait_list.append(process.i_wait)
    end_list.append(process.end)
    t_wait_list.append(process.t_wait)
    turnaround_list.append(process.turnaround)

# Here we get all of the average times we need to output, and output them
avg_interarrival = round(get_avg(interarrival_times), 2)
print("Average Interarrival Time:", avg_interarrival)

avg_service = round(get_avg(service_times), 2)
print("Average Service Time:", avg_service)

avg_turnaround = round(get_avg(turnaround_list), 2)
print("Average Turnaround Time:", avg_turnaround)

avg_t_wait = round(get_avg(t_wait_list), 2)
print("Average Total Wait Time:", avg_t_wait)
print()

# Outputing the Table

columns = {
    "ID": ID_list,
    "Start Time": start_list,
    "Initial Wait": i_wait_list, # creates the columns for the table
    "End Time": end_list,
    "Total Wait Time": t_wait_list,
    "Turnaround Time": turnaround_list
}

table = pd.DataFrame(columns) # creates the table using our columns we created

print("First 10 Processes:")
print(table.head(10).to_string(index=False)) # prints first 10 rows, without the index Pandas uses as we have our own
print()
print("Last 10 Processes:")
print(table.tail(10).to_string(index=False)) # prints last 10 rows, without the index Pandas uses as we have our own
print()

# Allows entire table to be output
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print("Entire Table of Output:")
print(table.to_string(index=False)) # Outputs entire table

