"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    current_cart = {}
    for item in notes:
        current_cart[item] = 1
    return current_cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: tuple - tuple of (recipe_name, recipe_dict) tuples with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    for recipe_name, recipe_dict in recipe_updates:
        ideas[recipe_name] = recipe_dict
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return {k: v for k, v in sorted(cart.items())}


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment_cart = {}
    for item, quantity in cart.items():
        if item in aisle_mapping:
            aisle_info = aisle_mapping[item]
            fulfillment_cart[item] = [quantity] + aisle_info
    
    # Sort in reverse alphabetical order by item name
    sorted_items = sorted(fulfillment_cart.items(), reverse=True)
    return dict(sorted_items)


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment_cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for item in fulfillment_cart:
        if item in store_inventory:
            current_quantity = store_inventory[item][0]
            requested_quantity = fulfillment_cart[item][0]
            
            if isinstance(current_quantity, int):
                new_quantity = current_quantity - requested_quantity
                if new_quantity <= 0:
                    store_inventory[item][0] = "Out of Stock"
                else:
                    store_inventory[item][0] = new_quantity
    return store_inventory