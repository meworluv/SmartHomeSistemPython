import json
import decorators

class SmartHomeEngine():
    """Класс умного дома"""
    def __init__(self, f:str) -> None:
            self.json_name = f
            try:
                with open(f, mode="r", encoding="utf-8") as file:
                    self.tasks = json.load(file)
            except FileNotFoundError:
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
    def add_task(self, name: str, time: str, priority: str,  status: str = "idle") -> None:
        """Добавляет задачу"""
        self.tasks[name] = {"time": time, "status": status, "priority": priority}
        self.export()
        return None

    @decorators.measure_time
    def delete_task(self, name: str) -> None:
        """Удаляет задачу"""
        self.tasks.pop(name)
        self.export()
        return None

    @decorators.measure_time
    def toggle_status(self, name: str) -> None:
        """Изменяет статус выполнения задачи между idle и active"""
        if self.tasks[name].get("status") == "idle":
            self.tasks[name]["status"] = "active"
        else:
            self.tasks[name]["status"] = "idle"
        self.export()
        return None

    @decorators.measure_time
    def get_tasks(self):
        """Возвращает список всех задач"""
        return self.tasks

    def export(self) -> None:
        """Экспортирует словарь с задачами в json"""
        with open(self.json_name, mode="w", encoding="utf-8") as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=4)
        return None