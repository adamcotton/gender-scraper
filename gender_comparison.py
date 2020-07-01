import numpy as np
import csv
import matplotlib.pyplot as plt
import os.path

#A folder with all data csv files post Gender API was created and analyzed

#Iterate over all years and journal

years = np.arange(2005,2021,1)

journals = ['Cell', 'Nature','Science','ACS_chem_bio','cell_chem_bio','nature_chem_bio', 'angewandte','chemmedchem','EJOC','JACS','JMedChem','JOC','Nature_Chemistry','Org_let','tet_letters','Tetrahedron']

# Iterate over each journal
for journal in journals:

	percents_male = []
	percents_female = []
	percents_unsure = []

	first_genders = [] 
	corresponding_genders = []
	year_lists = []
	year_data = []
	
	for year in years:
		
		#To prevent error is journal is newer than 2005
		if os.path.isfile('%s_%s_first.csv' % (journal, year)):

			year_data.append(year)
			
			#Open list of first names for first authors
			with open('%s_%s_first.csv' % (journal, year)) as csv_file:

				first_gender = []
				year_list = []
				
				#Read csv file and skip top row (headers)
				csv_reader = csv.reader(csv_file, delimiter=',')
				next(csv_reader)
						
				#For each row, append the year
				for row in csv_reader:
					
					year_list.append(year)
					
					#If gener API couldn't assign gender, append blank
					if row[3] == '':
						first_gender.append('')
				
					# If small sample size (100), then unless >= 99% sure of gender, then append blank,
					#If sure then append gender
					elif int(row[5]) < 100:
						if int(row[4]) >= 99:
							first_gender.append(row[3])
						else:
							first_gender.append('')
					
					# If >=95% sure of gender then append gender, otherwise append blank
					elif int(row[4]) >=95:
						first_gender.append(row[3])
						
					elif int(row[4]) <=95:
						first_gender.append('')		
					
			# Append year and gender of first author								
			year_lists.append(year_list)
			first_genders.append(first_gender)
			
			#Open list of first names for corresponding authors
			with open('%s_%s_corresponding.csv' % (journal, year)) as csv_file:
	
				corresponding_gender = []
				
				#Read csv file and skip first row (headers)
				csv_reader = csv.reader(csv_file, delimiter=',')
				next(csv_reader)
	
				#Fo each row
				for row in csv_reader:
					
					#If gener API couldn't assign gender, append blank
					if row[3] == '':
						corresponding_gender.append('')
					
					# If small sample size (100), then unless >= 99% sure of gender, then append blank,
					#If sure then append gender
					elif int(row[5]) < 100:
						if int(row[4]) >= 99:
							corresponding_gender.append(row[3])
						else:
							corresponding_gender.append('')
					
					# If >=95% sure of gender then append gender, otherwise append blank
					elif int(row[4]) >=95:
						corresponding_gender.append(row[3])
						
					elif int(row[4]) <=95:
						corresponding_gender.append('')		
		
			# Append gender of corresponding author
			corresponding_genders.append(corresponding_gender)
	
	year_list_array = []
	first_list_array = []
	corresponding_list_array = []

	#create new array with each year
	for x in year_lists:
		year_list_array += x

	#create new array of first author genders
	for x in first_genders:
		first_list_array += x
	
	#create new array of corresponding author genders
	for x in corresponding_genders:
		corresponding_list_array += x
	
	#Create tuple of year, first author gender and corresponding gender
	gender_comparison = list(zip(year_list_array, first_list_array, corresponding_list_array))
	
	#Define the 4 possible outcomes of defined genders
	male_male_list = []
	male_female_list = []
	female_male_list = []
	female_female_list = []
	
	#for each year
	for year in year_data:
	
		female_male = []
		female_female = []
		male_male = []
		male_female = []
	
		#Iterate over tuple of years and genders
		for paper in gender_comparison:
			if paper[0] == year:
				# Compare the genders of firt and corresponding authors and append to corresponding arrays
				if paper[2] == 'male' and paper[1] == 'male':
					male_male.append(paper[1])
				if paper[2] == 'male' and paper[1] == 'female':
					male_female.append(paper[1])
				if paper[2] == 'female' and paper[1] == 'male':
					female_male.append(paper[1])
				if paper[2] == 'female' and paper[1] == 'female':
					female_female.append(paper[1])
		
		#Occasionally for some journal years, there were no female corresponding authors with female first authors, if thats the case, define percentage as blank
		if (len(female_male)+len(female_female)) == 0:
			female_male_percent = ''
			female_female_percent = ''

		#Make sures not to fail, see above line 151
		elif (len(male_male)+len(male_female)) == 0:
			male_male_percent = ''
			male_female_percent =''

		# Calculate percentages of gender breakdown of first authors given a set gender of corresponding author
		else:	
			male_male_percent = (len(male_male) / (len(male_male) + len(male_female))) *100
			male_female_percent = (len(male_female) / (len(male_male) + len(male_female))) *100
			female_male_percent = (len(female_male) / (len(female_male) + len(female_female))) *100
			female_female_percent = (len(female_female) / (len(female_male) + len(female_female))) *100
		
		#Create lists of percentages
		male_male_list.append(male_male_percent)
		male_female_list.append(male_female_percent)
		female_male_list.append(female_male_percent)
		female_female_list.append(female_female_percent)
		
		#Zip into list year and percentage of male or female first authors for each gender of corresponding author
		male_corresponding = list(zip(year_data, male_male_list, male_female_list))
		female_corresponding = list(zip(year_data, female_male_list, female_female_list))
		
		#Export csv file for each above list
		np.savetxt('%s_male_corresponding.csv' % journal, male_corresponding, delimiter=",", fmt='%s')
		np.savetxt('%s_female_corresponding.csv' % journal, female_corresponding, delimiter=",", fmt='%s')
	



