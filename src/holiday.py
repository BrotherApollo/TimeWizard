from datetime import date, timedelta

class USFedHolidays(dict):
    """Object becomes a dictionary of {date: holiday name} 
    for the holidays of the given year(s)"""
    
    def __init__(self, years: int|list[int]):
        super().__init__()
        
        # Converting int to list[int]
        if isinstance(years, int):
            years = [years]
        
        for year in years:
            self._populate_year(year)
    
    def _populate_year(self, year):
        """Updates self with holidays from given year
        key is date object, value is string of holiday name"""
        def nth_weekday(month:int, weekday:int, n:int):
            """
            Returns the nth weekway occurance of a month
            '3rd monday in Jan' logic
            """
            d = date(year, month, 1)
            while d.weekday() != weekday:
                d += timedelta(days=1) # Moving forward 1 day
            return d + timedelta(weeks=n-1) # Advancing to the nth week
        
        def last_weekday(month:int, weekday:int):
            """
            Returns date object of the last target weekday of a month
            `last monday in May` logic
            """
            d = date(year, month+1, 1) - timedelta(days=1)
            while d.weekday() != weekday:
                d -= timedelta(days=1)
            return d
        
        holidays = {
            # Fixed date holidays
            date(year, 1, 1): "New Year's Day",
            date(year, 6, 19): "Juneteenth",
            date(year, 7, 4): "Independence Day",
            date(year, 11, 11): "Veteran's Day",
            date(year, 12, 25): "Christmas Day",
            
            # Weekday based holidays
            nth_weekday(1, 0, 3): "Martin Luther King Jr. Day", # Third Monday in Jan
            nth_weekday(2, 0, 3): "Presidents' Day", # Third Monday in Feb
            last_weekday(5, 0): "Memorial Day", # Last Monday in May
            nth_weekday(9, 0, 1): "Labor Day", # First Monday in Sep
            nth_weekday(10, 0, 2): "Columbus Day", # Second Monday in Oct
            nth_weekday(11, 3, 4): "Thanksgiving", # 4th Thursday in Oct
        }
        
        self.update(holidays)