# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
print('\nЗадача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.')
import math

class Triangle:
	def __init__(self, A, B, C):
		# Функция вычисляет длину стороны согласно координатам точек
		def sideLen(dot1, dot2):
			return math.sqrt((dot2[0] - dot1[0]) ** 2
							 + (dot2[1] - dot1[1]) ** 2)
		self.A = A
		self.B = B
		self.C = C
		# На основании соседних координат вычисляем длины
		self.AB = sideLen(self.A, self.B)
		self.BC = sideLen(self.B, self.C)
		self.CA = sideLen(self.C, self.A)

	# Вычисление площади треугольника по формуле Герона
	def areaTriangle(self):
		semi_perimeter = self.perimeterTriangle() / 2
		return math.sqrt(semi_perimeter * (semi_perimeter - self.AB) * (semi_perimeter - self.BC) * (semi_perimeter - self.CA))

	# вычисляем периметр треугольника
	def perimeterTriangle(self):
		return self.AB + self.BC + self.CA

	# Вычисляем высоту треугольника
	def heightTriangle(self):
		return self.areaTriangle() / (self.AB / 2)


treugolnik1 = Triangle((3, 2), (6, 7), (0, 12))

# Вывод на экран результатов
print("\nПериметр Треугольника = %1.2f " % treugolnik1.perimeterTriangle(),"\nВысота Треугольника = %1.2f " % treugolnik1.heightTriangle(),
	  "\nПлощадь Треугольника = %1.2f " % treugolnik1.areaTriangle())




# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
print('\nЗадача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.')
class Trapeze:
	def __init__(self, A, B, C, D):
		# Функция вычисляет длину стороны согласно координатам точек
		def sideLen(dot1, dot2):
			return math.sqrt((dot2[0] - dot1[0]) ** 2 + (dot2[1] - dot1[1]) ** 2)

		self.A = A
		self.B = B
		self.C = C
		self.D = D

		self.AB = sideLen(self.A, self.B)
		self.BC = sideLen(self.B, self.C)
		self.CD = sideLen(self.C, self.D)
		self.DA = sideLen(self.D, self.A)
		self.AC = sideLen(self.A, self.C)
		self.BD = sideLen(self.B, self.D)
		self.perimeter = self.AB + self.BC + self.CD + self.DA
		# Вычисление P1 - Периметр 1 Треугольника
		self.perimeter_trenagle1 = 0.5*(self.AB + self.BC + self.AC)
		# Вычисление P2 - Периметр 2 Треугольника
		self.perimeter_trenagle2 = 0.5*(self.CD + self.DA + self.AC)

	# Вычисление P - периметр трапеции
	def Trapeze_P(self):
		return self.AB + self.BC + self.CD + self.DA

	# Вычисление S - площади трапеции. Делим трапецию на 2 треугольника и вычисляем площади треугольников по формуле Герона и складываем их.
	def Trapeze_S(self):
		return (math.sqrt(self.perimeter_trenagle1*(self.perimeter_trenagle1 - self.AB)*(self.perimeter_trenagle1 - self.BC)*(self.perimeter_trenagle1 - self.AC)))+\
			   (math.sqrt(self.perimeter_trenagle2*(self.perimeter_trenagle2 - self.CD)*(self.perimeter_trenagle2 - self.DA)*(self.perimeter_trenagle2 - self.AC)))

	# Проверка равнобедренности
	def isTrapezeEqu(self):
		if self.AC == self.BD:
			return True
		return False

Trapeze1 = Trapeze((3, 2), (6, 7), (12, 7), (15, 2))

# Вывод на экран результатов
print("\nПериметр Трапеции = %1.2f " % Trapeze1.Trapeze_P(), "\nПлощадь Трапеции = %1.2f " % Trapeze1.Trapeze_S(), "\nСтороны Трапеции ABCD",
	  "\nAB = %1.2f " % Trapeze1.AB, "BC = %1.2f " % Trapeze1.BC, "CD = %1.2f " % Trapeze1.CD, "DA = %1.2f " % Trapeze1.DA)