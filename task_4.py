class EmployeeSalary:
    hourly_payment = 400                                 # Установили почасовой уровень оплаты


    def __init__(self, name, hours, rest_days, email):    # Инициализируем конструктор с атрибутами name, hours, rest_days, email.
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email


    @classmethod
    def get_hours(cls, name, hours, rest_days, email):   # Добавляем метод класса get_hours()
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days, email):   # Добавляем метод класса get_email()
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_payment):           # Добавляем метод класса set_hourly_payment()
        cls.hourly_payment = new_payment

    def salary(self):
        return self.hours * self.hourly_payment         # Добавляем метод расчёта заработной платы salary()



