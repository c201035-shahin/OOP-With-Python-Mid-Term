## NOT COMPLETED, NO OUTPUT

class InvalidShowError(Exception):
    pass

class InvalidSeatError(Exception):
    pass

class AlreadyBookedError(Exception):
    pass

class Hall:
    def __init__(self, rows, cols, hall_no):
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._seats = {}
        self._show_list = []

    def _allocate_seats(self):
        seats = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        return seats

    def _entry_show(self, show_id, movie_name, show_time):
        show_info = (show_id, movie_name, show_time)
        self._show_list.append(show_info)

        self._seats[show_id] = self._allocate_seats()

    def book_seats(self, show_id, seat_list):
        if show_id in self._seats:
            seats_available = self._seats[show_id]
            for row, col in seat_list:
                if not (0 <= row < self._rows and 0 <= col < self._cols):
                    raise InvalidSeatError("Invalid seat coordinates.")
                if seats_available[row][col] == 0:
                    seats_available[row][col] = 1
                    print(f"Seat ({row}, {col}) has been booked for show {show_id}.")
                else:
                    raise AlreadyBookedError(f"Seat ({row}, {col}) is already booked for show {show_id}.")
        else:
            raise InvalidShowError(f"Show {show_id} not found.")

    def view_show_list(self):
        print("List of Shows:")
        for show in self._show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id in self._seats:
            seats_available = self._seats[show_id]
            print(f"Available Seats for Show {show_id}:")
            for row in range(self._rows):
                for col in range(self._cols):
                    if seats_available[row][col] == 0:
                        print(f"Row: {row}, Col: {col}")
        else:
            raise InvalidShowError(f"Show {show_id} not found.")

class TicketCounter:
    def __init__(self):
        self._hall_list = []

    def add_hall(self, hall):
        self._hall_list.append(hall)

    def view_all_shows(self):
        print("All Shows:")
        for hall in self._hall_list:
            hall.view_show_list()

    def view_available_seats(self, show_id):
        for hall in self._hall_list:
            try:
                hall.view_available_seats(show_id)
            except InvalidShowError as e:
                print(e)

    def book_tickets(self, show_id, seat_list):
        for hall in self._hall_list:
            try:
                hall.book_seats(show_id, seat_list)
            except (InvalidShowError, InvalidSeatError, AlreadyBookedError) as e:
                print(e)
