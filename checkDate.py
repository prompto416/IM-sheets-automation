
from datetime import datetime 



f = open('htmlSET.txt','r')
htmlSource = f.read()

_TH_ABBR_MONTHS = [
    "ม.ค.",
    "ก.พ.",
    "มี.ค.",
    "เม.ย.",
    "พ.ค.",
    "มิ.ย.",
    "ก.ค.",
    "ส.ค.",
    "ก.ย.",
    "ต.ค.",
    "พ.ย.",
    "ธ.ค.",
]
# คัดวันทีจาก  html webscrape เเล้วก็เทียบกับวันที่วันนี้

def filterDate():
    a = datetime.now()
    years_to_add = a.year + 543
    d1 = a.strftime("%d-%m-%Y")
    d1 = a.replace(year=years_to_add).strftime('%d-%m-%Y')
    currentDate = d1
    a = "วันที่ประกาศ"
    b = "วันที่มีผลบังคับใช้"
    if a and b in htmlSource:
        # print(a,b)
        mid = htmlSource.index(a)
        end = htmlSource.index(b)
    announcedDate = htmlSource[mid+(len(a)):mid+12+13]
    effectiveDate = htmlSource[end+len(b):end+12+20]
    # print(announcedDate)
    # print(effectiveDate)

    for i in _TH_ABBR_MONTHS:
        if i in announcedDate:
            monthToNum = _TH_ABBR_MONTHS.index(i)+1
            announcedDate = announcedDate.replace(i,str(monthToNum))
        if i in effectiveDate:
            monthToNum = _TH_ABBR_MONTHS.index(i)+1
            effectiveDate = effectiveDate.replace(i,str(monthToNum))

    announcedDate =   announcedDate.strip().replace(" ","-")
    effectiveDate = effectiveDate.strip().replace(" ","-")

    return [currentDate,announcedDate,effectiveDate]

def checkDate():
    myDates = filterDate()
    currentDate = myDates[0]
    announcedData = myDates[1]
    effectiveDate = myDates[2]

    #เครื่องหมายมากกว่าเท่ากับจะตรงกันข้ามเพราะ format วันที่เป็น วันเดือนปี ปกติถ้าจะเทียบด้วย logical operator ต้องเป็น เดือนวันปี หรือ ปีเดือนวัน
    if effectiveDate <= currentDate:
        return True 
    else:
        return False
print(filterDate())
print(checkDate())




# วันที่ประกาศ
# วันที่มีผลบังคับใช้