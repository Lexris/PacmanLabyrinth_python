def astar_search(game, heuristic=None):
    """
    Expand cheapest node with respect to cost and heuristic.
    """

    from heapq import heappush, heappop

    current_state = game.getStartState()
    action_list = []

    visited = []
    heap = []
    heappush(heap, (0, current_state, action_list))

    while heap and not game.isGoalState(current_state):
        heap_top = heappop(heap)
        current_state, action_list = (heap_top[i] for i in [1, 2])

        if current_state not in visited:
            visited.append(current_state)

        for successor in game.getSuccessors(current_state):
            if successor[0] not in visited:
                heappush(heap, (
                    len(action_list) + 1 + heuristic(successor[0], game), successor[0],
                    action_list + [successor[1]]))

    return action_list
