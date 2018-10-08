import csv
import glob


def main():
    with open(glob.glob("timetable/" + "*.csv")[0], newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            # print(','.join(row))
            return(','.join(row))
