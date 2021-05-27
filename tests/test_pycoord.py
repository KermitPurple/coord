from src import Coord
import unittest, math

class TestCoord(unittest.TestCase):
    def test_r_theta(self):
        c = Coord(10, 0)
        self.assertEqual(c.r, 10)
        self.assertEqual(c.theta, 0)
        c.x = 5
        self.assertEqual(c.r, 5)
        c.theta = math.pi / 2
        self.assertAlmostEqual(c.r, 5)
        self.assertAlmostEqual(c.y, 5)
        c.theta = math.pi / 4
        self.assertAlmostEqual(c.x, 5 * math.cos(math.pi / 4))

    def test_from_tuple(self):
        self.assertEqual(Coord.from_tuple((1, 2)), Coord(1, 2))

    def test_from_polar(self):
        self.assertEqual(Coord.from_polar(3, 0), Coord(3, 0))

    def test_scalar_mul(self):
        self.assertEqual(Coord(4, 5).scal_mul(3), Coord(12, 15))

    def test_dot_prod(self):
        self.assertEqual(Coord(1, 2).dot(Coord(3, 4)), 11)

    def test_dist(self):
        self.assertAlmostEqual(Coord(2, 2).dist((4, 4)), math.sqrt(8))

    def test_almost_eq(self):
        self.assertEqual(Coord(0.00000000001, 0.999999999999).almost_eq((0, 1)), True)
        self.assertEqual(Coord(0.01, 4.99).almost_eq((0, 5), 1), True)
        self.assertEqual(Coord(0.01, 4.99).almost_eq((0, 5), 3), False)

    def test_repr(self):
        self.assertEqual(repr(Coord(0, 0)), 'Coord(x=0.000, y=0.000)')

    def test_neg(self):
        self.assertEqual(Coord(2, -2), -Coord(-2, 2))

    def test_abs(self):
        self.assertEqual(abs(Coord(2, -2)), Coord(2, 2))

    def test_round(self):
        self.assertEqual(round(Coord(5.55555, 12.00000000000001), 2), Coord(5.56, 12))
        self.assertEqual(round(Coord(5.55555, 12.00000000000001), 0), Coord(6, 12))

    def test_floor(self):
        self.assertEqual(math.floor(Coord(2.5, 3.5)), Coord(2, 3))

    def test_ceil(self):
        self.assertEqual(math.ceil(Coord(2.5, 3.5)), Coord(3, 4))

    def test_eq(self):
        self.assertTrue(Coord(5, 5) == Coord(5, 5))
        self.assertFalse(Coord(5, 4) == Coord(5, 5))
        self.assertTrue(Coord(5, 4) != Coord(4, 5))

    def test_add_sub(self):
        a = Coord(1, 2)
        b = (5, 4)
        c = Coord(6, 6)
        self.assertEqual(a + b, c)
        self.assertEqual(b + a, c)
        self.assertEqual(c - b, a)
        self.assertEqual(c - b, c + -Coord.from_tuple(b))
        self.assertEqual(b - a, Coord(4, 2))
        self.assertEqual(a + b - c, Coord())

    def test_mul(self):
        self.assertEqual(5 * Coord(2, 3), Coord(10, 15))
        self.assertEqual(Coord(2, 3) * Coord(3, 4), 18)


