import csv
import glob


with open(glob.glob("timetable/" + "*.csv")[0], newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(','.join(row))
