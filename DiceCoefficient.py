import math

def rectangle_2d(x, y, x_size, y_size):
    x = float(x)
    y = float(y)
    x_size = float(x_size)
    y_size = float(y_size)
    # can put this stuff as method when turn rect_2d into class
    #res = 0.01
    #tempx = x
    #xrange_list = []
    #x_endpoint = x + x_size
    #print("x: {}, y: {}, x_size: {}, y_size: {}".format(x, y, x_size, y_size))
    #while tempx <= x_endpoint:
        #if tempx == x:
        #xrange_list.append(tempx)
        #tempx += res
        #else:
         #   xrange_list.append(tempx)
         #   tempx += res
    #for val in xrange_list:
     #   print(round(val, 1))
    return x, y, x_size, y_size

def area(rect):
    x = rect[0]
    y = rect[1]
    x_size = rect[2]
    y_size = rect[3]
    
    area_of_rectangle = x_size * y_size
    
    return area_of_rectangle

def intersect(rect1, rect2):
    rect1_x = rect1[0]
    rect1_y = rect1[1]
    rect1_xsize = rect1[2]
    rect1_ysize = rect1[3]
    rect1_res = 0.01
    
    rect2_x = rect2[0]
    rect2_y = rect2[1]
    rect2_xsize = rect2[2]
    rect2_ysize = rect2[3]
    rect2_res = 0.01
    
    rect1_tempx = rect1_x
    rect1_tempy = rect1_y
    
    rect2_tempx = rect2_x
    rect2_tempy = rect2_y
    
    rect1_xrange_list = []
    rect1_yrange_list = []
    
    rect2_xrange_list = []
    rect2_yrange_list = []
    
    rect1_x_endpoint = rect1_x + rect1_xsize
    rect1_y_endpoint = rect1_y + rect1_ysize
    
    rect2_x_endpoint = rect2_x + rect2_xsize
    rect2_y_endpoint = rect2_y + rect2_ysize
    
    while rect1_tempx <= rect1_x_endpoint:
        rect1_xrange_list.append(round(rect1_tempx, 2))
        rect1_tempx += rect1_res
            
    while rect1_tempy <= rect1_y_endpoint:
        rect1_yrange_list.append(round(rect1_tempy, 2))
        rect1_tempy += rect1_res
            
    while rect2_tempx <= rect2_x_endpoint:
        rect2_xrange_list.append(round(rect2_tempx, 2))
        rect2_tempx += rect2_res
        
    while rect2_tempy <= rect2_y_endpoint:
        rect2_yrange_list.append(round(rect2_tempy, 2))
        rect2_tempy += rect2_res
    
    # will return a set of the values that intersect (can't index these though)            
    #intersect_x = set(rect1_xrange_list).intersection(rect2_xrange_list)
    #intersect_y = set(rect1_yrange_list).intersection(rect2_yrange_list)
    
    x_intersection_list = []
    for rect1_xval in rect1_xrange_list:
        for rect2_xval in rect2_xrange_list:
            if rect1_xval == rect2_xval:
                x_intersection_list.append(rect1_xval)
                
    y_intersection_list = []
    for rect1_yval in rect1_yrange_list:
        for rect2_yval in rect2_yrange_list:
            if rect1_yval == rect2_yval:
                y_intersection_list.append(rect1_yval)
    
    if len(x_intersection_list) > 0:
        if len(y_intersection_list) > 0:
            overlap_rect_xorigin = x_intersection_list[0]
            overlap_rect_yorigin = y_intersection_list[0]
            last_x_index = len(x_intersection_list)
            last_y_index = len(y_intersection_list)
    
            overlap_rect_xsize = x_intersection_list[last_x_index-1] - x_intersection_list[0]
            overlap_rect_ysize = y_intersection_list[last_y_index-1] - y_intersection_list[0]

            overlap_rect = rectangle_2d(overlap_rect_xorigin, overlap_rect_yorigin, overlap_rect_xsize, overlap_rect_ysize)
        
            return overlap_rect
        else:
            return "There is no overlap..."

def dice_coefficient(rect1, rect2):
    #if intersect(rect1, rect2) == "There is no overlap...":
    #   dice_coefficient = "0: There is no overlap"
    #  return dice_coefficient
    #if area(rect1) != None:
     #   if area(rect2) != None:
    #else:
    if intersect(rect1, rect2) != None:
        area_overlap = area(intersect(rect1, rect2))
        dice_coefficient = ((2*area(intersect(rect1, rect2))) / (area(rect1) + area(rect2)))
        message = print("Area of overlap = {}".format(area_overlap) + "\n" + "Dice Coefficient = {}".format(round(dice_coefficient, 3)))
        return message
    if intersect(rect1, rect2) == None:
        print("0: There is no overlap")

    # testing output
def get_rect1():
    while True:
        try: 
            rect1_x, rect1_y, rect1_sizex, rect1_sizey, *other = map(float, input("Enter the following values for the First Rectangle: " +
                                                                            "x-origin, " +
                                                                            "y-origin, " +
                                                                            "rectangle length in the x-direction, " +
                                                                            "and the rectangle length in the y-direction: ").split(","))
            if other: 
                print("you entered too many parameters...")
                print()
                print(other)

        except ValueError:
                    print("-------------------------------------------------------------------------")
                    print("The coordinates should only contain integers or decimals and be separated with a comma")
                    # we'll also print a new line to allow some space between the instructions
                    print()
        else: 
            return rect1_x, rect1_y, rect1_sizex, rect1_sizey
def get_rect2():
    while True:
        try: 
            rect2_x, rect2_y, rect2_sizex, rect2_sizey, *other = map(float, input("Enter the following values for the Second Rectangle: " +
                                                                            "x-origin, " +
                                                                            "y-origin, " +
                                                                            "rectangle length in the x-direction, " +
                                                                            "and the rectangle length in the y-direction: ").split(","))
            if other: 
                print("you entered too many parameters...")
                print()
                print(other)
        except ValueError:
                    print("-------------------------------------------------------------------------")
                    print("The coordinates should only contain integers or decimals and be separated with a comma")
                    # we'll also print a new line to allow some space between the instructions
                    print()
        else:
            return rect2_x, rect2_y, rect2_sizex, rect2_sizey

def main():
    rect1_bounds = get_rect1()
    rect2_bounds = get_rect2()
    rect1 = rectangle_2d(rect1_bounds[0], rect1_bounds[1], rect1_bounds[2], rect1_bounds[3])
    rect2 = rectangle_2d(rect2_bounds[0], rect2_bounds[1], rect2_bounds[2], rect2_bounds[3])
    if intersect(rect1, rect2) != "There is no overlap...":
        overlapping_rectangle = intersect(rect1, rect2)

    print("Rectangle 1 Attributes:")
    print("x,y origin: ({}, {}) \nx_size: {} \ny_size: {}".format(rect1_bounds[0], rect1_bounds[1], rect1_bounds[2], rect1_bounds[3]))
    print("Area = {}".format(area(rect1)))
    print()
    print("Rectangle 2 Attributes:")
    print("x,y origin: ({}, {}) \nx_size: {} \ny_size: {}".format(rect2_bounds[0], rect2_bounds[1], rect2_bounds[2], rect2_bounds[3]))
    print("Area = {}".format(area(rect2)))
    print()
    print("Dice Coefficient:")
    dice_coefficient(rect1, rect2)


main()