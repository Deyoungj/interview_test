
def calculate_median(colors:list):

	len_of_colors = len(colors)

	# sort the number in decending order
	colors.sort()
	

	#we check if the total colors is an even number

	if len_of_colors % 2 == 0:

		median1 = colors[int(len_of_colors/2)]
		print('median1',median1)
		median2 = colors[int(len_of_colors/2-1)]
		print('median2',median2)
		median = (median1 + median2)/2
	else:
		median = colors[int(len_of_colors/2)]

	print('Median is: ', median)



