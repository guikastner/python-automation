import xml.etree.ElementTree as ET

file_path = "groceries.xml"

tree = ET.parse(file_path)
root = tree.getroot()

items_over6 = []
print(items_over6)

for item in root.findall("grocery_item"):
    name = item.find("name").text
    price = item.find("price").text
    if float(price) > 6:
        items_over6.append(name)
    #print(name, price)