class Hall:
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []

    def allocate_seats(self):
        seats = [["Free" for _ in range(self.cols)] for _ in range(self.rows)]
        return seats

    def entry_show(self, show_id, movie_name, show_time):
        show_info = (show_id, movie_name, show_time)

        self.show_list.append(show_info)
        seats = self.allocate_seats()
        self.seats[show_id] = seats

hall1 = Hall(10, 20, 1)

hall1.entry_show("S1", "Movie A", "2:00 PM")

print("Show List:")
for show in hall1.show_list:
    print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

print("\nSeats Allocation for Show 'S1':")
for row in hall1.seats["S1"]:
    print(row)
