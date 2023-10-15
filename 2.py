class Hall:
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []

class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        if isinstance(hall, Hall):
            cls.hall_list.append(hall)
            print(f"Hall {hall.hall_no} has been added to the hall_list.")
        else:
            print("Invalid hall object. Please provide an instance of the Hall class.")

    def __init__(self, rows, cols, hall_no):
        hall = Hall(rows, cols, hall_no)
        self.entry_hall(hall)

cinema1 = Star_Cinema(10, 20, 1)
cinema2 = Star_Cinema(8, 15, 2)

print("List of Halls:")
for hall in Star_Cinema.hall_list:
    print(f"Hall {hall.hall_no} - Rows: {hall.rows}, Columns: {hall.cols}")
