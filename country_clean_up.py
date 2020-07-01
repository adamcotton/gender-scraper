import numpy as np
import csv

# It was consistent that countries full names were cut up in the scraping program, or only states were given
# For all the very common mistranslations, this script was used to correct them

# Define the year range and file types to be cleaned up
years = np.arange(2006,2021,1)
types = ['solo', 'first', 'corresponding']
journal = 'ACS_Chem_Bio'

for type in types:

	for year in years:
	
		#Open each csv file
		with open('%s_%s_%s.csv' % (journal,year,type), 'r') as csv_file:
	
			#Read the csv file
			reader = csv.reader(csv_file, delimiter=',')
	
			#If common mistranslation found, then replace with correct translation
			temp = []
			for row in reader:	
				counter = 0
				if row[1] == 'Russian':
					temp.append('%s,%s' %(row[0],'Russia'))
					continue
				if row[1] == 'United':
					temp.append('%s,%s' %(row[0],'United Kingdom'))
					continue
				if row[1] == 'Saudi':
					temp.append('%s,%s' %(row[0],'Saudi Arabia'))
					continue
				if row[1] == 'New':
					temp.append('%s,%s' %(row[0],'New Zealand'))
					continue
				if row[1] == 'US.A':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'The':
					temp.append('%s,%s' %(row[0],'Netherlands'))
					continue
				if row[1] == 'the':
					temp.append('%s,%s' %(row[0],'Netherlands'))
					continue
				if row[1] == 'Costa':
					temp.append('%s,%s' %(row[0],'Costa Rica'))	
					continue
				if row[1] == 'Hong':
					temp.append('%s,%s' %(row[0],'Hong Kong'))
					continue
				if row[1] == 'South':
					temp.append('%s,%s' %(row[0],'South Korea'))
					continue
				if row[1] == 'Republic':
					temp.append('%s,%s' %(row[0],'Republic of Korea'))
					continue
				if row[1] == 'PR':
					temp.append('%s,%s' %(row[0],'China'))
					continue
				if row[1] == 'PR.':
					temp.append('%s,%s' %(row[0],'China'))
					continue
				if row[1] == 'P':
					temp.append('%s,%s' %(row[0],'China'))
					continue
				if row[1] == "People's":
					temp.append('%s,%s' %(row[0],'China'))
					continue
				if row[1] == 'Czech':
					temp.append('%s,%s' %(row[0],'Czech Republic'))
					continue
				if row[1] == 'The':
					temp.append('%s,%s' %(row[0],'Netherlands'))
					continue
				if row[1] == 'Puerto':
					temp.append('%s,%s' %(row[0],'Puerto Rico'))
					continue
				if row[1] == 'RO.C':
					temp.append('%s,%s' %(row[0],'Taiwan'))
					continue
				if row[1] == 'AL':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'AK':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'AZ':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'AR':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'CA':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'CO':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'CT':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'DE':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'FL':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'GA':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'HI':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'ID':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'IL':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'IN':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'IA':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'KS':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'KY':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'LA':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'ME':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'MD':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'MA':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'MI':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'MN':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'MS':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'MO':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'MT':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'NE':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'NV':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'NH':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'NJ':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'NM':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'NY':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'NC':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'ND':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'OH':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'OK':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'OR':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'PA':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'RI':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'SC':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'SD':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'TN':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'TX':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'UT':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'VT':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'VA':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'WA':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'WV':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'WI':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'WY':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				
				
				if row[1] == 'Alabama':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Alaska':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Arizona':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Arkansas':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'California':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Colorado':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Connecticut':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Delaware':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Florida':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Georgia':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Hawaii':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Idaho':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Illinois':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Indiana':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Iowa':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Kansas':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Kentucky':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Louisiana':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Maine':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Maryland':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Massachusetts':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Michigan':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Minnesota':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Missippi':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Misouri':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Montana':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Nebraska':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Nevada':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Ohio':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Oklahoma':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Oregon':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Pennsylvania':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Rhode':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Tennessee':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Texas':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Utah':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Vermont':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Virginia':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Washington':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'West':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Wisconsin':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Wyoming':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Boston':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'London':
					temp.append('%s,%s' %(row[0],'United Kingdom'))
					continue
				if row[1] == 'Moscow':
					temp.append('%s,%s' %(row[0],'Russia'))
					continue
				if row[1] == 'Tucson':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Harvard':
					temp.append('%s,%s' %(row[0],'USA'))
					continue
				if row[1] == 'Yale':
					temp.append('%s,%s' %(row[0],'USA'))
					continue	
				if row[1] == 'DC':
					temp.append('%s,%s' %(row[0],'USA'))
					continue	
				
				if row[1] == 'Tel:':
					temp.append('%s,%s' %(row[0],''))
					continue	
				if row[1] == 'Tel':
					temp.append('%s,%s' %(row[0],''))
					continue	
				
				# This is to remove zip/postal codes
				for character in row[1]:
					if character.isdigit():
						counter += 1
				# If exception found, edit the data point in the old csv 
				if counter > 0:	
					temp.append('%s,%s' %(row[0],''))
					continue	
				temp.append('%s,%s' %(row[0],row[1]))

		
		# Export cleaned version of the data
		np.savetxt('Clean/%s_%s_%s.csv' % (journal, year, type), temp, delimiter=",", fmt='%s')