from src.holiday import USFedHolidays
from datetime import date

def test_num_holidays():
    holidays = USFedHolidays(2025)
    assert len(holidays.keys()) == 11
    
    holidays = USFedHolidays([2025, 2026])
    assert len(holidays.keys()) == 22
    
def test_2025_holidays():
    holidays = USFedHolidays(2025)
    
    US_FEDERAL_HOLIDAYS_2025 = [
        date(2025, 1, 1),   # New Year's Day
        date(2025, 1, 20),  # Martin Luther King Jr. Day
        date(2025, 2, 17),  # Washington’s Birthday (Presidents Day)
        date(2025, 5, 26),  # Memorial Day
        date(2025, 6, 19),  # Juneteenth National Independence Day
        date(2025, 7, 4),   # Independence Day
        date(2025, 9, 1),   # Labor Day
        date(2025, 10, 13), # Columbus Day
        date(2025, 11, 11), # Veterans Day
        date(2025, 11, 27), # Thanksgiving Day
        date(2025, 12, 25), # Christmas Day
    ]
    
    for d in US_FEDERAL_HOLIDAYS_2025:
        assert holidays[d]
