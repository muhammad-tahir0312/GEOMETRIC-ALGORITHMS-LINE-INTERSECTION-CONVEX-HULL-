import tkinter as tk
import time as time
import numpy as np
import math
import random

class ConvexHullApp:
    def __init__(self, master, width, height):
        self.master = master
        self.master.title("Convex Hull Algorithms")
        self.canvas = tk.Canvas(master, width=width, height=height, bg="white")
        self.canvas.pack()

        self.points = []
        self.convex_hull = []
        self.start_time = time.time()

        self.canvas.bind("<Button-1>", self.add_point)

        # Algorithm selection dropdown menu
        self.algorithm_var = tk.StringVar()
        self.algorithm_var.set("Graham Scan")  # Default selection
        algorithms = ["Graham Scan", "Jarvis March", "Quick Hull", "Montone's Chain", "Brute Force"]
        self.algorithm_menu = tk.OptionMenu(master, self.algorithm_var, *algorithms)
        self.algorithm_menu.pack()

        self.draw_button = tk.Button(master, text="Draw Convex Hull", command=self.draw_convex_hull)
        self.draw_button.pack()

        self.time_label = tk.Label(master, text="Time Elapsed:  seconds")
        self.time_label.pack()

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_canvas)
        self.reset_button.pack()

        # Draw x and y axes with a small gap
        #gap = 10
        #self.canvas.create_line(gap, height - gap, width, height - gap, fill="black", width=2)  # x-axis
        #self.canvas.create_line(gap, gap, gap, height - gap, fill="black", width=2)  # y-axis
        #self.canvas.create_text(width - 20, height - gap + 20, text="X", anchor="w", fill="black",
        #                        font=("Helvetica", 12, "bold"))
        #self.canvas.create_text(gap + 20, gap + 20, text="Y", anchor="w", fill="black", font=("Helvetica", 12, "bold"))

    def update_time_label(self):
        elapsed_time = time.time() - self.start_time
        self.time_label.config(text=f"Time Elapsed: {round(elapsed_time, 10)} seconds")
    
    def draw_line_segment(self, p1, p2, color="red"):
        x1, y1 = p1
        x2, y2 = p2
        self.canvas.create_line(x1, y1, x2, y2, fill=color, width=2, tags="convex_hull")

    def add_point(self, event):
        x, y = event.x, event.y
        self.points.append((x, y))
        self.canvas.create_oval(x - 3, y - 3, x + 3, y + 3, fill="white")
        self.canvas.create_text(x + 10, y - 10, text=f"({x}, {y})", anchor="w", fill="blue")

    def draw_convex_hull(self):
        if len(self.points) < 3:
            return

        # Delete the previous convex hull
        self.canvas.delete("convex_hull")

        algorithm = self.algorithm_var.get()

        if algorithm == "Graham Scan":
            self.convex_hull = self.graham_scan()
        elif algorithm == "Jarvis March":
            self.convex_hull = self.jarvis_march_convex_hull()
        elif algorithm == "Quick Hull":
            self.convex_hull = self.quickhull()
        elif algorithm == "Montone's Chain":
            self.convex_hull = self.andrews_monotone_chain()
        elif algorithm == "Brute Force":
            self.convex_hull = self.brute_force()
        
        # Draw the convex hull
        if self.convex_hull != None:
            for frame in range(1, len(self.convex_hull)+1):
                if frame == len(self.convex_hull):
                    frame = 0
                def update(frame):
                    c0 = self.convex_hull[frame - 1]
                    c1 = self.convex_hull[frame]
                    self.canvas.create_line(c0[0],c0[1], c1[0], c1[1], fill='red', width=2)
                self.canvas.after(500 * frame, update, frame)
        
        
    def reset_canvas(self):
        # Reset canvas by deleting all points and the convex hull
        self.canvas.delete("all")
        self.points = []
        self.convex_hull = []
        self.start_time = time.time()
        self.update_time_label()


        # Redraw x and y axes with a small gap
        # gap = 10
        # self.canvas.create_line(gap, self.canvas.winfo_reqheight() - gap, self.canvas.winfo_reqwidth(),
        #                         self.canvas.winfo_reqheight() - gap, fill="black", width=2)  # x-axis
        # self.canvas.create_line(gap, gap, gap, self.canvas.winfo_reqheight() - gap, fill="black", width=2)  # y-axis
        # self.canvas.create_text(self.canvas.winfo_reqwidth() - 20, self.canvas.winfo_reqheight() - gap + 20, text="X",
        #                         anchor="w", fill="black",
        #                         font=("Helvetica", 12, "bold"))
        # self.canvas.create_text(gap + 20, gap + 20, text="Y", anchor="w", fill="black", font=("Helvetica", 12, "bold"))
    
    def graham_scan(self):
        start=time.time()
        # Implement the graham_scan function as before
        global anchor # to be set, (x,y) with smallest y value

        def polar_angle(p0,p1=None):
            if p1==None: p1=anchor
            y_span=p0[1]-p1[1]
            x_span=p0[0]-p1[0]
            return math.atan2(y_span,x_span)

        def distance(p0,p1=None):
            if p1==None: p1=anchor
            y_span=p0[1]-p1[1]
            x_span=p0[0]-p1[0]
            return y_span**2 + x_span**2
        
        def quicksort(a):
            if len(a)<=1:
                return a
            smaller= []
            equal=[]
            larger =[]
            piv_ang=polar_angle(a[random.randint(0,len(a)-1)]) # select random pivot
            for pt in a:
                pt_ang=polar_angle(pt) # calculate current point angle
                if   pt_ang<piv_ang:  smaller.append(pt)
                elif pt_ang==piv_ang: equal.append(pt)
                else:larger.append(pt)
            return  quicksort(smaller) \
                +sorted(equal,key=distance) \
                    +quicksort(larger)

	    # Find the (x,y) point with the lowest y value,
	    # along with its index in the 'points' list. If
	    # there are multiple points with the same y value,
	    # choose the one with smallest x.
        min_idx=None
        for i,(x,y) in enumerate(self.points):
            if min_idx==None or y<self.points[min_idx][1]:
                min_idx=i
            if y==self.points[min_idx][1] and x<self.points[min_idx][0]:
                min_idx=i

	    # set the global variable 'anchor', used by the
	    # 'polar_angle' and 'distance' functions
        anchor= self.points[min_idx]

	    # sort the points by polar angle then delete
	    # the anchor from the sorted list
        sorted_pts=quicksort(self.points)
        del sorted_pts[sorted_pts.index(anchor)]

        def det(p1,p2,p3):
            return   (p2[0]-p1[0])*(p3[1]-p1[1]) \
			-(p2[1]-p1[1])*(p3[0]-p1[0])

	    # anchor and point with smallest polar angle will always be on hull
        hull=[anchor,sorted_pts[0]]
        for s in sorted_pts[1:]:
            while det(hull[-2],hull[-1],s)<=0:
                del hull[-1] # backtrack
			#if len(hull)<2: break
            hull.append(s)
        self.update_time_label()
        return hull


    def jarvis_march_convex_hull(self):
        start = time.time()
        def orientation(p, q, r):
            val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
            if val == 0:
                return 0
            return 1 if val > 0 else -1
    # Implementation of jarvis_march_convex_hull function as before
        n = len(self.points)
        if n < 3:
            raise ValueError("Convex hull not possible with less than 3 points")

    # Find the point with the lowest y-coordinate (and leftmost if ties)
        pivot = min(self.points, key=lambda p: (p[1], p[0]))

        hull = []  # Convex hull to be returned

        while True:
            hull.append(pivot)
            endpoint = self.points[0]

            for i in range(1, n):
                if endpoint == pivot or orientation(pivot, endpoint, self.points[i]) == -1:
                    endpoint = self.points[i]

            if endpoint == hull[0]:
                break  # Convex hull is complete

            pivot = endpoint
        self.update_time_label()
        return hull

    def quickhull(self):
        start=time.time()
        points = self.points
        def calculate_determinant(point_1,point_2,point_3):
            return (point_1[0] * point_2[1]) + (point_1[1] * point_3[0]) + (point_2[0] * point_3[1]) - (point_3[0] * point_2[1]) - (point_3[1] * point_1[0]) - (point_2[0] * point_1[1])

        def find_min_and_max(points):
            minimum_point = points[0]
            maximum_point = points[0]
            for point in points:
                if(point[0] <= minimum_point[0]):
                    minimum_point = point
                if(point[0] >= maximum_point[0]):
                    maximum_point = point
            return minimum_point,maximum_point

        def calc_line_dist(min_absis,max_absis,point):
            return abs((point[1] - min_absis[1]) * (max_absis[0] - min_absis[0]) - (max_absis[1] - min_absis[1]) * (point[0] - min_absis[0]))

        def divide_side(points,min_absis,max_absis):
            left_hull = []
            right_hull = []
            for point in points:
                if(point != min_absis) and (point != max_absis):
                    if (calculate_determinant(min_absis,max_absis,point) > 0):
                        left_hull.append(point)
                    if (calculate_determinant(min_absis,max_absis,point) < 0):
                        right_hull.append(point)
            return left_hull,right_hull

        def find_max_distance(points,min_absis,max_absis):
            max_distance = 0
            index_of_max = 0
            for i in range(0,len(points)):
                curr_distance = calc_line_dist(min_absis,max_absis,points[i])
                if curr_distance > max_distance:
                    index_of_max = i
                    max_distance = curr_distance
            return points[index_of_max]

        def quick_hull_left(points,min_absis,max_absis):
            if(len(points) == 0):
                return
            else:
                max_point = find_max_distance(points,min_absis,max_absis)
                points.remove(max_point)
                list_of_hull.append(max_point)
                first_side,_ = divide_side(points,min_absis,max_point)
                second_side,_ = divide_side(points,max_point,max_absis)
                quick_hull_left(first_side,min_absis,max_point)
                quick_hull_left(second_side,max_point,max_absis)

        def quick_hull_right(points,min_absis,max_absis):
            if(len(points) == 0):
                return
            else:
                max_point = find_max_distance(points,min_absis,max_absis)
                points.remove(max_point)
                list_of_hull.append(max_point)
                _,first_side = divide_side(points,min_absis,max_point)
                _,second_side = divide_side(points,max_point,max_absis)
                quick_hull_right(first_side,min_absis,max_point)
                quick_hull_right(second_side,max_point,max_absis)

        if len(points) <= 1:
            return points

        min_absis, max_absis = find_min_and_max(points)
        left_hull, right_hull = divide_side(points, min_absis, max_absis)
        list_of_hull = [min_absis, max_absis]
        quick_hull_left(left_hull, min_absis, max_absis)
        quick_hull_right(right_hull, min_absis, max_absis)

        central_x = sum(point[0] for point in list_of_hull)/len(list_of_hull)
        central_y = sum(point[1] for point in list_of_hull)/len(list_of_hull)
        list_of_hull.sort(key = lambda point: math.atan2(point[0] - central_x, point[1] - central_y))

        tuple_of_hull = []
        for i in range(0,len(list_of_hull)):
            if(i == len(list_of_hull)-1):
                tuple_of_hull.append([list_of_hull[i],list_of_hull[0]])
            else:
                tuple_of_hull.append([list_of_hull[i],list_of_hull[i+1]])
        self.update_time_label()
        return tuple_of_hull


    
    def brute_force(self):
        points= self.points
        start=time.time()
        def orientation(p, q, r):
            val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
            if val == 0:
                return 0  # collinear
            elif val > 0:
                return 1  # clockwise
            else:
                return 2  # counterclockwise
        n = len(points)
        # There must be at least 3 points
        if n < 3:
            return []

        # Initialize result
        hull = []

        # Find the leftmost point
        l = 0
        for i in range(1, n):
            if points[i][0] < points[l][0]:
                l = i

        p = l
        q = None
        while True:
            hull.append(points[p])
            q = (p + 1) % n
            for r in range(n):
                if orientation(points[p], points[q], points[r]) == 2:
                    q = r
            p = q
            if p == l:
                break
        self.update_time_label()
        return hull
    def andrews_monotone_chain(self):
        start = time.time()
        def orientation(p, q, r):
            val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
            if val == 0:
                return 0
            return 1 if val > 0 else -1

        points = self.points
        n = len(points)
        if n < 3:
            raise ValueError("Convex hull not possible with less than 3 points")

        points = sorted(points)  # Sort points lexicographically

        # Build lower hull
        lower_hull = []
        for p in points:
            while len(lower_hull) >= 2 and orientation(lower_hull[-2], lower_hull[-1], p) != -1:
                lower_hull.pop()
            lower_hull.append(p)

        # Build upper hull
        upper_hull = []
        for p in reversed(points):
            while len(upper_hull) >= 2 and orientation(upper_hull[-2], upper_hull[-1], p) != -1:
                upper_hull.pop()
            upper_hull.append(p)

        # Concatenate the lower and upper hulls to get the convex hull
        convex_hull = lower_hull[:-1] + upper_hull[:-1]
        self.update_time_label()
        return convex_hull

if __name__ == "__main__":
    root = tk.Tk()
    app = ConvexHullApp(root, width=900, height=500)
    root.mainloop()
