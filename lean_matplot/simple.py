import matplotlib.pyplot as plt


def show_line_diagram():
    input_values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    plt.plot(input_values, squares, linewidth=5)

    # name a title and label x,y, set the fontsize for text
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    # show both axis '刻度‘
    plt.tick_params(axis="both", labelsize=14)

    # render the plot diagram
    plt.show()


def show_scatter():
    x = [2, 3, 4, 5, 6, 7, 8]
    y = [1, 2, 3, 4, 5, 6, 7]
    plt.scatter(x, y, s=100)  # x,y is two list contains the value need show on screen
    plt.title("Scatter Title")
    plt.xlabel("X-Label")
    plt.ylabel("Y-Label")
    plt.show()


def show_scatter_different_way():
    x_value = list(range(1, 1001))
    print(x_value)
    y_value = [x_v ** 2 for x_v in x_value]
    plt.title("100 value y=x_value^2", fontsize=24)
    plt.tick_params(axis="both", labelsize=14)
    plt.xlabel("X Series", fontsize=14)
    plt.ylabel("Y Series", fontsize=14)
    plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.ma, s=40)
    plt.axis([0, 1100, 0, 110000])
    plt.show()

def test_q_one():
    x_values = [1,2,3,4,5]
    y_vlaues = [x**3 for x in x_values]
    plt.title("Y=X^3 aka f(x) = x^3 ")
    plt.scatter(x_values, y_vlaues, s=40)
    plt.show()


def test_q_two():
    x_value = list(range(1, 5000))
    y_value = [x ** 3 for x in x_value]
    plt.title("Y=X^3 aka f(x) = x^3 ")
    plt.scatter(x_value, y_value, s=40)
    #plt.axis([0, 5001, 0, 1000])
    plt.show()

# show_line_diagram()
# show_scatter()
# show_scatter_different_way()
# test_q_one()
test_q_two()