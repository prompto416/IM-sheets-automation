from parinya import LINE 
#your api token

line = LINE('')

line.sendtext('Sheet updated')


# import requests

# url = 'https://notify-api.line.me/api/notify'
#your token
# token = ''
# headers = {
#             'content-type':
#             'application/x-www-form-urlencoded',
#             'Authorization':'Bearer '+token
#            }
# imageurl = 'https://media.discordapp.net/attachments/938633479950827520/1014175836242464891/unknown.png'
# while True:
#     msg = input("Enter your name:")
#     r = requests.post(url, headers=headers , data = {'message':" ",'imageThumbnail':imageurl,'imageFullsize':imageurl}
# )
#     # r = requests.post(url, headers=headers , data = {'message':msg})
#     print(r.text)