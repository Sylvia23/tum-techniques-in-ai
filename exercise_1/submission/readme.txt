# README.txt

Python Version: 3.7.1

## Solution 1

### Packages used:
- numpy==1.15.4
- heapq

### Implementation details

The task is to find the minimum cost required to reach the goal. There is only
one source, so a single source shortest path algorithm has to be used. The edge
costs are not constant. So BFS will not work here. Dijkstra's single source
shortest path algorithm is the appropriate choice here.

The program starts by finding out the source and the destination cells. Then it
starts exploring the graph from the source cell. The possible moves are defined
by tuples which when added to the current cell gives us the next cell.

Each of the nodes are pushed to a priority queue with the lowest cost node
having the highest priority in the queue. So whenever a node is popped from the
queue, it contains the minimum distance required to reach that node. As a node
is popped, all the valid moves are made from that node to those nodes for which
the minimum cost has not already been calculated. The moves are made by pushing
the next node into the priority queue paired with its distance which we get by
adding the move cost with the current node's distance.

The search ends when we pop the destination node from the queue, or if the queue
becomes empty. When the destination node is popped, the distance that the tuple
contains is the desired output. If the queue becomes empty before finding the
destination, that means the destination is unreachable.


## Solution 2

### Packages used:
- numpy==1.15.4

### Implementation details

The task can be simplified to finding connected components of dots which also
has a node in any of the bordering rows and columns and leaving them as they
are. So the search starts from nodes of each of the four borders. It marks the
adjacent dots and all the dots connected to them as visited. This leaves all the
dots which are surrounded by X as unvisited. A depth first search is used since
it is simple to find connected components with. After this, marking all the
unvisited dots as X produces the expected result.