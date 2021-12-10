from math import sqrt

def correlation(x, y):
    # correlation calcualtion

    # x = recalls (repeat for x = f1)
    # y = adhd_scores
    # both need to be dictionaries with key as participant name

    if(len(x)!= len(y)):
        print("error, fuck off!! this wasn't supposed to happen, you suck")
        print("get your shit together you teaspoon!!")
        exit()

    N = len(x)
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x_sq = 0
    sum_y_sq = 0

    for i in x:
        sum_x += x[i]
        sum_y += y[i]
        sum_xy += x[i]*y[i]
        sum_x_sq += x[i]*x[i]
        sum_y_sq += y[i]*y[i]

    correlation = ( N*sum_xy - sum_x*sum_y )
    correlation /= sqrt(( N*sum_x_sq - sum_x*sum_x )*( N*sum_y_sq - sum_y*sum_y ))
    print("correlation: ", correlation)

    return(correlation)

# testing corrlation
test_x = [14.2, 16.4, 11.9, 15.2, 18.5, 22.1, 19.4, 25.1, 23.4, 18.1, 22.6, 17.2]
test_y = [215, 325, 185, 332, 406, 522, 412, 614, 544, 421, 445, 408]
correlation(test_x, test_y)
