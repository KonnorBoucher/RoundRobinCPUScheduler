class Process:
    def __init__(self, ID, s_time, a_time): #initializes the process object when it is first created.
        self.ID = ID
        self.s_time = s_time
        self.a_time = a_time
        self.time_left = s_time
        self.start = 0   #The next 7 attributes start 0 or false but will become integers when these values can be calculated.
        self.end = 0
        self.i_wait = 0
        self.t_wait = 0
        self.turnaround = 0
        self.been_sent = False #used to check if process is on its first time being sent to the CPU
        self.in_queue = False #checks if already waiting in queue
        
    def get_i_wait(self, time):
        self.i_wait = time - self.a_time
        
# gets the total wait time, being how long the process ended up taking minus how much time it needed, adding any initial wait it had.
    def get_t_wait(self, time):
        self.t_wait = self.turnaround - self.s_time + self.i_wait

    def get_start(self, time):
        self.start = time

    def get_end(self, time): #gets end time and turnaround time
        self.end = time
        self.turnaround = self.end - self.a_time