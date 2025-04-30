from datetime import date
file_path = 'SampleLogFile.log'
COUNT = 0
with open(file_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line)
        if str(date.today()) in line and 'ERROR' in line:
            COUNT += 1
ErrorFile = 'error.txt'
with open(ErrorFile, 'a') as file:
    file.write(f"{date.today()}: {COUNT} errors\n")
