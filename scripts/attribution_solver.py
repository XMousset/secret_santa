import random

from scripts.config import CONFIG

random.seed()


def invalid_exclusions(attributions):
    """Check if 'attributions' respect exclusions requests.

    Parameters
    ----------
    attributions : list of ChristmasFriend
        Single loop of ChristmasFriend in attribution order.
        If n friends in the list, length must be n+1.

    Returns
    -------
    bool
        True if there is an incompatibility. False otherwise.
    """
    for i in range(len(attributions)-1):
        if attributions[i+1].is_excluded_for(attributions[i]):
            return True
    return False


def is_valid(attributions, friends):
    """Process each loop separatly and check if the attributions are valid.

    Parameters
    ----------
    attributions : list of ChristmasFriend
        List of ChristmasFriend in attribution order.
        Can contain multiple loops.
    friends : list of ChristmasFriend
        A unique list containing all the ChristmasFriend objects.

    Returns
    -------
    bool
        False if an error is found, True otherwise.

    Raises
    ------
    ValueError
        If there is a problem with the loops in attributions.
    """
    nb_loop = len(attributions) - len(friends)
    
    if CONFIG["one loop"] and nb_loop != 1:
        return False
    
    attr_loops = []
    current_loop = []
    for friend in attributions:
        current_loop.append(friend)
        if len(current_loop) > 2 and friend == current_loop[0]:
            attr_loops.append(current_loop)
            current_loop = []
    
    if nb_loop != len(attr_loops):
        raise ValueError(
            f"There is a problem in the 'attributions' list :\n{attributions}"
        )
    
    for loop in attr_loops:
        if invalid_exclusions(loop):
            return False
    
    return True


def attribute_friends(friends):
    """Create the 'attributions' list.

    Parameters
    ----------
    friends : list of ChristmasFriend
        A unique list containing all the ChristmasFriend objects.

    Returns
    -------
    list of ChristmasFriend
        A list of Christmas friend in attributions order.
        Friend that start a loop must appear twice in the list
        as they also close the loop.
        (e.g. for a list of 2 loops of 5 friends :
        ['A', 'B', 'C', 'A', 'D', 'E', 'D'])
    """
    attributions = []
    nb_friends = len(friends)
    nb_loops = 0
    new_loop = True
    
    not_choose = friends.copy()
    
    while len(attributions) < nb_friends + nb_loops:
        if new_loop or CONFIG["one loop"]:
            legal_choices = not_choose.copy()
            if len(not_choose) == 0:
                legal_choices.append(start_loop)
        else:
            legal_choices = not_choose.copy()
            legal_choices.append(start_loop)
        
        choice = random.choice(legal_choices)
        attributions.append(choice)
            
        if new_loop:
            nb_loops += 1
            start_loop = choice
            new_loop = False
        
        if choice in not_choose:
            not_choose.remove(choice)
        else:
            new_loop = True
        
    
    return attributions


def find_solution(friends):
    """Generate a valid attribution list.

    Parameters
    ----------
    friends : list of ChristmasFriend
        A unique list containing all the ChristmasFriend objects.

    Returns
    -------
    list of ChristmasFriend
        A list of Christmas friend in attributions order that is valid.
        Friend that start a loop must appear twice in the list
        as they also close the loop.
        (e.g. for a list of 2 loops of 5 friends :
        ['A', 'B', 'C', 'A', 'D', 'E', 'D'])
    int
        The number of iterations done to find a valid solution.

    Raises
    ------
    ValueError
        If too much iterations.
    """
    it = 0
    attributions = []
    while not is_valid(attributions, friends):
        if it >= CONFIG["max iters"]:
            raise ValueError(
                f"Could not find attributions in {it} "
                "iterations."
            )
        attributions = attribute_friends(friends)
        it += 1
    return attributions, it