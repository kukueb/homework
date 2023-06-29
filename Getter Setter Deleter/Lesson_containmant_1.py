class Year:
    def __init__(self, days, season):
        self.__days = days
        self.__season = season

    @property
    def get_days(self):
        return self.__days
    @property
    def get_season(self):
       return self.__season
    @get_days.setter
    def days(self, days):
        if days == 365 or days == 360:
            self.__days = days
        else:
            raise Exception('Неккоректное значение')
    @get_season.setter
    def season(self, season):
        self.__season = season

year = Year(365, 'winter')
print(year.get_days)
year.set_season = 'summer'
print(year.get_season)