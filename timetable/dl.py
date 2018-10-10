import requests
import zipfile
import os
import glob


def main():
    url = "http://lms.apiit.edu.my/intake-timetable/download_timetable/timetableCSV.zip"
    print("Downloading . . . . . . . .")

    r = requests.get(url)

    with open("timetable/timetableCSV.zip", "wb") as f:
        print("Writing timetableCSV.zip. . . . . .")
        f.write(r.content)

    with zipfile.ZipFile("timetable/timetableCSV.zip", "r") as unzip:
        print("Unzipping timetableCSV.zip. . . . . . .")
        unzip.extractall("timetable/")
        print("Unzipping completed")
        os.remove("timetable/timetableCSV.zip")
        print("Deleting zip")
        os.rename(glob.glob("timetable/" + "*.csv")[0], "tt.csv")

# For testing only. Use from scheduler.py in production


# main()
