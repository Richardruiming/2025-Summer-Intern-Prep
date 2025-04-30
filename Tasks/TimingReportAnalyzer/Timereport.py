import numpy as np
class path:
    def __init__(self, Startpoint, Endpoint, Path_Group, Path_Type, slack):
        self.Startpoint = Startpoint
        self.Endpoint = Endpoint
        self.Path_Group = Path_Group
        self.Path_Type = Path_Type
        self.slack = slack

def insertion(arr, slack):
    temp = slack
    for i in range(len(arr)):
        if arr[i] > temp:
            temp2 = arr[i]
            arr[i] = temp
            temp = temp2
    return temp

file = 'timing.rpt'
with open(file, 'r') as f:
    lines = f.readlines()
    dict = {}
    error = 0
    smallest = np.array([0,0,0,0,0])
    for i in range(len(lines)):
        if 'Startpoint' in lines[i] and int(lines[i+4].split( )[1].strip()) < 0:
            error += 1
            slack = int(lines[i+4].split( )[1].strip())
            if slack <= smallest[4]:
                Startpoint = lines[i].split(':')[1].strip()
                Endpoint = lines[i+1].split(':')[1].strip()
                Path_Group = lines[i+2].split(':')[1].strip()
                Path_Type = lines[i+3].split(':')[1].strip()
                if slack < smallest[4]:
                    temp = insertion(smallest, slack)
                    dict[slack] = path(Startpoint, Endpoint, Path_Group, Path_Type, slack)
                    del dict[temp]
                
    