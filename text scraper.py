
#!/usr/bin/python
from bs4 import BeautifulSoup as bs
import os
import cfscrape

# website with model images
url = 'https://www.reddit.com'

scraper = cfscrape.create_scraper()

# download page for parsing
page = scraper.get(url)
#the print(page) below tells you whether you successfully
#reached the url. Some sites won't allow you to scrape their site,
#and you'll receive something like a 503. A 404 error could indicate
#a typo in the url above. A 200 means success. That's what you want.
print(page)
soup = bs(page.text, 'html.parser')

# locate all elements with image tag
h2_tags = soup.findAll('h2')
for x in h2_tags:
    print(x)
#print(h2_tags)

# create directory for model images
#if not os.path.exists('images'):
    #os.makedirs('images')

# move to new directory
#os.chdir('images')

# image file name variable
#x = 0

# writing images
#for image in image_tags:
 #   try:
  #      url = image['src']
   #     response = scraper.get(url)
    #    if response.status_code == 200:
     #       with open('images-' + str(x) + '.jpg', 'wb') as f:
      #          f.write(scraper.get(url).content)
       #         f.close()
        #        x += 1
    #except:
     #   pass






