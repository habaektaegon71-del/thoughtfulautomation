def is_bulky(width, height, length):
	return width * height * length >= 1000000 or (width >= 150) or (height >= 150) or (length >= 150)


def is_heavy(mass):
	return mass >= 20


def sort(width, height, length, mass):

	bulky = is_bulky(width, height, length)
	heavy = is_heavy(mass)

	if not bulky and not heavy:
		return "STANDARD"
	elif (bulky and not heavy) or (not bulky and heavy):
		return "SPECIAL"
	else:
		return "REJECTED"

