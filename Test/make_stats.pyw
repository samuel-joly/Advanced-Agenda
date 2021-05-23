import os
import matplotlib.pyplot as plt
import time
import numpy as np
'''
TODO
	- Add values on top of bar graph
'''
# Create list with 24 index with len(activity_list)+1 index
def make_day():
	global day, activity_list
	# Create an empty day_list without hour index
	# at the start of the hour line
	width = len(activity_list) + 1
	height = 24
	day = []
	for i in range(height):
		day.append([0]*width)
	# Write hour h at the start of the hour line
	for i, hour in enumerate(day):
		tab = [i]
		for j in activity_list:
			tab.append(0)
		day[i] = tab
# Read all the save_file and save it in day_list
def get_all_save():
	global save_file, save_note, stat_list
	exclude_file = ['advAgenda.pyw','README.md','.git','.gitignore',' all_save.txt', 'test.py','make_stats.py']
	stat_list = [0 for item in activity_list]
	save_file = [x for x in os.listdir('.') if x not in exclude_file]
	width = len(activity_list) + 1
	height = 24
	day_list = [[[0]*width]*height]*len(save_file)
	cumul_list = [0]*int(len(activity_list)+1)

	# For the save file
	for z,file in enumerate(save_file):
		# If it's note a note_save
		if len(file) <= 7:
			# Open it reading mode
			with open(file,'r') as save_files:
				# read all from the third line 
				save_lines = save_files.readlines()[2:]
				# For every line ine the file
				for i, line in enumerate(save_lines):
					# Delete '\n' and ' '
					line = line.replace('\n', '')
					# Convert to list
					line = line.split(' ')
					# delete empty index (might be two in a row)
					if line[-1] == "" and len(line)>1:
						del line[-1]
						if line[-1] == "":
							del line[-1]
					# Save the data in the all_data_list
					day_list[z][i] = line

					for j,value in enumerate(line):
						cumul_list[j] += int(value)

					save = str(day_list[z][i][0])
					if int(save) < 10:
						save = '0'+save
					day_list[z][i][0] = save + '.' + file[:3]



			save_files.close()

		elif len(file) >= 7:
			save_note.append(file)

	stat_list[0] = cumul_list

	local = time.localtime()
	day_find = local.tm_yday

activity_list = ["Cig","Python","Passif","House",\
				"Friend",'Income',"Outcome","Game",\
				'Work','Webdev']

color = ['cyan','blue','red','yellow','green','grey','orange','maroon','black','pink']
timed_activity = [2,3,4,5,8,9,10,11]

save_file = []
save_note = []
make_day()
day_list = get_all_save()

y_pos = np.arange(len(activity_list))
for index,item in enumerate(stat_list):
	if index in timed_activity:
		plt.bar(index-1, stat_list[0][index], align='center', alpha=0.5, color=color[index-1])

plt.xticks(y_pos,activity_list)
plt.ylabel('Usage')
plt.title('AdvAgenda Stats')
plt.show()