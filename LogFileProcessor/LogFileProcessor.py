from datetime import date
file_path = 'logininfo.log'
COUNT = 0
with open(file_path, 'r') as file:
    lines = file.readlines()
    if lines.contains(date.today()):
        if lines.contains('ERROR'):
            COUNT += 1
ErrorFile = 'error.txt'
with open(ErrorFile, 'a') as file:
    file.write(f"{date.today()}: {COUNT} errors\n")