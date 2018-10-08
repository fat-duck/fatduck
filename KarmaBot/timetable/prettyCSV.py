import csv, datetime

filename = '/timetable/' + datetime.datetime.today().strftime('%Y-%m-%d') + '.csv'
# print(filename)
intakeCode = 'UC2F1805CS'
ignoredModule = ['CT110-3-2-VTC-L', 'CT110-3-2-VTC-LAB', 'CT029-3-2-ISE-L', 'CT029-3-2-ISE-LAB', 'MPU3412-CC2', 'CT050-3-2-WAPP-L', 'CT050-3-2-WAPP-LAB', 'MPU3123-TITAS(LS)', 'MPU3143-BMK2(FS)']

def getTimetable():
	message = ''
	with open("timetable/2018-10-08.csv", newline='') as csv_file:
	    csv_reader = csv.reader(csv_file, delimiter=',')
	    for row in csv_reader:
	    	if (row[1].upper() == intakeCode):
	        	if datetime.datetime.today().strftime('%d-%m-%Y') in row[2]:
	        		if row[6] not in ignoredModule:
	        			message += ('Module Code: ' + row[6] + '\n' + 'Date: ' + row[2] + '\n' + 'Time: ' + row[3] + '\n' + 'Location: ' + row [5] + '\n' + 'Lecturer: ' + row [6] + '\n\n')
	if message != '':
		print('Message sent!')
	return message