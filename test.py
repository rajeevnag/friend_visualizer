

def write_connections(friend_connections):
    import json
    breakpoint() 
    with open('mutual_connections.txt','w') as file:
        json.dump(friend_connections,file)

    with open('mutual_connections.txt','r') as infile:
        new_data = json.load(infile)
    
    breakpoint()
    x = 5

friend_connections  = dict()

api_counter = 0
friends = ['goodbeanalt','CrypticNoOne']
for friend in friends:
    with open('direct_connections.txt','r+') as file:
        connections = file.readlines()
        current_connections = list()
        

        for connection in connections:
            connection = connection.replace('\n','')
            if connection in friends and connection not in current_connections:
                current_connections.append(connection) 

        
        friend_connections[friend] = current_connections
        x = 5



write_connections(friend_connections)

