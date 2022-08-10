def calculate_variance(colors:list):

    len_of_colors = len(colors)

    # Mean of the data
    mean = sum(colors) / len_of_colors

    # Square deviations
    deviations = [(x - mean) ** 2 for x in colors]
    # Variance
    variance = sum(deviations) / len_of_colors
    print('the variance of the colors is: ' + str(variance))
