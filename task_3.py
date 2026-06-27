class PointsForPlace:
    @staticmethod
    def get_points_for_place(place: int) -> int: # Метод get_points_for_place не испоьзует состояния объекта (нет обращения к self). Делаем статическим с помощь декоратора @staticmethod.
        points = 0                               # Переменная points должна быть локальной, так как находится внутри методов. Если сделать её глобальной, при повторных вызовах объектов данные будут искажаться.
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
        else:
            points = 100 - place
        return points

class PointsForMeters:
    @staticmethod
    def get_points_for_meters(meters: int) -> float:  # Метод get_points_for_meters не испоьзует состояния объекта (нет обращения к self). Делаем статическим с помощь декоратора @staticmethod.
        points = 0
        if meters < 0:
            print('Количество метров не может быть отрицательным')
        else:
            points = meters * 0.5
        return points

class TotalPoints(PointsForPlace, PointsForMeters):      # Реализован класс TotalPoints. Наследуется сразу от двух классов — PointsForPlace и PointsForMeters и реализует все их методы.
    @staticmethod
    def get_points_for_points(meters: int, place: int) -> float:   # Реализован метод get_total_points().
        place_points = TotalPoints.get_points_for_place(place)
        meters_points = TotalPoints.get_points_for_meters(meters)
        total = place_points + meters_points                      # Переменная total суммирует значения методов get_points_for_place() и get_points_for_meters()
        return total


points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_points_for_points(100, 10))
