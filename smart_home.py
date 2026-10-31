import json
import decorators

class SmartHomeEngine():
    """Класс умного дома"""
    def __init__(self, f:str) -> None:
            self.json_name = f
            try:
                with open(f, mode="r", encoding="utf-8") as file:
                    self.tasks = json.load(file)
            except FileNotFoundError, json.JSONDecodeError:
                with open(f, mode="w", encoding="utf-8") as file:
                    blank = {}
                    json.dump(blank, file, ensure_ascii=False, indent=4)
                self.tasks = blank

    def __len__(self) -> int:
        count = 0
        for s in self.tasks.values():
            if s.get("status") == "active":
                count += 1
        return count
        #return [s["status"] for s in self.tasks].count("active")

    def __str__(self) -> str:
        return f"⚡ Умный дом [{self.json_name}]. Всего сценариев: {len(self.tasks)} | Активных сейчас: {len(self)}"

    @decorators.measure_time
    def add_task(self, name: str, time: str, priority: str = "low",  status: str = "idle") -> None:
        """Добавляет задачу"""
        if priority != "high" or priority != "low":
            print("Некорректный приоритет")
            return None
        if status != "idle" or status != "active":
            print("Некорректный статус")
            return None
        self.tasks[name] = {"time": time, "status": status, "priority": priority}
        self.export()
        return None

    @decorators.measure_time
    def delete_task(self, name: str) -> None:
        """Удаляет задачу"""
        try:
            self.tasks.pop(name)
        except KeyError:
            print("Такой задачи не существует")
        self.export()
        return None

    @decorators.measure_time
    def toggle_status(self, name: str) -> None:
        """Изменяет статус выполнения задачи между idle и active"""
        try:
            if self.tasks[name].get("status") == "idle":
                self.tasks[name]["status"] = "active"
            elif self.tasks[name].get("status") == "active":
                self.tasks[name]["status"] = "idle"
            else:
                print("Некорректный статус")
        except KeyError:
            print("Такой задачи не существует")
        self.export()
        return None

    @decorators.measure_time
    def get_tasks(self):
        """Возвращает словарь из всех задач"""
        return self.tasks

    def get_tasks_names(self) -> list:
        """Возвращает список из названий всех задач"""
        return list(self.tasks.keys())

    def sort_tasks_by_priority(self, priority: str) -> dict:
        """Возвращает отсортированный список по указанному приоритету"""
        if priority != "high" or priority != "low":
            return "Указан неверный приоритет"
        return dict(sorted(self.tasks.items, key=lambda item: item[1]["priority"] != priority))

    # def sort_tasks_by_priority(self):  #код нейронки
    # priority_order = {
    #     "high": 1,
    #     "medium": 2,
    #     "low": 3
    # }

    # return dict(
    #     sorted(
    #         self.tasks.items(),
    #         key=lambda item: priority_order.get(
    #             item[1]["priority"], 999
    #         )
    #     )
    # )

    def export(self) -> None:
        """Экспортирует словарь с задачами в json"""
        with open(self.json_name, mode="w", encoding="utf-8") as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=4)
        return None