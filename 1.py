class Hall:
    def __init__(self, hall_name, capacity):
        self.hall_name = hall_name
        self.capacity = capacity

class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        if isinstance(hall, Hall):
            cls.hall_list.append(hall)
            print(f"{hall.hall_name} has been added to the hall_list.")
        else:
            print("Invalid hall object. Please provide an instance of the Hall class.")

hall1 = Hall("Thera A", 100)
hall2 = Hall("Thera B", 150)

Star_Cinema.entry_hall(hall1)
Star_Cinema.entry_hall(hall2)

print("List of Halls:")
for hall in Star_Cinema.hall_list:
    print(f"{hall.hall_name} - Capacity: {hall.capacity}")
