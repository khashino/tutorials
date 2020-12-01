from bs4 import BeautifulSoup
import requests
import pysftp
import xml.etree.ElementTree as xml


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
        element = t_date+","+t_code+","+t_type+","+t_buy+","+t_sell
        Data.append(element)

################XML####################

tree = xml.parse(out_file)

xmlRoot = tree.getroot()
exchangerate = xmlRoot.find('exchangerate')

#child.append(child)

for mdata in Data:
    child = xml.SubElement(exchangerate,"row")
    xdate = xml.SubElement(child,"date")
    xdate.text = mdata.split(",")[0]
    xcode = xml.SubElement(child,"code")
    xcode.text = mdata.split(",")[1]
    xname = xml.SubElement(child,"name")
    xname.text = mdata.split(",")[2]
    xbuy = xml.SubElement(child,"buy")
    xbuy.text = mdata.split(",")[3]
    xsell = xml.SubElement(child,"sell")
    xsell.text = mdata.split(",")[4]


tree.write(out_file)

#######################################

#################File#################
#with open(out_file, "a") as file_object:
#    for mdata in Data:
#        file_object.write(mdata+"\n")
######################################

################SFTP###################

#srv = pysftp.Connection(host=dest_host, username=dest_user,password=dest_pass,log="pysftp.log")

#with srv.cd(dest_dir): #chdir to public
#    srv.put(out_file) #upload file to nodejs/

# Closes the connection
#srv.close()
#########################################
