class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class QuadTree:
    def __init__(self, x, y, w, h, capacity, tree_list):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.tree_list = tree_list

        self.capacity = capacity
        self.subdivided = False
        self.points = []

    def subdivide(self):
        if not self.subdivided and len(self.points) >= self.capacity:
            self.nw = QuadTree(self.x, self.y, self.w/2, self.h/2, self.capacity, self.tree_list)
            self.ne = QuadTree(self.x + self.w/2, self.y, self.w/2, self.h/2, self.capacity, self.tree_list)
            self.sw = QuadTree(self.x, self.y + self.h/2, self.w/2, self.h/2, self.capacity, self.tree_list)
            self.se = QuadTree(self.x + self.w/2, self.y + self.h/2, self.w/2, self.h/2, self.capacity, self.tree_list)
            self.tree_list.append(self.nw)
            self.tree_list.append(self.sw)
            self.tree_list.append(self.ne)
            self.tree_list.append(self.se)
            self.subdivided = True

    def insert(self, point):
        if point.x >= self.x and point.x < self.x + self.w and point.y >= self.y and point.y < self.y + self.h and not self.subdivided:
            self.points.append(point)
            self.subdivide()
        elif self.subdivided:
            self.nw.insert(point)
            self.ne.insert(point)
            self.sw.insert(point)
            self.se.insert(point)
        else:
            return
    
    def query(self, query_tree_list, x, y, w, h):
        checked_list = []
        point_list = []

        for i in query_tree_list:
            if i.x + i.w > x and i.x < x + w and i.y + i.h > y and i.y < y + h:
                checked_list.append(i)
        
        for i in checked_list:
            for j in i.points:
                if j.x > x and j.x < x + w and j.y > y and j.y < y + h:
                    point_list.append(j)
        
        return point_list, checked_list