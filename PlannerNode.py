import sys
from MapNode import MapNode

class PlannerNode:
    def __init__(self):
        self.current_obj=MapNode()
        
        # Since we know that the first step the bot will take will be down, we can simply do it here
        self.current_obj.direction_callback("down")  # example 1
        self.wall_callback()

    def wall_callback(self):
        turn = ["right", "down", "left", "up"]
        visited = set()
        visited.add(self.current_obj.current)

        stack = [self.current_obj.current]

        while stack:
            position = self.current_obj.current

            for direction in turn:
                oldpos = self.current_obj.current
                self.current_obj.direction_callback(direction)
                newpos = self.current_obj.current

                if newpos !=oldpos and newpos not in visited:
                    visited.add(newpos)
                    stack.append(newpos)
                    break
                else:
                    self.current_obj.current = oldpos
            else:
                stack.pop()
                if stack:
                    self.current_obj.current = stack[-1]

            if self.current_obj.current == self.current_obj._MapNode__map.end:
                   break
       
        # current_obj has all the attributes to help you in in your path planning !
       # pass # Your code goes here. You need to figure out an algorithm to decide on the best direction of movement of the bot based on the data you have.
        # after deciding on the direction, you need to call the direction_callback() function as done in example 1.
if __name__ == '__main__':
    start_obj=PlannerNode()
    start_obj.current_obj.print_root.mainloop()
 
