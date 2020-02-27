import unittest
from sww_triangle import*


class BuggyTriangleTest(unittest.TestCase):

    def test_init(self):
        t = Triangle(4, 5, 6)
        self.assertEqual(t.a, 4)
        self.assertEqual(t.b, 5)
        self.assertEqual(t.c, 6)

    def test_triangleEquilateral(self):
        """To test equilateral function"""

        t = Triangle(2.5,2.5,2.5)
        self.assertTrue(t.equilateral_triangle())
        self.assertTrue(Triangle(4.5, 4.5, 4.5).equilateral_triangle())
        self.assertFalse(Triangle(0, 0, 0).equilateral_triangle())
        self.assertFalse(Triangle(2.3, 1.2, 1.2).equilateral_triangle())

    def test_triangleIsosceles(self):
        """To test isosceles function"""
        t = Triangle(4, 4, 6)
        self.assertTrue(t.isosceles_triangle())
        self.assertTrue(Triangle(7, 7, 9).isosceles_triangle())
        self.assertFalse(Triangle(4, 4, 17).isosceles_triangle())

    def test_triangleRight(self):
        """To test right function"""
        t = Triangle(5, 12, 13)
        self.assertTrue(t.right_triangle())
        self.assertTrue(Triangle(3, 4, 5).right_triangle())
        self.assertFalse(Triangle(1, 2, 5).right_triangle())

    def test_triangleScalene(self):
        """To test scalene function"""
        t = Triangle(7, 8, 9)
        self.assertTrue(t.scalene_triangle())
        self.assertTrue(Triangle(4, 5, 6).scalene_triangle())
        self.assertFalse(Triangle(1, 2, 3).scalene_triangle())


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)