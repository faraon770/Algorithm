class Node:
    """
    Задача 1: Класс узла (Node)
    Содержит данные и ссылку на следующий узел.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    Задача 2: Класс связного списка (LinkedList)
    """

    def __init__(self):
        self.head = None

    def add_to_front(self, data):
        """
        Задача 3: Добавление элемента в начало списка.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        """
        Задача 4: Добавление элемента в конец списка.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        """
        Задача 5: Вывод всех элементов списка.
        """
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" → ".join(elements) if elements else "Список пуст")

    def search(self, value):
        """
        Задача 6: Поиск элемента в списке.
        Возвращает True, если элемент найден, иначе False.
        """
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def delete_first(self):
        """
        Задача 7: Удаление первого элемента списка.
        """
        if self.head:
            self.head = self.head.next
        else:
            print("Ошибка: Список пуст, нечего удалять.")

    def count_elements(self):
        """
        Задача 8: Подсчёт количества элементов.
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def reverse(self):
        """
        Задача 10: Разворот связного списка.
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


# -

if __name__ == "__main__":
    print("--- Выполнение Лабораторной работы №9 ---")

    # Задача 1 & 2: Создание списка и узлов
    llist = LinkedList()

    # Задача 9: Считывание 5 чисел от пользователя
    print("\nЗадача 9: Введите 5 чисел для добавления в список:")
    for i in range(5):
        try:
            num = int(input(f"Введите число {i + 1}: "))
            llist.append(num)
        except ValueError:
            print("Ошибка ввода. Будет добавлено значение 0.")
            llist.append(0)

    print("\nВаш список:")
    llist.display()

    # Задача 3: Добавление в начало
    print("\nДобавляем 100 в начало:")
    llist.add_to_front(100)
    llist.display()

    #  Задача 8: Подсчёт
    print(f"Количество элементов: {llist.count_elements()}")

    #  Задача 6: Поиск
    search_val = 100
    print(f"Поиск элемента {search_val}: {llist.search(search_val)}")

    # Демонстрация Задача 7: Удаление первого
    print("\nУдаление первого элемента:")
    llist.delete_first()
    llist.display()

    #  Задача 10: Разворот
    print("\nРазворот списка:")
    llist.reverse()
    llist.display()