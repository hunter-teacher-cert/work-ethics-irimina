# Julian, Michael

import random

MAX_FAMILY_SIZE = 3


class Aircraft:
    """
    Instance Variables:
        rows: int - number of rows in the plane
        cols: int - number of columns in the plane
        premium_rows: int - number of rows that are premium economy seats
        plane: bool[][] - matrix that represents the plane
    """
    def __init__(self, rows, cols, premium_rows):
        self.rows = rows
        self.cols = cols
        self.premium_rows = premium_rows
        self.plane = [[0 for _ in range(cols)] for _ in range(rows)]

    def __str__(self):
        rows = [''.join([str(seat).center(6) for seat in row]) for row in self.plane]
        string = ''
        for i, row in enumerate(rows):
            row_number = str(i + 1).rjust(len(str(self.rows)))
            string += f'{row_number} {"P" if i < self.premium_rows else "E"} | {row}\n'
        return string

    @property
    def vacant_seats(self):
        """
        Returns how many total seats are available
        """
        count = 0
        for row in range(self.rows):
            for seat in self.plane[row]:
                if seat == 0:
                    count += 1
        return count

    @property
    def vacant_premium_seats(self):
        """
        Returns how many premium seats are available
        """
        count = 0
        for row in range(self.premium_rows):
            for seat in self.plane[row]:
                if seat == 0:
                    count += 1
        return count

    @property
    def vacant_economy_seats(self):
        """
        Returns how many economy seats are available
        """
        count = 0
        for row in range(self.premium_rows, self.rows - self.premium_rows):
            for seat in self.plane[row]:
                if seat == 0:
                    count += 1
        return count

    def get_random_seat(self, row_end, row_start=0):
        """
        Returns a tuple representing a random vacant seat (row, column)
        """
        assert self.vacant_seats > 0
        # Select random row
        row = -1
        while row < 0:
            i = random.randint(row_start, row_end - 1)
            if self.plane[i].count(0):
                row = i
        # Select random seat
        seat = -1
        while seat < 0:
            i = random.randint(0, self.cols - 1)
            if not self.plane[row][i]:
                seat = i
        return (row, seat)

    def get_random_premium_seat(self):
        """
        Returns a tuple representing a random vacant premium seat (row, column)
        """
        assert self.vacant_premium_seats > 0
        return self.get_random_seat(row_end=self.premium_rows)

    def get_random_economy_seat(self):
        """
        Returns a tuple representing a random vacant economy seat (row, column)
        """
        assert self.vacant_economy_seats > 0
        return self.get_random_seat(row_start=self.premium_rows, row_end=self.rows)

    def assign_seat(self, row, column, family):
        """
        Sets the matrix cell representing the seat to the family number
        This seat will be regarded as occupied
        """
        assert self.plane[row][column] == 0
        self.plane[row][column] = family
