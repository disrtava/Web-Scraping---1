from bs4 import BeautifulSoup
import requests
import csv

url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

headers = ['name','distance','mass','radius']
star_data = []

page_source = requests.get(url,verify = False)
soup = BeautifulSoup(page_source.content,'html.parser')

collected_data = soup.find_all('table')
# print(collected_data[7])
table_rows = collected_data[7]

# print(collected_data[2].find_all('tr'))

temp_list = []

for row in table_rows.find_all('tr'):
    
     td = row.find_all('td')
     td = [col.text.strip() for col in td]
     
     if len(td) != 0 :
          if td[0]!="":
                temp_list.append(td[0])
          else:
            temp_list.append("")
            
          if td[5]!="":
            temp_list.append(td[5])
          else:
            temp_list.append("")
            
          if td[7]!="":
            temp_list.append(td[7])
          else:
            temp_list.append("")       
     
          if td[8]!="":
            temp_list.append(td[8])
          else:
            temp_list.append("") 

     star_data.append(temp_list)
     temp_list=[]

star_data = star_data[1:]

with open("stars.csv", "w", newline="",encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(star_data)