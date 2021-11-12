adj_list= {
    'A':['B' , 'C'],    'B':['D','E'] ,   'C':['B','F'],    'D':[],    'E':['F'],    'F':[]
    
    
    
}
color ={}
parent={}
traverse_time={}
dfs_traversal_output=[]
for node in adj_list.keys():
    color[node]='w'
    parent[node]=None
    traverse_time[node]=[-1,-1]

for node in adj_list.keys():
    print (node, "->",traverse_time[node])
    
print (color)
print (parent)
print (traverse_time )
