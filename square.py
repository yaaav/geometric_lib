import unittest


def area(a):
    """
    По заданной стороне вычисляет площадь квадрата.
    
    Параметры:
    a (float): Длина стороны
    
    Возвращаемое значение:
    (float): Площадь квадрата
    
    Пример:
    >>> area(10.0)
    100.0
    """
    return a * a


def perimeter(a):
    """
    По заданной стороне вычисляет периметр квадрата.
    
    Параметры:
    a (float): Длина стороны
    
    Возвращаемое значение:
    (float): периметр квадрата
    
    Пример:
    >>> perimeter(10.0)
    40.0
    """
    return 4 * a


# Класс для тестирования функций квадрата
class SquareTestCase(unittest.TestCase):
    # Тесты для функции вычисления площади
    def test_area_normal(self):
        """Площадь квадрата со стороной 5 должна быть 25."""
        self.assertEqual(area(5), 25)  # 5 * 5 = 25

    def test_area_zero(self):
        """Площадь квадрата со стороной 0 должна быть 0."""
        self.assertEqual(area(0), 0)

    def test_area_fractional(self):
        """Площадь квадрата со стороной 2.5 должна быть 6.25."""
        self.assertEqual(area(2.5), 6.25)  # 2.5 * 2.5 = 6.25

    def test_area_one(self):
        """Площадь квадрата со стороной 1 должна быть 1."""
        self.assertEqual(area(1), 1)

    def test_area_negative(self):
        """Невалидные данные"""
        self.assertEqual(area(-1), 1)

    def test_area_string(self):
        """Передача строки должна вызывать TypeError."""
        with self.assertRaises(TypeError):
            area("abc")

    # Тесты для функции вычисления периметра
    def test_perimeter_normal(self):
        """Периметр квадрата со стороной 5 должен быть 20."""
        self.assertEqual(perimeter(5), 20)  # 4 * 5 = 20

    def test_perimeter_zero(self):
        """Периметр квадрата со стороной 0 должен быть 0."""
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_fractional(self):
        """Периметр квадрата со стороной 1.5 должен быть 6."""
        self.assertEqual(perimeter(1.5), 6.0)  # 4 * 1.5Периметр квадрата со отрицательной стороной -1 должен быть -4 = 6.0

    def test_perimeter_one(self):
        """Периметр квадрата со стороной 1 должен быть 4."""
        self.assertEqual(perimeter(1), 4)

    def test_perimeter_negative(self):
        """Невалидные данные"""
        self.assertEqual(perimeter(-1), -4)

    def test_perimeter_string(self):
        """Невалидные данные"""
        self.assertEqual(perimeter('4'), '4444')

# Блок для запуска тестов при непосредственном выполнении файла
if __name__ == "__main__":
    unittest.main()
