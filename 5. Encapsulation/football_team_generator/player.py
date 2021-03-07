class Player:

    def __init__(self, name, endurance, sprint, dribble, passing, shooting):
        self.__name = name
        self.__endurance = endurance
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    def get_name(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_endurance(self):
        return self.__endurance

    @property
    def endurance(self):
        return self.__endurance

    def set_endurance(self, endurance):
        self.__endurance = endurance

    def get_sprint(self):
        return self.__sprint

    @property
    def sprint(self):
        return self.__sprint

    def set_sprint(self, sprint):
        self.__sprint = sprint

    def get_dribble(self):
        return self.__dribble

    @property
    def dribble(self):
        return self.__dribble

    def set_dribble(self, dribble):
        self.__dribble = dribble

    def get_passing(self):
        return self.__passing

    @property
    def passing(self):
        return self.__passing

    def set_passing(self, passing):
        self.__passing = passing

    def get_shooting(self):
        return self.__shooting

    @property
    def shooting(self):
        return self.__shooting

    def set_shooting(self, shooting):
        self.__shooting = shooting

    def __str__(self):
        result = f"Player: {self.__name}\n"
        atrr_dict = self.__dict__
        del atrr_dict['_Player__name']
        for key, value in atrr_dict.items():
            start = key[9].upper()
            result += f"{start}{key[10:]}: {value}\n"
        return result
