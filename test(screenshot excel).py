import pyscreenshot

# im=pyscreenshot.grab(bbox=(x1,x2,y1,y2))
image = pyscreenshot.grab(bbox=(90, 240, 1500, 485))

# To view the screenshot
image.show()

# To save the screenshot 
image.save("screenshot_google_sheet_rows.png")