from bs4 import BeautifulSoup
import requests
import pysftp

###chcp 1256
#####Variables########
url="https://www.sanarate.ir/"
out_file="sample.txt"
dest_host='44.33.22.11'
dest_user='userrrr'
dest_pass='passss'
dest_dir='/'
######################
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")
tables = soup.find_all('table')
tbl_num = 1

Data = []

listOfStrings = ['EUR' , 'USD']

t_date = soup.find("span", {"id": "MainContent_ViewCashChequeRates_lblCashDay"}).string[14:23].replace("/","")

#print("date,type,code,Buy,Sell")



#if 1==2:
#   cnt = 0
#   for my_table in tables:
#       cnt += 1#
#
#       print ('=============== TABLE {} ==============='.format(cnt))
#       rows = my_table.find_all('tr', recursive=True)           # <-- HERE
#       #print (rows)
#       for row in rows:
#           cells = row.find_all(['th', 'td'], recursive=False)          # <-- HERE
#           print(cells)
#           #for cell in cells:
#              # DO SOMETHING
#               #if cell.string: print (cell.string)


rows = tables[tbl_num].find_all('tr', recursive=True)           # <-- HERE
#print (rows)


for row in rows:
    cells = row.find_all(['th', 'td'], recursive=False)          # <-- HERE
    if cells[1].string in listOfStrings:

        t_buy=cells[2].string.replace(",", "")
        t_sell=cells[3].string.replace(",", "")
        t_type=cells[0].string
        t_code=cells[1].string
        #print(t_date+","+t_type+","+t_code+","+t_buy+","+t_sell)
        Data.append(t_date+","+t_type+","+t_code+","+t_buy+","+t_sell)


with open(out_file, "a") as file_object:
    for mdata in Data:
        file_object.write(mdata+"\n")


srv = pysftp.Connection(host=dest_host, username=dest_user,password=dest_pass,log="pysftp.log")

with srv.cd(dest_dir): #chdir to public
    srv.put(out_file) #upload file to nodejs/

# Closes the connection
srv.close()
