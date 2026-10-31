class User():
    """Класс пользователя"""
    def __init__(self) -> None:
        self.__pass = "123321"
    
    # @property
    # def level(self):
    #     """Возвращает уровень доступа пользователя"""
    #     self.__level = "user"
    #     return self.__level
    
    # @level.setter
    # def level(self):
    #     """Меняет уровень доступа на админа при прохождении проверки"""
    #     if self.tryPassword():
    #         self.__level = "admin"
    #         print("Получен уровень доступа: админ")
    #     else:
    #         print("У вас нет прав для получения высокого уровня доступа")

    # def tryPassword(self) -> None:
    #     for i in range(3):
    #         user_input = input("Введите пароль: ")
    #         if user_input == self.__pass:
    #             print("Вы авторизованы")
    #             return True
    #         else:
    #             print(f"Неверный пароль. Осталось попыток: {3 - i}")
    #     return False

    def ask(self, str: str = "") -> str:
        user_inp = input(str)
        return user_inp