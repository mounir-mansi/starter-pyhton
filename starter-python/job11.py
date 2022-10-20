from xml.dom import minidom
doc = minidom.parse("domains.xml") 
#.parse sert à parcourir le document
elements = doc.getElementsByTagName("column")
newList = []

for i in elements :
    if i.getAttribute("name") == "domain" :
        newList.append(i.childNodes[0].data)

print(len(newList))


