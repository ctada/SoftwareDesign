""" A practice problem for object-oriented programming """

class Date(object):
    """ Represents a particular day on the calendar """
    def __init__(self, month, day, year):
        """ Initializes a Date object

            month: the month (represented as an integer in [1,12])
            day: the day of the month (represented as an integer)
            year: the year (represented as an integer)
            This method will not validate whether a given date is invalid
            (e.g. April 31, 2000) """
<<<<<<< HEAD
        self.month = month
        self.day = day
        self.year = year
=======
        pass
>>>>>>> 5d728c19d7ef961a52d640267312c597cf953983


    def is_before(self,other_date):
        """ Returns true if and only if self occurs before other_date

            >>> d1 = Date(4,20,1981)
            >>> d2 = Date(5,31,1995)
            >>> d1.is_before(d2)
            True
        """
<<<<<<< HEAD
        if self.year<other_date.year:
            return True
        elif self.year == other_date.year:
            if self.month < other_date.month:
                return True
            elif self.month > other_date.month:
                return False
            elif self.month == other_date.month and self.day < other_date.day:
                return True
            else:
                return False
        else:
            return False
=======
        pass
>>>>>>> 5d728c19d7ef961a52d640267312c597cf953983


    def __str__(self):
        """ Converts the date to a string in the following format:
            Month, Day Year (where Month is the name of the month, e.g. January)

        >>> print Date(3,26,2015)
        March, 26th 2015
        """
<<<<<<< HEAD
        month_ref=dict(zip(range(1,13), ['January','February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']))
        return str.format('{month}, {day}th {year}', month=month_ref[self.month], day= self.day, year=self.year)
=======
        pass
>>>>>>> 5d728c19d7ef961a52d640267312c597cf953983

    def increment_year(self):
        """ Modifies the Date object self so that it represents a date of the
            same month and day but for the following year. """
<<<<<<< HEAD
        self.year += 1
=======
        pass
>>>>>>> 5d728c19d7ef961a52d640267312c597cf953983

    def is_leap_year(self):
        """ Returns true if the year that this date falls in is a leap year
            see: http://en.wikipedia.org/wiki/Leap_year
<<<<<<< HEAD
            A leap year is every 4 years, but not every 100 years, then again every 400 years.

            Note: please add appropriate doctests BEFORE you start coding 

            >>> Date(1,2,1964).is_leap_year()
            True
            >>> Date(1,2,1965).is_leap_year()
            False
        """

        yr = self.year
        if not yr%4 == 0:
            return False
        elif not yr%100 == 0: #if divisible by 4 and not divisible by 100
            return True
        elif not yr%400 == 0: #if divisible by 4, divisible by 100 and not divisible 400
            return False
        else:
            return True
=======

            Note: please add appropriate doctests BEFORE you start coding """
        pass
>>>>>>> 5d728c19d7ef961a52d640267312c597cf953983

if __name__ == '__main__':
    import doctest
    doctest.testmod()