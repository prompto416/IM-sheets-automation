from scrape import scrapeHTML_string
from getDownloadURL_Module import *

myHTML = scrapeHTML_string()
downloadURL = getDownloadURL(myHTML)
fileForUpdate = getDownloadURL_fileName(myHTML)
