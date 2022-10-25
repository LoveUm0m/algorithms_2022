import os

class calc():

	def __init__(self):
		self.operation = str()
		self.number_one = float()
		self.number_two = float()
        def cls(self):
		os.system('cls' if os.name == 'nt' else 'clear')


	def input_operation(self):
		self.operation = input('Введите операцию (+, -, *, / или 0 для выхода): ')
		if (self.operation == '+') or (self.operation == '-') or (self.operation == '*') or (self.operation == '/') or (self.operation == '0'):
			if self.operation == '0':
				self.bb()
			self.calculation()
		else:
			self.cls()
			print('Вы допустили ошибку при введении операции!')
			self.input_operation()

	def input_numbers(self):
		try:
			self.number_one = float(input('Введите первое число: '))
			self.number_two = float(input('Введите второе число: '))
		except Exception as e:
			print('Допущена ошибка при вводе числа. Трай аген)')
			self.input_numbers()


	def calculation(self):
		self.input_numbers()
		if self.operation == '+':
			self.cls()
			print(f'{self.number_one} + {self.number_two} = {self.number_one + self.number_two}')
		elif self.operation == '-':
			self.cls()
			print(f'{self.number_one} - {self.number_two} = {self.number_one - self.number_two}')
		elif self.operation == '*':
			self.cls()
			print(f'{self.number_one} * {self.number_two} = {self.number_one * self.number_two}')
		elif self.operation == '/':
			self.cls()
			if self.number_two == 0:
				print('Деление на ноль!')
			else:
				print(f'{self.number_one} / {self.number_two} = {self.number_one / self.number_two}')
		self.input_operation()


	def bb(self):
		exit()
calc = calc()
calc.input_operation()