class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data, None)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if not self.head:
            return None
        elif self.head is None:
            self.tail = None
        else:
            node = self.head
            self.head = node.next_node
            return node.data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        if not self.head:
            return ''
        else:
            nodes = []
            node = self.head
            while node:
                nodes.append(node.data)
                node = node.next_node
            return '\n'.join(nodes)
