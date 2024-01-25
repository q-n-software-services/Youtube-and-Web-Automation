import requests

url = 'https://ils.unc.edu/cws/Handouts/Computer%20Basics/Computer%20Basics.pdf'
print(url)
r = requests.get(url)
with open('newFile.pdf', "wb") as f:
    f.write(r.content)
print("done")
