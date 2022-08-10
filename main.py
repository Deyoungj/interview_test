
from colors import list_of_colors

from mean import calculate_mean
from median import calculate_median
from variance import calculate_variance


# Which color of shirt is the mean color?

calculate_mean(list_of_colors)

# Which color is mostly worn throughout the week?
colour = max(list_of_colors)

print('color mostly worn throughout the week is blue, because it occurs: ',colour, 'times in the week' )


# Which color is the median?
calculate_median(list_of_colors)

# Which color is the standard deviation?
