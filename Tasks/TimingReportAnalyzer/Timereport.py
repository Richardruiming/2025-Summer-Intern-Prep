#!/usr/bin/env python3
class Path:
    def __init__(self, Startpoint, Endpoint, Path_Group, Path_Type, slack):
        self.Startpoint = Startpoint
        self.Endpoint = Endpoint
        self.Path_Group = Path_Group
        self.Path_Type = Path_Type
        self.slack = slack

file = 'large_timing.rpt'
with open(file, 'r') as f:
    lines = f.readlines()
    error = 0
    worst_paths = []
    for i in range(len(lines)):
        if 'Startpoint' in lines[i] and float(lines[i+4].split(' ')[1].strip()) < 0:
            error += 1
            slack = float(lines[i+4].split(' ')[1].strip())
            if slack < 0:
                Startpoint = lines[i].split(':')[1].strip()
                Endpoint = lines[i+1].split(':')[1].strip()
                Path_Group = lines[i+2].split(':')[1].strip()
                Path_Type = lines[i+3].split(':')[1].strip()
                worst_paths.append(Path(Startpoint, Endpoint, Path_Group, Path_Type, slack))
    sorted_slack = sorted(worst_paths, key=lambda x: x.slack)
    if len(sorted_slack) > 5:
        firth = sorted_slack[4].slack
        sorted_slack = [i for i in sorted_slack if i.slack <= firth]
    worst_paths = sorted_slack
refile = 'return.rpt'
with open(refile,'w') as f:
    f.write('There are ' + str(error) + ' paths with negative slack.\n')
    f.write('The following 5 paths have the most negative slack:\n')
    for i in worst_paths:
        f.write('Startpoint: ' + i.Startpoint + '\n')
        f.write('Endpoint: ' + i.Endpoint + '\n')
        f.write('Path Group: ' + i.Path_Group + '\n')
        f.write('Path Type: ' + i.Path_Type + '\n')
        f.write('Slack: ' + str(i.slack) + '\n\n')
