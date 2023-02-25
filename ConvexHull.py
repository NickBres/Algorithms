import numpy

def direction(point_a,point_b,point_c):
    mat = [[1,1,1],[point_a[0],point_b[0],point_c[0]],[point_a[1],point_b[1],point_c[1]]]
    det = numpy.linalg.det(mat)
    if det > 0:
        return 'left'
    elif det < 0:
        return 'right'
    else:
        return 'straight'

def find_lowest_point(points):
    res = points[0]
    for point in points:
        if point[1] < res[1]:
            res = point
    return res
def compare(a,b):
    return a[0]-b[0]

def Grahams_scan(points):  # Andrew's algorithm O(n)
    lowest_point = find_lowest_point(points)
    points.sort(key=compare())  # sort points by x from small to large

    points.remove(lowest_point)  # add the lowest point to the first place
    points.insert(0,lowest_point)

    stack = [points[0],points[1]]
    for i in range(3,len(points)):
        if direction(stack[-1],stack[-2],points[i]) == 'left':
            stack.pop()
        stack.insert(points[i])

    return stack

if __name__ == '__main__':
    print(direction((-5,5),(-2,10),(-1,6)))