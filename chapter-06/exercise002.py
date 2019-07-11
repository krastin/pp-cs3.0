import calendar
import datetime


def next_leap_year(current_year: int) -> int:
    """ Prints out which year is the next leap year after current_year

    >>> next_leap_year(2019)
    2020
    >>> next_leap_year(2018)
    2020
    >>> next_leap_year(2020)
    2024
    """

    iter_year = current_year + 1
    while True:
        if calendar.isleap(iter_year):
            return iter_year

def leap_years_between(year1: int, year2: int) -> int:
    """ determine how many leap years there will be between the years year1 and year2 inclusive

    >>> leap_years_between(2018,2020)
    1
    >>> leap_years_between(2017,2022)
    1
    >>> leap_years_between(2000,2020)
    6
    """

    return calendar.leapdays(year1-1, year2+1)

def which_day_of_the_week(year: int, month: int, day: int) -> str:
    """determine which day of the week the year, month, day date is

    >>> which_day_of_the_week(2016, 7, 29)
    Friday
    """
    weekdays = []
    weekdays.append('Monday')
    weekdays.append('Tuesday')
    weekdays.append('Wednesday')
    weekdays.append('Thursday')
    weekdays.append('Friday')
    weekdays.append('Saturday')
    weekdays.append('Sunday')

    return weekdays[calendar.weekday(year, month, day)]
    
if __name__ == "__main__":
    current_year = datetime.datetime.now().year
    current_year_is_leap = 'is' if calendar.isleap(current_year) else 'is not'
    print('Current year is: %d. It %s a leap year!' % (current_year, current_year_is_leap))

    print('Next leap year is:', next_leap_year(current_year))

    print('Leap years between 2000 and 2050 inclusive are', leap_years_between(2000,2050))

    print('29 July 2016 is a', which_day_of_the_week(2016, 7, 29))