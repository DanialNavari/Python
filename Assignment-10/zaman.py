class zaman:
    def __init__(self , h, m, s, l):
        #properties
        self.hour = h
        self.minute = m
        self.second = s
        self.local_time = l

    #methods
    def hour_to_second(self):
        #convert second to hour for example 1 h => 3600 s
        ...

    def minute_to_second(self):
        #convert minutes to seconds for example 60 m => 1 h
        ...
    
    def second_to_hour(self):
        #convert second to hour for example 3600 s => 1 h
        ...
    
    def H_12(self):
        #convert time to 12 hours for example 14:00:00 => 2pm
        ...
    
    def H_2(self):
        #convert time to 24 hours for example 2pm => 14:00:00
        ...

    def now_to_local_time(self):
        #convert time to other countries local time
        ...