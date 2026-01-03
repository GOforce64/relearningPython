"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*IDs):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    *list_of_IDs, = *IDs,
    return list_of_IDs


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    first, second,number1, *rest = each_wagons_id
    *correct_wagon_list, = number1, *missing_wagons, *rest, first, second 
    return correct_wagon_list


def add_missing_stops(route, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    *list_of_stops, = *stops.values(),
    dict_Stops = {"stops": list_of_stops}
    route_with_stops = {**dict_Stops, **route}
    return route_with_stops


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    combined_data = {**route, **more_route_information}
    return combined_data


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    *corect_order, = zip(*wagons_rows)
    corect_order_list = []
    for this_touple in corect_order:
        corect_order_list.append(list(this_touple))
    return corect_order_list
