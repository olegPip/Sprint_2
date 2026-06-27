class Movies:
    def __init__(self):
        # Инициализируем пустой список
        self.movies = []

    def add_movie(self, movie):
        # Добавляем фильм в конец списка
        self.movies.append(movie)


class Comedy(Movies):
    def add_movie(self, movie):
        # Вызываем родительский метод для добавления фильма
        super().add_movie(movie)
        # Возвращаем строку в нужном формате
        return f"Комедии: {self.movies}"

class Drama(Movies):
    def add_movie(self, movie):
        # Вызываем родительский метод для добавления фильма
        super().add_movie(movie)
        # Возвращаем строку в нужном формате
        return f"Драмы: {self.movies}"


# Создаем объекты классов
comedy_handler = Comedy()
drama_handler = Drama()

# Вызываем методы и выводим результат на экран
print(comedy_handler.add_movie('Большой куш'))
print(drama_handler.add_movie('Оружейный барон'))