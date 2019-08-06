import os.path
from xml.etree import ElementTree as ET

a = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
nonXML = []

for j in a:
	for i in a:
		filename = str('data/masters/XML/partition_'+str(j)+str(i))
		save_path = ''
		completeName = os.path.join(save_path, filename)
		try:
			with open(completeName, 'r') as original: data = original.read()
			if (j == "a" and i == "a"):
				with open(completeName, 'a') as modified: modified.write("</masters>")
			elif (j == "u" and i == "s"):
				with open(completeName, 'w') as modified: modified.write("<masters>\n" + data)
			else:

				# if its in xml, add tags
				try:
					with open(completeName, 'w') as modified: modified.write("<masters>\n" + data)
					with open(completeName, 'a') as modified: modified.write("</masters>")
					with open(completeName, 'r') as original: newdata = original.read()
					x = ET.fromstring(newdata)

				# if its not in xml, revert to original
				except Exception:
					with open(completeName, 'w+') as modified: modified.write(data)
					print(completeName+" is not in XML format.")
					nonXML.append(filename)

			print("done with "+completeName)
		except FileNotFoundError:
			done = 0

i = 0
while i < len(nonXML):
	try:
		filename1 = nonXML[i]
		i+=1
		filename2 = nonXML[i]
		with open(filename2, 'r') as original: h2Data = original.read()
		with open(filename1, "a") as myfile:
			myfile.write(h2Data)

		save_path = ''
		completeName = os.path.join(save_path, filename1)

		with open(completeName, 'r') as original: data = original.read()
		with open(completeName, 'w') as modified: modified.write("<masters>\n" + data)
		with open(completeName, 'a') as modified: modified.write("</masters>")
		with open(completeName, 'r') as original: newdata = original.read()
		
		x = ET.fromstring(newdata)
		print(completeName+" is complete")
		os.remove(filename2)
		print(filename2+" has been removed.")
		i+=1
	except Exception:
		i-=1
		filename1 = nonXML[i]
		i+=1
		filename2 = nonXML[i]
		i+=1
		filename3 = nonXML[i]

		readFile = open(filename1)
		lines = readFile.readlines()
		readFile.close()
		w = open(filename1,'w')
		w.writelines([item for item in lines[:-1]])
		w.close()


		with open(filename2, 'r') as original: h2Data = original.read()
		with open(filename3, 'r') as original: h3Data = original.read()
		with open(filename1, "a") as myfile:
			myfile.write(h2Data+h3Data)

		save_path = ''
		completeName = os.path.join(save_path, filename1)

		with open(completeName, 'r') as original: data = original.read()
		# with open(completeName, 'w') as modified: modified.write("<masters>\n" + data)
		with open(completeName, 'a') as modified: modified.write("</masters>")
		with open(completeName, 'r') as original: newdata = original.read()
		
		# x = ET.fromstring(newdata)
		print(completeName+" is complete")
		os.remove(filename2)
		print(filename2+" has been removed.")
		os.remove(filename3)
		print(filename3+" has been removed.")
		i+=1
		# i +=2



