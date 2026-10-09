tasks = []

def add_task():
    texs = input("Введите задачу: ").strip()
    if text:
        tasks.append(text)
        print("Задача добавлена.")
    else:
        print("Пустая задача не добавлена.")

def main():
    while True:
        print("\n1. Добавить задачу")
        print("2. Выход")
        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            print("До свидания!")
            break
        else:
            print("Неверный пункт меню.")

if __name__ == "__main__":
    main()
