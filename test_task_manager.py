import pytest
from src.task_manager import TaskManager
from src.task import Task
from src.DB import create_connection
#############################################
'''
ПОСЛЕ ИСПОЛЬЗОВАНИЯ ТЕСТА ВСЯ БД БУДЕТ ОЧИЩЕНА
'''
#############################################
@pytest.fixture(scope="function")

def setup_database():
    conn = create_connection()
    conn.execute("DELETE FROM taskdb")  # ОЧИСТКА ТАБЛИЦ БД
    conn.commit()
    yield conn
    conn.close()

@pytest.fixture
def task_manager():

    return TaskManager()
def test_create_task(task_manager, setup_database):

    task = task_manager.create_task("Test Task", "This is a test task", "2025-12-31 12:00:00", "низкий", "работа")

    assert task.id is not None  # Проверка  что ID задачи не None

    assert task.title == "Test Task"  # Проверка  что название задачи корректно

def test_update_task(task_manager, setup_database):

    task = task_manager.create_task("Task to Update", "This task will be updated", "2025-12-31 12:00:00", "средний", "учеба")

    task_manager.update_task(task.id, title="Updated Task", description="Updated description")

    updated_task = task_manager.get_task(task.id)

    assert updated_task['title'] == "Updated Task"  # проверка что название обновлено

    assert updated_task['description'] == "Updated description"  # ghjdthrf, что описание обновлено


def test_delete_task(task_manager, setup_database):

    task = task_manager.create_task("Task to Delete", "This task will be deleted", "2025-12-31 12:00:00", "высокий", "личное")

    task_manager.delete_task(task.id)

    assert task_manager.get_task(task.id) is None  # Проверка что задача удалена


def test_load_tasks(task_manager, setup_database):

    task_manager.create_task("Task 1", "Description 1", "2025-12-31 12:00:00", "низкий", "работа")

    task_manager.create_task("Task 2", "Description 2", "2025-12-31 12:00:00", "средний", "учеба")

    tasks = task_manager.get_all_tasks()
    assert len(tasks) == 2  # Проверка что загружено 2 задачи