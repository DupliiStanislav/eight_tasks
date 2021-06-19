

class Envelope:
	"""
	Create class Envelope and initialize length and width
	"""
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def __sub__(self, other):
		"""
		Change magic method for comparing our envelopes
		"""
		if self.length > other.length and self.width > other.width:
			return f'We can put {other.__str__()} into {self.__str__()}'
		elif self.length < other.length and self.width < other.width:
			return f'We can put {self.__str__()} into {other.__str__()}'

	def __str__(self):
		"""
		Change method __str__ to represent good print
		"""
		return f'Envelope with length: {self.length} \
and width: {self.width}'


def is_positive_valid(*args):
	"""
	validation for non-negative input
	"""
	if any(num < 0 for num in args):
		raise ValueError
	return args[0]


def main():
	"""
	main function to manage all of the logic
	"""
	while True:
		try:
			length1 = is_positive_valid(float(input('Insert length of 1st envelope:')))
			width1 = is_positive_valid(float(input('Insert width of 1st envelope:')))
			length2 = is_positive_valid(float(input('Insert length of 2nd envelope:')))
			width2 = is_positive_valid(float(input('Insert width of 2nd envelope:')))
		except ValueError:
			print('To create an envelope you should use positive integer or float numbers')
			continue

		# create our envelopes
		env1 = Envelope(length1, width1)
		env2 = Envelope(length2, width2)

		# check if we can put one envelope into another
		check = env1 - env2
		print(check)

		next_ = input('If you want to check another one pair of envelopes print "yes"')

		if next_.lower() != 'yes':
			break


if __name__ == '__main__':
	main()





