import unittest

from wheelofjeopardy.wheel import Wheel
from wheelofjeopardy.sectors.sector import Sector
from wheelofjeopardy.category import Category

class WheelTestCase(unittest.TestCase):
    def setUp(self):
        self.wheel =  Wheel()

class TestWheelInitialization(WheelTestCase):
    def test_name_attribute(self):
        self.assertEqual(self.wheel.description,
                         'Wheel from the game Wheel of Jeopardy!')
        self.assertEqual(str(self.wheel),
                         'Wheel from the game Wheel of Jeopardy!')

    def test_sector_list_size(self):
        self.assertEqual(len(self.wheel._sectors), 12)

    def test_sector_list_type(self):
        for aSector in self.wheel._sectors:
            self.assertTrue(isinstance(aSector, Sector))

class TestGetSector(WheelTestCase):
    def test_get_random_sector(self):
        self.assertTrue(isinstance(self.wheel.get_random_sector(), Sector))

if __name__ == '__main__':
    unittest.main()
