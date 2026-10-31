from smart_home import SmartHomeEngine
from authorise import User

smart_home = SmartHomeEngine("smarthome_tasks.json")
user = User()

while True:
    print("Вас приветствует умный дом")
    print("""Список доступных комманд:
    1. Состояние системы
    2. Список всех задач
    3. Добавить новую задачу
    4. Запустить/остановить задачу
    5. Удалить задачу
    0. Выход""")
    ask = user.ask("Что хотите сделать: ")
    if ask == "1":
        print(smart_home)
    elif ask == "2":
        print(smart_home.get_tasks())
    elif ask == "3":
        task_name = input("Введите название задачи: ")
        task_time = input("Введите время начала выполнения задачи: ")
        task_priority = input("Введите приоритет задачи: ")
        task_status = input("Введите статус выполнения задачи (Enter -> IDLE): ")
        if task_status == "":
            task_status = "idle"
        smart_home.add_task(task_name, task_time, task_priority, task_status)
    elif ask == "4":
        task_inp = input("Введите название задачи, статус которой хотите изменить: ")
        smart_home.toggle_status(task_inp)
    elif ask == "5":
        task_inp = input("Введите название задачи, статус которой хотите изменить: ")
        smart_home.delete_task(task_inp)
    elif ask == "0":
        break
    else:
        print("Такой задачи не предусмотрено")