from collections import Counter
from turtle import color


def calculate_mode(colors:list):

	len_of_colors = len(colors)

	# sort the number in ascending order

	colors.sort()

	data = Counter(colors)
	# convert to a dictionary

	data_dict = dict(data)

	mode = [k for k, v in data_dict.items() if v == max(list(data_dict.values()))]

	if len(mode) == len_of_colors:
		get_mode =  "no mode found"

	else:
		get_mode = "Mode is or are: "+ ','.join(map(str,mode))

	print(get_mode)