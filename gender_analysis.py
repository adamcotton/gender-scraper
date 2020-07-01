import numpy as np
import csv
import matplotlib.pyplot as plt
import os.path

#A folder with all data csv files post Gender API was created and analyzed

#Iterate over all years, author types and journal
years = np.arange(2005,2021,1)
types = ['first','corresponding']
journals = ['Cell', 'Nature','Science','ACS_chem_bio','cell_chem_bio','nature_chem_bio', 'angewandte','chemmedchem','EJOC','JACS','JMedChem','JOC','Nature_Chemistry','Org_let','tet_letters','Tetrahedron']


for journal in journals:

	for type in types:

		percents_male = ['male']
		percents_female = ['female']
		year_list = ['year']
		
		for year in years:
			
			#To prevent errors for journals that are newer than 2005
			if os.path.isfile('%s_%s_%s.csv' % (journal, year, type)):
				
				year_list.append(year)
				
				#Open csv
				with open('%s_%s_%s.csv' % (journal, year, type)) as csv_file:

					males = []
					females = []
					
					#Read csv and skip the first line (headers)
					csv_reader = csv.reader(csv_file, delimiter=',')
					next(csv_reader)
					
					#Iterate over each row
					for row in csv_reader:
						
						#If gender API failed to assign a gender then skip entry
						if row[3] == '':
							continue
						
						# If small sample size (100), then unless >= 99% sure of gender, then skip entry,
						#If sure then add to list of males or females
						if int(row[5]) < 100:
							if int(row[4]) >= 99:
								if row[3] == 'female':
									females.append('female')
								if row[3] == 'male':
									males.append('male')
							continue
						
						# If >= 95% sure of gender, then define author as set binary gender
						if row[3] == 'female' and int(row[4]) >=95:
							females.append('female')
							
						if row[3] == 'male' and int(row[4]) >= 95:
							males.append('male')
							
					#Calculate percent male and female and then append to master list
					percent_male = (len(males) / (len(males) + len(females) )) * 100
					percent_female = (len(females) / (len(males) + len(females) )) * 100
		
					percents_male.append(percent_male)
					percents_female.append(percent_female)
		
			# Zip up results into tuple with the percents for each year					
			results = list(zip(year_list, percents_male, percents_female))

			# Save csv file with percents for each journal
			np.savetxt('%s_%s_percents.csv' % (journal, type), results, delimiter=",", fmt='%s')
	
