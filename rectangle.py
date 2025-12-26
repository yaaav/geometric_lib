import unittest


def area(a, b):  
    """
    По заданным сторонам вычисляет площадь прямоугольника
    
    Параметры:
    a (float): Длина первой стороны
    b (float): Длина второй стороны
    
    Возращаемое значение:
    float: Площадь прямоугольника
    
    Пример:
    >>> area(7.0, 10.0)
    70.0
    """
    return a * b  

 

def perimeter(a, b):  
    """
    По заданным сторонам вычисляет периметр прямоугольника
    
    Параметры:
    a (float): Длина первой стороны
    b (float): Длина второй стороны
    
    Возращаемое значение:
    float: периметр прямоугольника
    
    Пример:
    >>> perimeter(7.0, 10.0)
    34.0
    """
    return (a + b) * 2

# Класс для тестирования функций треугольника
class RectangleTestCase(unittest.TestCase):
    # Тесты для функции вычисления площади
    def test_area_normal(self):
        """Площадь прямоугольника 5x3 должна быть 15."""
        self.assertEqual(area(5, 3), 15)

    def test_area_zero(self):
        """Площадь, если одна из сторон нулевая, должна быть 0."""
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(5, 0), 0)

    def test_area_square(self):
        """Площадь квадрата 4x4 должна быть 16."""
        self.assertEqual(area(4, 4), 16)

    def test_area_fractional(self):
        """Площадь прямоугольника 2.5x4 должна быть 10.0."""
        self.assertEqual(area(2.5, 4), 10.0)

    # Тесты для функции вычисления периметра
    def test_perimeter_normal(self):
        """Периметр прямоугольника 5x3 должен быть 16."""
        self.assertEqual(perimeter(5, 3), 16)

    def test_perimeter_zero(self):
        """Периметр, если обе стороны нулевые, должен быть 0."""
        self.assertEqual(perimeter(0, 0), 0)

    def test_perimeter_square(self):
        """Периметр квадрата 4x4 должен быть 16."""
        self.assertEqual(perimeter(4, 4), 16)

    def test_perimeter_fractional(self):
        """Периметр прямоугольника 2.5x3.5 должен быть 12.0."""
        self.assertEqual(perimeter(2.5, 3.5), 12.0)

if __name__ == '__main__':
    unittest.main()