"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack


class TestPush(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push('test1')
        stack.push('test2')
        stack.push('test3')
        self.assertEqual(stack.top.data, 'test3')
        self.assertEqual(stack.top.next_node.data, 'test2')
        self.assertEqual(stack.top.next_node.next_node.data, 'test1')
        self.assertEqual(stack.top.next_node.next_node.next_node, None)
        with self.assertRaises(AttributeError):
            self.assertEqual(stack.top.next_node.next_node.next_node.data, AttributeError)
