import heapq  

def dijkstra(graph, start,finish):
  value={node:float('inf') for node in graph}
  value[start]=0
  queue = []
  heapq.heappush(queue, [value[start], start]) 
  while queue:  
    cost, name = heapq.heappop(queue)  
    for new_name, new_value in graph[name].items():
      sum = cost + new_value  
      if value[new_name]>sum: 
        value[new_name] = sum
        heapq.heappush(queue, [sum, new_name])
    # if name==finish:break

  return value

graph = {
   'A':{'B':9,'C':2},
	'B':{'D':3,'A':9,'C':6,'E':1},
	'C':{'A':2,'B':6,'F':9,'D':2},
	'D':{'C':2,'B':3,'E':5,'F':6},
	'E':{'B':1,'D':5,'F':3,'G':7},
	'F':{'D':6,'E':3,'G':4,'C':9},
	'G':{'E':7,'F':4}
}

print(dijkstra(graph, 'A','G'))