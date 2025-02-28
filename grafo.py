import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PySide6 import QtCore
from ui.ggx import Ui_TASKMANAGERAPP
from src.task_manager import TaskManager
from datetime import datetime
from src.task import Task
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TASKMANAGERAPP()
        self.ui.setupUi(self)
        self.task_manager = TaskManager()
        self.load_tasks()
        self.ui.addtask.clicked.connect(self.add_task)
        self.ui.deletetask.clicked.connect(self.delete_task)
        self.ui.updatetask.clicked.connect(self.update_task)
    def load_tasks(self):
        self.ui.taskTable.setRowCount(0)
        tasks = self.task_manager.get_all_tasks_dict()

        for task in tasks.values():
            row_position = self.ui.taskTable.rowCount()
            self.ui.taskTable.insertRow(row_position)
            self.ui.taskTable.setItem(row_position, 0, QTableWidgetItem(str(task.id)))
            self.ui.taskTable.setItem(row_position, 1, QTableWidgetItem(task.title))
            self.ui.taskTable.setItem(row_position, 2, QTableWidgetItem(task.description))
            self.ui.taskTable.setItem(row_position, 3, QTableWidgetItem(task.status))
            self.ui.taskTable.setItem(row_position, 4, QTableWidgetItem(task.deadline))
            self.ui.taskTable.setItem(row_position, 5, QTableWidgetItem(task.priority))
            self.ui.taskTable.setItem(row_position, 6, QTableWidgetItem(task.category))
    def add_task(self):
        title = self.ui.nametitle.text()
        description = self.ui.nameopisanie.toPlainText()
        deadline_date = self.ui.calendarik.selectedDate().toString("yyyy-MM-dd")
        deadline_time = self.ui.TimeEdit.time().toString("HH:mm")
        deadline = f"{deadline_date} {deadline_time}"
        priority = self.ui.prioritet.text()
        category = self.ui.categoria.text()
        if title:
            new_task = Task(
                task_id=None,
                title=title,
                description=description,
                createtime=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                status='не выполнено',
                deadline=deadline,
                priority=priority,
                category=category
            )

            saved_task = self.task_manager.create_task(new_task.title, new_task.description, new_task.deadline,
                                                       new_task.priority, new_task.category)
            row_position = self.ui.taskTable.rowCount()
            self.ui.taskTable.insertRow(row_position)

            task_data = [
                str(saved_task.id),
                saved_task.title,
                saved_task.description,
                saved_task.status,
                saved_task.deadline,
                saved_task.priority,
                saved_task.category
            ]
            for column, value in enumerate(task_data):
                self.ui.taskTable.setItem(row_position, column, QTableWidgetItem(value))
            self.clear_input_fields()
        else:
            QMessageBox.warning(self, "Ошибка", "Введите название задачи.")

    def delete_task(self):
        selected_row = self.ui.taskTable.currentRow()
        if selected_row >= 0:
            task_id = int(self.ui.taskTable.item(selected_row, 0).text())
            self.task_manager.delete_task(task_id)
            self.load_tasks()
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите задачу для удаления.")

    def update_task(self):
        selected_row = self.ui.taskTable.currentRow()
        if selected_row >= 0:
            task_id = int(self.ui.taskTable.item(selected_row, 0).text())
            title = self.ui.nametitle.text()
            description = self.ui.nameopisanie.toPlainText()
            deadline_date = self.ui.calendarik.selectedDate().toString("yyyy-MM-dd")
            deadline_time = self.ui.TimeEdit.time().toString("HH:mm")
            deadline = f"{deadline_date} {deadline_time}"
            priority = self.ui.prioritet.text()
            category = self.ui.categoria.text()

            self.task_manager.update_task(task_id, title, description, status=None, deadline=deadline,
                                          priority=priority, category=category)
            self.load_tasks()
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите задачу для обновления.")

    def clear_input_fields(self):
        self.ui.nametitle.clear()
        self.ui.nameopisanie.clear()
        self.ui.prioritet.clear()
        self.ui.categoria.clear()
        self.ui.calendarik.setSelectedDate(QtCore.QDate.currentDate())
        self.ui.TimeEdit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())