from smart_home import SmartHomeEngine
from authorise import User

smart_home = SmartHomeEngine("smarthome_tasks.json")
user = User()

while True:
    print("\nВас приветствует умный дом")
    print("""\nСписок доступных комманд:
    1. Состояние системы
    2. Список всех задач
    3. Сортированный список всех задач
    4. Добавить новую задачу
    5. Запустить/остановить задачу
    6. Удалить задачу
    0. Выход""")
    ask = user.ask("\nЧто хотите сделать: ")
    if ask == "1":
        print(smart_home)
    elif ask == "2":
        print(smart_home.get_tasks())
    elif ask == "3":
        task_priority = input("Введите приоритетный приоритет (строго high или low)")
        print(smart_home.sort_tasks_by_priority(task_priority))
    elif ask == "4":
        task_name = input("Введите название задачи: ")
        task_time = input("Введите время начала выполнения задачи: ")
        task_priority = input("Введите приоритет задачи (строго high или low) (Enter -> low): ")
        task_status = input("Введите статус выполнения задачи (строго idle или active) (Enter -> idle): ")
        if task_priority == "":
            task_status = "low"
        if task_status == "":
            task_status = "idle"
        smart_home.add_task(task_name, task_time, task_priority, task_status)
    elif ask == "5":
        print(f"Список задач: {smart_home.get_tasks_names()}")
        task_inp = input("Введите название задачи, статус которой хотите изменить: ")
        smart_home.toggle_status(task_inp)
    elif ask == "6":
        print(f"Список задач: {smart_home.get_tasks_names()}")
        task_inp = input("Введите название задачи, которую хотите удалить: ")
        smart_home.delete_task(task_inp)
    elif ask == "0":
        break
    else:
        print("Такой задачи не предусмотрено")