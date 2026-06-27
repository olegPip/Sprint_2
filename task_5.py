class Results:                                         # Написали класс Results.
    def __init__(self, victories, draws, losses):      # Проинициализировали атрибуты victories, draws, losses.
        self.victories = victories
        self.draws = draws
        self.losses = losses

class Football(Results):                              # Написали класс Football который наследуется от класса Results.
    def number_of_wins(self):                         # Написали метод number_of_wins() который возвращает "Футбольных побед: 1".
        return f"Футбольных побед: {self.victories}"
    
    def number_of_draws(self):
        return f"Футбольных ничьих: {self.draws}"      # Написали метод number_of_draws() который возвращает "Футбольных ничьих: 1".
    
    def number_of_losses(self):
        return f"Футбольных поражений: {self.losses}"   # Написали метод number_of_losses() который возвращает "Футбольных ничьих: 1".
    
    def total_points(self):                            # Написали метод total_points() который возвращает "Общее количество очков: 5".
        points = 3 * self.victories + self.draws       # Рассчитали количество очков
        return f"Общее количество очков: {points}"
    

class Hockey(Results):
    def number_of_wins(self):
        return f"Хоккейных побед: {self.victories}"

    def number_of_draws(self):
        return f"Хоккейных ничьих: {self.draws}"    
    
    def number_of_losses(self):
        return f"Хоккейных поражений: {self.losses}"
    
    def total_points(self):
        points = 2 * self.victories + self.draws
        return f"Общее количество очков: {points}"
    
# Создали объект football_team и hockey_team классов Football, Hockey с параметрами (2, 2, 2)
football_team = Football(2, 2, 2)
hockey_tem = Hockey(2, 2, 2)

# Вызвали все методы для объектов football_team и hockey_team цыклом for.
for team in (football_team, hockey_tem):
    print(team.number_of_wins())
    print(team.number_of_draws())
    print(team.number_of_losses())
    print(team.total_points())
















