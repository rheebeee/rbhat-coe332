#!/usr/bin/env python3
import json
import unittest
import random
import sys
import petname
from read_animals import breed

class TestReadAnimals(unittest.TestCase):

    def test_breed(self):
        dict_one = {
            'head': 'snake',
            'body': 'sheep-fish',
            'arms': 3,
            'legs': 6,
            'tail': 9
        }
        dict_two = {
            'head': 'snake',
            'body': 'sheep-fish',
            'arms': 3,
            'legs': 6,
            'tail': 9
        }
        self.assertRaises(TypeError, breed, 'Parent one', 'Parent two')
        self.assertEqual(breed(dict_one, dict_two), dict_one)
        self.assertDictEqual(breed(dict_one, dict_two), dict_one)
        self.assertRaises(TypeError, breed, 10, 5)
        self.assertDictEqual(breed(dict_one, dict_two), dict_two)
        self.assertRaises(TypeError, breed, 'head', 2)

if __name__ == '__main__':
    unittest.main()
