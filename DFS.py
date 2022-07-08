graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def dfs(start,state):
	not_visit,visited=list(),list()
	not_visit.append(start)

	while not_visit:
		
		node=not_visit.pop()

		if node not in visited:
			visited.append(node)
			not_visit.extend(state[node])
	return visited;
	