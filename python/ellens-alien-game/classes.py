"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    
    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        Alien.total_aliens_created += 1  # Increment the total number of aliens created
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3

    def hit(self):
        self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other):
        pass

    def __str__(self):
        return f"Alien at ({self.x_coordinate}, {self.y_coordinate})"


# TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.

def new_aliens_collection(coordinates):
    """Create a list of aliens.

    Args:
        coordinates (list of tuples): List of (x, y) coordinates for each alien.

    Returns:
        list: List of Alien objects.
    """
    return [Alien(x, y) for x, y in coordinates]


print(new_aliens_collection([(1, 2), (3, 4), (5, 6)]))