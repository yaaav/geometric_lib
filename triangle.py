import unittest


def area(a, h):  
    """
    По основанию и высоте вычисляет площадь треугольника
    
    Параметры:
    a (float): Длина основания треугольника
    h (float): Высота треугольника опущенная на основание
    
    Возвращаемое значение:
    float: Площадь треугольника
    
    Пример:
    >>> area(3.0, 6.0)
    9.0
    """
    return a * h / 2  

 

def perimeter(a, b, c):  
    """
    По заданным сторонам вычисляет периметр треугольника
    
    Параметры:
    a (float): Длина первой стороны
    b (float): Длина второй стороны
    c (float): Длина третьей стороны

    Возвращаемое значение:
    float: периметр треугольника
    
    Пример:
    >>> perimeter(3.0, 4.0, 5.0)
    12.0
    """
    return a + b + c  

# Класс для тестирования функций треугольника
class TriangleTestCase(unittest.TestCase):
    # Тесты для функции вычисления площади
    def test_area_normal(self):
        """Площадь треугольника с основанием 10 и высотой 5 должна быть 25."""
        self.assertEqual(area(10, 5), 25)  # (10 * 5) / 2 = 25

    def test_area_zero_height(self):
        """Площадь треугольника с нулевой высотой должна быть 0."""
        self.assertEqual(area(10, 0), 0)

    def test_area_zero_base(self):
        """Площадь треугольника с нулевым основанием должна быть 0."""
        self.assertEqual(area(0, 5), 0)

    def test_area_fractional_result(self):
        """Площадь треугольника с основанием 5 и высотой 3 должна быть 7.5."""
        self.assertEqual(area(5, 3), 7.5)  # (5 * 3) / 2 = 7.5

    # Тесты для функции вычисления периметра
    def test_perimeter_normal(self):
        """Периметр треугольника со сторонами 3, 4, 5 должен быть 12."""
        self.assertEqual(perimeter(3, 4, 5), 12)  # 3 + 4 + 5 = 12

    def test_perimeter_equal_sides(self):
        """Периметр равностороннего треугольника со стороной 5 должен быть 15."""
        self.assertEqual(perimeter(5, 5, 5), 15)  # 5 + 5 + 5 = 15

    def test_perimeter_zero_side(self):
        """Периметр треугольника с одной нулевой стороной."""
        self.assertEqual(perimeter(0, 4, 5), 9)   # 0 + 4 + 5 = 9

    def test_perimeter_all_zero(self):
        """Периметр треугольника со всеми нулевыми сторонами должен быть 0."""
        self.assertEqual(perimeter(0, 0, 0), 0)

# Блок для запуска тестов при непосредственном выполнении файла
if __name__ == "__main__":
    unittest.main()