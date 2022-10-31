#Enter string composed of the whole HTML of the website
#Parameter ใส่เป็น HTML ของทั้ง Website (String)
def getDownloadURL(HTML_string):
    
    startString = HTML_string.index('xlsx')+4
    endString = startString +(HTML_string[startString:].index('target')-1)

    downloadURL_startIndex = HTML_string[startString:endString].index('http')
    downloadURL_endIndex = HTML_string[startString:endString].index('xlsx')+4
    startEnd_result = HTML_string[startString:endString]
    downloadURL = startEnd_result[downloadURL_startIndex:downloadURL_endIndex]
    #print(f'Printing: {downloadURL}')
    
    return downloadURL.strip()
    
def getDownloadURL_fileName(HTML_string):
    
    startString = HTML_string.index('xlsx')+4
    endString = startString +(HTML_string[startString:].index('target')-1)

    downloadURL_startIndex = HTML_string[startString:endString].index('http')
    downloadURL_endIndex = HTML_string[startString:endString].index('xlsx')+4
    startEnd_result = HTML_string[startString:endString]
    downloadURL = startEnd_result[downloadURL_startIndex:downloadURL_endIndex]
    
    downloadURL_fileName = downloadURL[downloadURL.index('Margin'):(downloadURL.index('xlsx')+4)]
    #print(f'Printing: {downloadURL}')
    
    return downloadURL_fileName.strip()
    

