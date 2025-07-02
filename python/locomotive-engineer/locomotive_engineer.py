"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*wagons):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return [*wagons]


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - wagons.
    """
    # Unpack first two items and the rest
    first, second, *rest = each_wagons_id
    
    # Find the index of wagon 1 in the rest
    index_of_one = rest.index(1)
    
    # Use unpacking to combine: rest up to 1, missing wagons, rest after 1, first two items
    return [*rest[:index_of_one + 1], *missing_wagons, *rest[index_of_one + 1:], first, second]


def add_missing_stops(route, **stops):
    """Add missing stops to route dict.
    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    stops_list = list(stops.values())
    route['stops'] = stops_list
    return route    
    


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}  


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    # Transpose the wagons_rows to get columns by color
    # Each column should contain wagons of the same color
    columns = list(zip(*wagons_rows))
    
    # Return the transposed result as a list of lists
    return [list(column) for column in columns]
