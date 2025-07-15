def equilateral(sides):
    if sides[0] == sides[1] == sides[2] and sides[0] != 0:
        return True
    else:
        return False 


def isosceles(sides):
    # Check triangle inequality first
    if sides[0] + sides[1] <= sides[2] or sides[1] + sides[2] <= sides[0] or sides[0] + sides[2] <= sides[1]:
        return False
    # Check if at least two sides are equal
    if sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
        return True
    else:
        return False


def scalene(sides):
    # Check triangle inequality first
    if sides[0] + sides[1] <= sides[2] or sides[1] + sides[2] <= sides[0] or sides[0] + sides[2] <= sides[1]:
        return False
    # Check if all sides are different
    if sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]:
        return True
    else:
        return False

