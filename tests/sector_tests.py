import unittest

from wheelofjeopardy.sectors.sector import Sector

# class SectorTestCase(unittest.TestCase):
#     def setUp(self):
#         self.sector = Sector()

class TestSectorName(unittest.TestCase):
    def test_name_attribute(self):
        self.sector = Sector("base class")
        self.assertEqual(self.sector.name, "base class")

if __name__ == '__main__':
    unittest.main()
