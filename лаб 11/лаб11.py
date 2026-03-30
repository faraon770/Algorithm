from collections import deque

# --- Задача 1: Создание графа (список смежности) ---
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F']
}

# --- Задача 2: Добавление новой вершины и связей ---
graph['F'] = ['C', 'E'] # Добавляем F и соединяем с C и E
# Также обновим существующие вершины, чтобы связь была двусторонней
graph['C'].append('F')
graph['E'].append('F')

# --- Задача 3: Функция для вывода соседей ---
def get_neighbors(graph, node):
    return graph.get(node, [])

# --- Задача 4: DFS (Рекурсивно) ---
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

# --- Задача 5: DFS (Через стек) ---
def dfs_stack(graph, start_node):
    visited = set()
    stack = [start_node]
    order = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            stack.extend(reversed(graph[node]))
    return order

# --- Задача 6: BFS (Через очередь) ---
def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

# --- Задача 8: Проверка пути ---
def has_path(graph, start, end):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == end: return True
        if node not in visited:
            visited.add(node)
            queue.extend(n for n in graph[node] if n not in visited)
    return False

# --- Задача 9: Достижимые вершины ---
def count_reachable(graph, start_node):
    return len(bfs(graph, start_node))

# --- Задача 10: Кратчайший путь (BFS) ---
def find_shortest_path(graph, start, end):
    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end: return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None

# --- ВЫВОД РЕЗУЛЬТАТОВ ---

print("--- Результаты Лабораторной работы №11 ---")

print("\nЗадача 1 & 2: Структура графа")
print(graph)

print("\nЗадача 3: Соседи вершины 'B'")
print(f"Соседи: {get_neighbors(graph, 'B')}")

print("\nЗадача 4: DFS (Рекурсивный обход от 'A')")
dfs_recursive(graph, 'A')
print() # перенос строки

print("\nЗадача 5: DFS (Обход через стек от 'A')")
print(dfs_stack(graph, 'A'))

print("\nЗадача 6: BFS (Обход через очередь от 'A')")
print(bfs(graph, 'A'))

print("\nЗадача 7: Порядок посещения (демонстрация)")
start = 'A'
print(f"Старт с '{start}'. Порядок BFS: {bfs(graph, start)}")

print("\nЗадача 8: Существует ли путь между 'A' и 'D'?")
print("Да" if has_path(graph, 'A', 'D') else "Нет")

print("\nЗадача 9: Количество достижимых вершин из 'A'")
print(f"Достижимо: {count_reachable(graph, 'A')}")

print("\nЗадача 10: Кратчайший путь от 'A' до 'F'")
print(f"Путь: {find_shortest_path(graph, 'A', 'F')}")