"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack


class TestPush(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push('node1')
        stack.push('node2')
        stack.push('node3')
        self.assertEqual(stack.top.data, 'node3')
        self.assertEqual(stack.top.next_node.data, 'node2')
        self.assertEqual(stack.top.next_node.next_node.data, 'node1')
        self.assertEqual(stack.top.next_node.next_node.next_node, None)
        with self.assertRaises(AttributeError):
            self.assertEqual(stack.top.next_node.next_node.next_node.data, AttributeError)


class TestPopThirst(unittest.TestCase):
    def test_pop_thirst(self):
        stack = Stack()
        stack.push('node1')
        data = stack.pop()
        self.assertIsNone(stack.top)
        self.assertEqual(data, 'node1')


class TestPopSecond(unittest.TestCase):
    def test_pop_second(self):
        stack = Stack()
        stack.push('node1')
        stack.push('node2')
        data = stack.pop()
        self.assertEqual(stack.top.data, 'node1')
        self.assertEqual(data, 'node2')
