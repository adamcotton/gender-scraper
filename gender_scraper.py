import requests
import pprint
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import json
from urllib.request import urlopen


#Function to scrape data from the web

# Define which journal you want to search: Note, for science you must have the check abstract list is not null to prevent pulling down articles
journal = 'Science'

# Define data range
years = np.arange(2015,2021,1)

#Iterate over each year
for year in years:
	
	# Define arrays
	all_authors = []
	last_authors = []
	first_authors = []
	solo_authors = []
	solo_authors_temp = []
	author_country = []
	solo_country = ['Country']
	last_country = ['Country']
	first_country = ['Country']

	# For each page in the pubmed search
	for page in np.arange(1,14,1):
		
		#URL used for searching
		url = ('https://pubmed.ncbi.nlm.nih.gov/?term="Science"%%5BJournal%%5D&filter=years.%s-%s&format=abstract&sort=date&size=200&page=%s' % (year,year,page))

		# Define the url request
		page = requests.get(url)
		
		#Use beautiful soup to fetch the html
		soup = BeautifulSoup(page.content, 'html.parser')
		
		#Return everything under main content
		results = soup.find(id='search-page')

		#Find all the papers that URL search returns
		papers = results.find_all('div', class_='results-article')
		
		# for each paper
		for paper in papers:
			
			# Search html and find list of countries and abstract list
			paper_list = paper.find('div', class_='full-view')
			
			country_list = paper_list.find_all('div', class_='affiliations')
			
			abstract_list = paper.find('div', class_='abstract')
	
			# Continue if exceptions found - for science this eliminates non research articles
			if abstract_list == None:
				continue
				
			if country_list == []:
				continue
			
			# For each country in each list, find final country referenced
			for country in country_list: 
					
				# Find country in the html	
				country_elem = country.find('ul', class_='item-list')
				
				#Convert to a string 
				country_ls = str((country_elem.text.strip())).split(',')
				
				#Clean up string
				author_country.append(country_ls[-1][:-1])	
				
				#Define last country with cleaned up scars
				new_country = country_ls[-1][:-1].split(' ')
				
				# Some results return email addresses (mainly older papers) so remove if the case
				#Occasionally there is a period at the end of the country, remove if the case
				for element in new_country:
					if '@' in element:
						new_country.remove(element)	
					if '.' in element:	
						if len(new_country) > 1:
							new_country[1] = new_country[1].replace('.','',1)
					
			paper_authors = []
	
			# Find the author list for each paper
			author_list = paper_list.find_all('div', class_='authors-list')
	
			#Iterate through the authors
			for author in author_list:
	
				#Find the text for each author on the paper
				author_list = paper.find_all('span', class_='authors-list-item')
	
				# Due to html, must parse twice
				for author in author_list:
		
					#Find each author
					author_elem = author.find('a', class_='full-name')
	
					#If no authors, continue
					if author_elem == None:
						continue
			
					#Clean up html 
					authors = (author_elem.text.strip())
					
					# Append authors to the author list for each paper
					paper_authors.append(authors)
			
					all_authors.append(authors)
			
			# Find out if its a solo author and define as such if so
			if len(paper_authors) == 1:
				solo_authors.append(paper_authors[0])
				if len(new_country) > 1:
					solo_country.append(new_country[1])
		
			# If more than 1 author, append first and last author and the authors country
			if len(paper_authors) > 1:
				last_authors.append(paper_authors[-1]), first_authors.append(paper_authors[0])
				if len(new_country) > 1:
					last_country.append(new_country[1]), first_country.append(new_country[1])
	
	#Define arrays
	first_author_first_name = ['First Name']
	corresponding_name = []
	corresponding_first_name = ['First Name']
	solo_name = []
	solo_first_name = ['First Name']

	# split each name to first and last names
	for author in first_authors:
		first_author_name.append(author.split())
	
	# Now just take the first name
	for author_name in first_author_name:
		first_author_first_name.append(author_name[0])

	# split each name to first and last names 
	for author in last_authors:
		corresponding_name.append(author.split())

	# Now just take the first name
	for author_name in corresponding_name:
		corresponding_first_name.append(author_name[0])

	# split each name to first and last names 
	for author in solo_authors:
		solo_name.append(author.split())

	# Now just take the first name
	for author_name in solo_name:
		solo_first_name.append(author_name[0])

	#Zip into tuples a list of first names and their country
	solo_authors_country = list(zip(solo_first_name,solo_country))
	last_authors_country = list(zip(corresponding_first_name,last_country))
	first_authors_country = list(zip(first_author_first_name, first_country))

	#Export csv files with the above tuples 
	np.savetxt('Data/Science/%s_%s_first.csv' % (journal, year), first_authors_country, delimiter=",", fmt='%s')
	np.savetxt('Data/Science/%s_%s_corresponding.csv' % (journal, year), last_authors_country, delimiter=",", fmt='%s')
	np.savetxt('Data/Science/%s_%s_solo.csv' % (journal, year), solo_authors_country, delimiter=",", fmt='%s')

