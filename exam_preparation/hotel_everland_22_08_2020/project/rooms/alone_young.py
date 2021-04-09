from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    room_members = 1
    room_cost = 10
    appliance_types = (TV,)

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, self.room_members)
        self.calculate_expenses(self.appliances)
