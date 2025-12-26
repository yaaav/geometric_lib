import math
import unittest


def area(r):
    '''
    По заданному радиусу вычисляет площадь круга
    
        Параметры:
            r (float): радиус круга
        Возращаемое значение:
            (float): площадь круга
        Пример вызова:
            >>> area(8.0)
            201.0619298297468
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    По заданному радиусу вычисляет периметр круга
    
        Параметры:
            r (float): радиус круга
        Возращаемое значение:
            (float): периметр круга
        Пример вызова:
            >>> perimeter(8.0)
            50.26548245743669
    '''
    return 2 * math.pi * r

# Класс для тестирования функций круга
class CircleTestCase(unittest.TestCase):
    # Тесты для функции вычисления площади
    def test_area_normal(self):
        """Площадь круга радиусом 5 должна быть π*25."""
        self.assertAlmostEqual(area(5), math.pi * 25, places=7)

    def test_area_zero(self):
        """Площадь круга радиусом 0 должна быть 0."""
        self.assertEqual(area(0), 0)

    def test_area_fractional(self):
        """Площадь круга радиусом 2.5 должна быть π*6.25."""
        self.assertAlmostEqual(area(2.5), math.pi * 6.25, places=7)

    def test_area_one(self):
        """Площадь круга радиусом 1 должна быть π."""
        self.assertAlmostEqual(area(1), math.pi, places=7)

    # Тесты для функции вычисления периметра (длины окружности)
    def test_perimeter_normal(self):
        """Длина окружности радиусом 5 должна быть 2*π*5."""
        self.assertAlmostEqual(perimeter(5), 2 * math.pi * 5, places=7)

    def test_perimeter_zero(self):
        """Длина окружности радиусом 0 должна быть 0."""
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_fractional(self):
        """Длина окружности радиусом 2.5 должна быть 2*π*2.5."""
        self.assertAlmostEqual(perimeter(2.5), 2 * math.pi * 2.5, places=7)

    def test_perimeter_one(self):
        """Длина окружности радиусом 1 должна быть 2*π."""
        self.assertAlmostEqual(perimeter(1), 2 * math.pi, places=7)

if __name__ == '__main__':
    unittest.main()