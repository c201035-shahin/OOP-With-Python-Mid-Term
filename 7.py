class Hall:
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []

    def allocate_seats(self):
        seats = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        return seats

    def entry_show(self, show_id, movie_name, show_time):
        show_info = (show_id, movie_name, show_time)
        self.show_list.append(show_info)

        self.seats[show_id] = self.allocate_seats()

    def book_seats(self, show_id, seat_list):
        if show_id in self.seats:
            seats_available = self.seats[show_id]
            for row, col in seat_list:
                if 0 <= row < self.rows and 0 <= col < self.cols:
                    if seats_available[row][col] == 0:
                        seats_available[row][col] = 1
                        print(f"Seat ({row}, {col}) has been booked for show {show_id}.")
                    else:
                        print(f"Seat ({row}, {col}) is already booked for show {show_id}.")
                else:
                    print(f"Invalid seat ({row}, {col}).")
        else:
            print(f"Show {show_id} not found.")

    def view_show_list(self):
        print("List of Shows:")
        for show in self.show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id in self.seats:
            seats_available = self.seats[show_id]
            print(f"Available Seats for Show {show_id}:")
            for row in range(self.rows):
                for col in range(self.cols):
                    if seats_available[row][col] == 0:
                        print(f"Row: {row}, Col: {col}")
        else:
            print(f"Show {show_id} not found.")

class TicketCounter:
    def __init__(self):
        self.hall_list = []

    def add_hall(self, hall):
        self.hall_list.append(hall)

    def view_all_shows(self):
        print("All Shows:")
        for hall in self.hall_list:
            hall.view_show_list()

    def view_available_seats(self, show_id):
        for hall in self.hall_list:
            hall.view_available_seats(show_id)

    def book_tickets(self, show_id, seat_list):
        for hall in self.hall_list:
            hall.book_seats(show_id, seat_list)

hall1 = Hall(10, 20, 1)
hall2 = Hall(8, 15, 2)

counter = TicketCounter()
counter.add_hall(hall1)
counter.add_hall(hall2)

hall1.entry_show("S1", "Movie A", "2:00 PM")
hall2.entry_show("S2", "Movie B", "4:30 PM")

counter.view_all_shows()
counter.view_available_seats("S1")

counter.book_tickets("S1", [(0, 0), (1, 1), (2, 2)])
