from bs4 import BeautifulSoup

# This is the html document whose information we need
html = '<!DOCTYPEhtml><html><head><title>Randomtrials</title></head><body><h2>Thisisarandomheading</h2><p>Thisisarandomparagraph</p><h2>Cowsslocation</h2><p>Bwaise</p><h2>Heptiseslocation</h2><p>Matigga</p><h2>Ssalislocation</h2><p>Kampala</p><h2>Lilislocation</h2><p>Ganacur</p><h2>JDNSIXNslocation</h2><p>JJOWMDL</p><h2>Joshuaslocation</h2><p>Bahamas</p></body></html>'

# Creates an object of the class BeautifulSoup 
soup = BeautifulSoup(html, 'html.parser')

# Find all enable us to get all the details from the specified tags which I have shown
table_details = soup.find_all(name = 'h2')

# print(table_details)

# Loop that prints out the text from the specified tag
for x in table_details:
    print(x.text)