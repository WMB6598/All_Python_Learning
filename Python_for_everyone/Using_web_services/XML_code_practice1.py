import xml.etree.ElementTree as ET #This is the built in XML parser

data = '''
<person>
    <name>Will</name>
    <phone type="intl">
        07468512098
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data) #Assigning the whole xml tree to a variable that we can search
print('Name:', tree.find('name').text) #This pulls the name from the xml tree
print('Attr:', tree.find('email').get('hide')) #This checks what hide is set to in the tree