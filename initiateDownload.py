import requests


#initDownloadURL = "https://media.set.or.th/rulebook/regulation/Margin_Announcement_20220531.xlsx"

def initDownload(initDownloadURL):
    req = requests.get(initDownloadURL)

    filename = req.url[initDownloadURL.rfind('/')+1:]

    with open(filename, 'wb') as f:
        for chunk in req.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
