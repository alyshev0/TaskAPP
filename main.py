from src.task_manager import TaskManager

task_manager = TaskManager()

console_output = lambda: print("1. Добавить задачу\n2. Показать все задачи\n3. Изменить статус\n4. Удалить задачу\n5. Поиск задач\n6. Поиск задач (категория/приоритет)\n7. Выход")

def search_tasks(search_term):
    results = []
    for task in task_manager.get_all_tasks():
        if (search_term.lower() in task.title.lower() or
            search_term.lower() in task.description.lower() or
            search_term.lower() in task.status.lower() or
            search_term.lower() in task.priority.lower() or
            search_term.lower() in task.category.lower()):
            results.append(task)
    return results

def search_task_cp(search_term):
    results = []
    for task in task_manager.get_all_tasks():
        if (search_term.lower() in task.priority.lower() or
            search_term.lower() in task.category.lower()):
            results.append(task)
    return results

def main():
    while True:
        console_output()
        choice = input("Выберите действие: ")
        if choice == '1':
            title = input("Введите название задачи: ")
            description = input("Введите описание задачи: ")
            deadline = input("Введите срок выполнения (Y-M-D H:M:S): ")
            priority = input("Введите приоритет (низкий, средний, высокий): ")
            category = input("Введите категорию (работа, учеба, личное): ")
            task_manager.create_task(title, description, deadline, priority, category)
            print("Задача успешно добавлена!")
        elif choice == '2':
            tasks = task_manager.get_all_tasks()
            for task in tasks:
                print(f"\nID: {task.id}")
                print(f"Название: {task.title}")
                print(f"Описание: {task.description}")
                print(f"Статус: {task.status}")
                print(f"Дата создания: {task.createtime}")
                print(f"Срок выполнения: {task.deadline}")
                print(f"Приоритет: {task.priority}")
                print(f"Категория: {task.category}")
        elif choice == '3':
            task_id = int(input("Введите ID задачи для обновления: "))
            title = input("Новое название (оставьте пустым, чтобы не менять): ")
            description = input("Новое описание (оставьте пустым, чтобы не менять): ")
            status = input("Новый статус (оставьте пустым, чтобы не менять): ")
            deadline = input("Новый срок выполнения (оставьте пустым, чтобы не менять): ")
            priority = input("Новый приоритет (оставьте пустым, чтобы не менять): ")
            category = input("Новая категория (оставьте пустым, чтобы не менять): ")
            if task_manager.update_task(
                    task_id,
                    title if title else None,
                    description if description else None,
                    status if status else None,
                    deadline if deadline else None,
                    priority if priority else None,
                    category if category else None
            ):
                print("Задача обновлена!")
            else:
                print("Ошибка: задача не найдена")
        elif choice == '4':
            task_id = int(input("Введите ID задачи для удаления: "))
            if task_manager.delete_task(task_id):
                print("Задача удалена!")
            else:
                print("Ошибка: задача не найдена")
        elif choice == '5':
            search_term = input("Введите поисковый запрос: ")
            results = search_tasks(search_term)
            if results:
                print("Найденные задачи:")
                for task in results:
                    print(f"\nID: {task.id}")
                    print(f"Название: {task.title}")
                    print(f"Описание: {task.description}")
                    print(f"Статус: {task.status}")
                    print(f"Дата создания: {task.createtime}")
                    print(f"Срок выполнения: {task.deadline}")
                    print(f"Приоритет: {task.priority}")
                    print(f"Категория: {task.category}")
            else:
                print("Задачи не найдены.")
        elif choice == '6':
            search_term = input("Введите категорию или приоритет для поиска: ")
            results = search_task_cp(search_term)
            if results:
                print("Найденные задачи по категории или приоритету:")
                for task in results:
                    print(f"\nID: {task.id}")
                    print(f"Название: { task.title}")
                    print(f"Описание: {task.description}")
                    print(f"Статус: {task.status}")
                    print(f"Дата создания: {task.createtime}")
                    print(f"Срок выполнения: {task.deadline}")
                    print(f"Приоритет: {task.priority}")
                    print(f"Категория: {task.category}")
            else:
                print("Задачи не найдены.")
        elif choice == '7':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()