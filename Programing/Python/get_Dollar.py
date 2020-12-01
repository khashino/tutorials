from bs4 import BeautifulSoup
import requests

###chcp 1256

print("Getting Arz Info from \nhttps://www.sanarate.ir/\n")

url="https://www.sanarate.ir/"
html_content = requests.get(url).text

soup = BeautifulSoup(html_content, "lxml")
tables = soup.find_all('table')
tbl_num = 1

listOfStrings = ['EUR' , 'USD']


t_date = soup.find("span", {"id": "MainContent_ViewCashChequeRates_lblCashDay"}).string[14:23].replace("/","")


if 1==2:
    cnt = 0
    for my_table in tables:
        cnt += 1

        print ('=============== TABLE {} ==============='.format(cnt))
        rows = my_table.find_all('tr', recursive=True)           # <-- HERE
        #print (rows)
        for row in rows:
            cells = row.find_all(['th', 'td'], recursive=False)          # <-- HERE
            print(cells)
            #for cell in cells:
                # DO SOMETHING
                #if cell.string: print (cell.string)

print("date,type,code,Buy,Sell")

rows = tables[tbl_num].find_all('tr', recursive=True)           # <-- HERE
#print (rows)
cnt = 0
for row in rows:
    cells = row.find_all(['th', 'td'], recursive=False)          # <-- HERE
    if cells[1].string in listOfStrings:

        t_buy=cells[2].string.replace(",", "")
        t_sell=cells[3].string.replace(",", "")
        t_type=cells[0].string
        t_code=cells[1].string
        print(t_date+","+t_type+","+t_code+","+t_buy+","+t_sell)
    cnt += 1
