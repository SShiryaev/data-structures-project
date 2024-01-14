"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack


class TestPush(unittest.TestCase):
    """Тестирование метода push класса Stack"""
    def test_push(self):
        stack = Stack()
        stack.push('node1')
        stack.push('node2')
        stack.push('node3')
        self.assertEqual(stack.top.data, 'node3')
        self.assertEqual(stack.top.next_node.data, 'node2')
        self.assertEqual(stack.top.next_node.next_node.data, 'node1')
        self.assertIsNone(stack.top.next_node.next_node.next_node)
        with self.assertRaises(AttributeError):
            error = stack.top.next_node.next_node.next_node.data


class TestPopThirst(unittest.TestCase):
    """Тестирование метода pop класса Stack"""
    def test_pop_thirst(self):
        stack = Stack()
        stack.push('node1')
        data = stack.pop()
        self.assertIsNone(stack.top)
        self.assertEqual(data, 'node1')


class TestPopSecond(unittest.TestCase):
    """Тестирование метода pop класса Stack"""
    def test_pop_second(self):
        stack = Stack()
        stack.push('node1')
        stack.push('node2')
        data = stack.pop()
        self.assertEqual(stack.top.data, 'node1')
        self.assertEqual(data, 'node2')


class TestStrMethod(unittest.TestCase):
    """Тестирование магического метода __str__ класса Stack"""
    def test__str__(self):
        stack = Stack()
        self.assertEqual(stack.top, None)
