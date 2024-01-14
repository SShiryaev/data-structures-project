"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue


class TestInit(unittest.TestCase):
    """Тестируем магический метод __init__ класса Queue"""
    def test__init__(self):
        queue = Queue()
        self.assertEqual(queue.head, None)
        self.assertEqual(queue.tail, None)


class TestStr(unittest.TestCase):
    """Тестируем магический метод __str__ класса Queue"""
    def test__str__(self):
        queue = Queue()
        self.assertEqual(queue.__str__(), '')
        queue.enqueue('test1')
        queue.enqueue('test2')
        queue.enqueue('test3')
        self.assertEqual(queue.__str__(), 'test1\ntest2\ntest3')


class TestEnqueue(unittest.TestCase):
    """Тестируем метод enqueue класса Queue"""
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('test1')
        queue.enqueue('test2')
        queue.enqueue('test3')
        self.assertEqual(queue.head.data, 'test1')
        self.assertEqual(queue.head.next_node.data, 'test2')
        self.assertEqual(queue.tail.data, 'test3')
        self.assertEqual(queue.tail.next_node, None)
