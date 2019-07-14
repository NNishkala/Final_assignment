#importing libraries
import bs4 as bs
import lxml
import urllib.request
import numpy as np
import pandas as pd

#request and scraping the code
sauce=urllib.request.urlopen('https://karki23.github.io/Weather-Data/Katherine.html')
srccode=bs.BeautifulSoup(sauce,'lxml')
print("Successfully Imported Libraries")
weather=srccode.find('table')
weather_arr=[]

try:
	for row in weather.find_all('tr'):
		cols = row.find_all('th')
		a=[]
		for r in cols:
			a.append(r.text.strip())
		weather_arr.append(a)
		break
except: pass
print("Successfully inserted the first row")

try:
	for row in weather.find_all('tr'):
		cols = row.find_all('td')
		a=[]
		for r in cols:
			a.append(r.text.strip())
		weather_arr.append(a)
except: pass
print("Successfully copied table")

w=[]
for i in weather_arr:
	if(i!=[]):
		w.append(i)
weather_array=np.asarray(w)#above piece of code(36-40) is to remove empty rows
print("Successfully converted to numpy array")
df = pd.DataFrame(weather_array)

#converting to csv file 
df.to_csv('/Users/Admin/machine_learning/summer_io/csv_files/ka.csv')
print("Successfully converted to csv")
