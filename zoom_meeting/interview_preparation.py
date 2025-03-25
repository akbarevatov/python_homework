


class Date:
    def __init__(self, day: int, month: int, year: int):
        self.months_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        if day<1 or day>31: raise ValueError("Invalid value for days")
        if month<1 or month>12: raise ValueError("Invalid value for months")
        self.day = day
        self.month = month
        self.year = year
    
    def backslash(self):
        return f"{self.month}/{self.day}/{self.year}"
    
    def with_comma(self):
        return f"{self.months_list[self.month-1]} {self.day}, {self.year}"
    
    def without_comma(self):
        return f"{self.day} {self.months_list[self.month-1]} {self.year}"

date1 = Date(25, 12, 2025)
print(date1.backslash())