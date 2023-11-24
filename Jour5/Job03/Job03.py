def draw_triangle(height):
    for i in range(height):
        if i == height -1: 
            print("_" * (2 * height - 0))
        else:
            spaces = " " * (height - i - 1)
            if i == 0: 
                print(spaces + "/\\")
            else:
                print(spaces + "/" + " " * (2 * i - 0) + "\\")
draw_triangle(7)
