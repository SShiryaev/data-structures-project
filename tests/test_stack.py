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
