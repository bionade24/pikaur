""" This file is licensed under GPLv3, see https://www.gnu.org/licenses/ """
# pylint: disable=invalid-name,disallowed-name

from typing import Any

from pikaur_test.helpers import PikaurTestCase
from pikaur.core import ComparableType


class ClassA(ComparableType):
    __ignore_in_eq__ = ('bar', )
    foo: Any
    bar: Any


class ClassB(ComparableType):
    pass


class ComparableTypeTest(PikaurTestCase):

    def test_eq(self):
        a1 = ClassA()
        a1.foo = 1
        a2 = ClassA()
        a2.foo = 1
        self.assertEqual(a1, a2)

    def test_neq(self):
        a1 = ClassA()
        a1.foo = 1
        a2 = ClassA()
        a2.foo = 2
        self.assertNotEqual(a1, a2)

    def test_ignore_1(self):
        a1 = ClassA()
        a1.foo = 1
        a2 = ClassA()
        a2.foo = 1
        self.assertEqual(a1, a2)
        a1.bar = 2
        a2.bar = 3
        self.assertEqual(a1, a2)

    def test_different_types(self):
        a1 = ClassA()
        b1 = ClassB()
        with self.assertRaises(TypeError):
            _ = a1 == b1

    def test_recursion_1(self):
        a1 = ClassA()
        a1.foo = a1
        a2 = ClassA()
        a2.foo = a2
        self.assertNotEqual(a1, a2)

    def test_recursion_2(self):
        a1 = ClassA()
        a1.foo = a1
        self.assertEqual(a1, a1)

    def test_recursion_3(self):
        a1 = ClassA()
        a1.foo = a1
        a2 = ClassA()
        a2.foo = a1
        self.assertEqual(a1, a2)
