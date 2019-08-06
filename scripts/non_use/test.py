
import os.path
from xml.etree import ElementTree as ET

filename1 = "h1.txt"
filename2 = "h2.txt"
with open(filename2, 'r') as original: h2Data = original.read()
with open(filename1, "a") as myfile:
	myfile.write(h2Data)


save_path = ''
completeName = os.path.join(save_path, filename1)

with open(completeName, 'r') as original: data = original.read()
with open(completeName, 'w') as modified: modified.write("<masters>\n" + data)
with open(completeName, 'a') as modified: modified.write("</masters>")
with open(completeName, 'r') as original: newdata = original.read()
print(newdata)

x = ET.fromstring(newdata)