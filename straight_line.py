'''program to check if the given co-ordinates form a straight line
'''
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        x1 = coordinates[0][0]
        y1 = coordinates[0][1]
        try:
            slope = (x1-coordinates[1][0])/(y1-coordinates[1][1])
            intercept  = y1 - slope*x1
        
            for xn,yn in coordinates[2:]:
                if((slope != (x1-xn)/(y1-yn)) or (intercept != yn-slope*xn)):
                    return False
        
            else:
                return True
        except ZeroDivisionError:
                for xn,yn in coordinates[2:]:
                    if yn != y1:
                        return False
                else:
                    return True
