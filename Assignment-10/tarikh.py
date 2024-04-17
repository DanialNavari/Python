class tarikh:
    def __init__(self, d, m, y, w, mn):
        # properties
        self.day = d
        self.month = m
        self.year = y
        self.day_name = w
        self.month_name = mn

    # methods
    def convert_miladi_to_shamsi(self):
        #convert en date to persian date for example : 2023/05/28 => 1402/03/07
        ...

    def shamsi_to_miladi(self):
        #convert persian date to en date for example : 1402/03/07 => 2023/05/28
        ...

    def today_date(self):
        #return today date for example : 1402/03/07
        ...
    
    def week_day_name(self):
        #return week day name for example : sunday
        ...

    
