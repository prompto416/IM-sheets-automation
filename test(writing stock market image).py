import gspread
from oauth2client.service_account import ServiceAccountCredentials  
import time

scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('testSheetAPI_Key.json', scope)
client = gspread.authorize(creds)

# python_test = client.open('testSheet').sheet1
Page_IM = client.open('testSheet').worksheet('IM')
Page_Sheet2 = client.open('testSheet').worksheet('Sheet2')

# for i in range(128):
#     if i <= 42: 
#         j = i  
#         k = 0 
#     elif i > 42 and i <= 85: 
#         j = i-43
#         k = 6
#     elif i > 85: 
#         j = i-(43*2)
#         k = 12
        
#     Page_Sheet2.update_cell(2+j,1+k,i+1)
#     if (i!=0) and (i%59)==0:
#             print('Sleeping for a minute')
#             time.sleep(61)
#time.sleep(61)
# for i in range(128):
#     if i <= 42: 
#         j = i  
#         k = 0 
#     elif i > 42 and i <= 85: 
#         j = i-43
#         k = 6
#     elif i > 85: 
#         j = i-(43*2)
#         k = 12
        
#     update_val = Page_IM.cell(2+i,2).value
#     print(j,k,update_val)
#     Page_Sheet2.update_cell(2+j,2+k,update_val)
#     if (i!=0) and (i%59)==0:
#             print('Sleeping for a minute')
#             time.sleep(61)
#time.sleep(61)
Page_Sheet2.update_cell(2+j,4+k,update_val)
quit()
for i in range(128):
    if i <= 42: 
        j = i  
        k = 0 
    elif i > 42 and i <= 85: 
        j = i-43
        k = 6
    elif i > 85: 
        j = i-(43*2)
        k = 12
        
    update_val = Page_IM.cell(2+i,3).value
    print(j,k,update_val)
    Page_Sheet2.update_cell(2+j,3+k,update_val)
    if (i!=0) and (i%59)==0:
            print('Sleeping for a minute')
            time.sleep(61)
time.sleep(61)

for i in range(128):
    if i <= 42: 
        j = i  
        k = 0 
    elif i > 42 and i <= 85: 
        j = i-43
        k = 6
    elif i > 85: 
        j = i-(43*2)
        k = 12
        
    update_val = Page_IM.cell(2+i,4).value
    print(j,k,update_val)
    Page_Sheet2.update_cell(2+j,4+k,update_val)
    if (i!=0) and (i%59)==0:
            print('Sleeping for a minute')
            time.sleep(61)
time.sleep(61)

for i in range(128):
    if i <= 42: 
        j = i  
        k = 0 
    elif i > 42 and i <= 85: 
        j = i-43
        k = 6
    elif i > 85: 
        j = i-(43*2)
        k = 12
        
    update_val = Page_IM.cell(2+i,5).value
    print(j,k,update_val)
    Page_Sheet2.update_cell(2+j,5+k,update_val)
    if (i!=0) and (i%59)==0:
            print('Sleeping for a minute')
            time.sleep(61)