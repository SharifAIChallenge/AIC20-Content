import driver
from state import *
from heapq import heappush, heappop, heapify
import itertools

#you can heuristic function here:
def h(state):
    return sum(abs(b % driver.board_side - g % driver.board_side) + abs(b//driver.board_side - g//driver.board_side)
               for b, g in ((state.index(i), driver.goal_state.index(i)) for i in range(1, driver.board_len)))

def search(start_state):

    global max_frontier_size, goal_node, max_search_depth

    explored, heap, heap_entry, counter = set(), list(), {}, itertools.count()

    key = h(start_state)

    root = State(start_state, None, None, 0, 0, key)

    entry = (key, 0, root)

    heappush(heap, entry)

    heap_entry[root.map] = entry

    while heap:
        #finding best node
        node = heappop(heap)

        explored.add(node[2].map)

        if node[2].state == driver.goal_state:
            driver.goal_node = node[2]
            return heap

        neighbors = driver.expand(node[2])

        #updating neighbors values
        for neighbor in neighbors:

            #calculating values
            neighbor.key = neighbor.cost + h(neighbor.state)

            entry = (neighbor.key, neighbor.move, neighbor)

            if neighbor.map not in explored:

                heappush(heap, entry)

                explored.add(neighbor.map)

                heap_entry[neighbor.map] = entry

                if neighbor.depth > driver.max_search_depth:
                    driver.max_search_depth += 1

            elif neighbor.map in heap_entry and neighbor.key < heap_entry[neighbor.map][2].key:

                hindex = heap.index((heap_entry[neighbor.map][2].key,
                                     heap_entry[neighbor.map][2].move,
                                     heap_entry[neighbor.map][2]))

                heap[int(hindex)] = entry

                heap_entry[neighbor.map] = entry

                heapify(heap)

        if len(heap) > driver.max_frontier_size:
            driver.max_frontier_size = len(heap)
