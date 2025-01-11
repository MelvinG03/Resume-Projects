class Car:
    
    """ A class to represet the car

    Defining features:
        x (integer): X position (coordinate) of the car
        y (integer): Y position (coordinate) of the car
        heading (string): Which direction the car is facing ('n', 'e', 's', 'w').

    Methods:
        turn(direction) (string): Turns the car left or right, to change the heading
        drive(distance=1) (integer): Moves the car in the chosen direction by a set integer value
        status() (string): The current position and heading of the car """

    def __init__(self):

        """Setting the car at the position (0,0) on the coordinate map and facing the car north"""

        self.x = 0
        self.y = 0
        self.heading = 'n'

    def turn(self, direction):
        
        """ Using if statements to determine where the car is going to face after turning

        Directions:
            direction (string): Gets input to turn the car left or right, ('l' or 'r')

        Change:
            Changes the direction that the car is facing """
        
        if self.heading == 'n':
            if direction == 'l':
                self.heading = 'w'
            elif direction == 'r':
                self.heading = 'e'
        elif self.heading == 'e':
            if direction == 'l':
                self.heading = 'n'
            elif direction == 'r':
                self.heading = 's'
        elif self.heading == 'w':
            if direction == 'l':
                self.heading = 's'
            elif direction == 'r':
                self.heading = 'n'
        elif self.heading == 's':
            if direction == 'l':
                self.heading = 'e'
            elif direction == 'r':
                self.heading = 'w'
        

    def drive(self, distance=1):
        
        """ Moving (driving) the car forwards

        Direction:
            distance (integer): The distance to move forwards in

        Change:
            Changes the Y (north or south) and X (east or west) positions """
        
        if self.heading == 'n':
            self.y += distance
        elif self.heading == 's':
            self.y -= distance
        elif self.heading == 'e':
            self.x += distance
        elif self.heading == 'w':
            self.x -= distance

    def status(self):
        
        """ Printing the final position and heading of the car

        Result:
            Prints output """
        
        print(f"Coordinates: ({self.x}, {self.y})")
        print(f"Heading: {self.heading}")

# Example usage
def main():
    c = Car()
    c.turn('l')
    c.drive(10)
    c.turn('l')
    c.drive()
    c.status()
    assert c.x == -10
    assert c.y == -1
    assert c.heading == 's'

if __name__ == "__main__":
    main()
