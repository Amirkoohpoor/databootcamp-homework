#!/usr/bin/env python
# coding: utf-8

# In[2]:


#from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


# In[3]:


url = 'https://mars.nasa.gov/news/'
response = requests.get(url)
soup = bs(response.text, 'html.parser')
print(soup.prettify())


# In[32]:


results = soup.find_all('div', class_="content_title")
results_p = soup.find_all('div', class_="rollover_description_inner")
titles = results[0].a.text
explain = results_p[0].text
print(titles)
print(explain)

# In[34]:


from splinter import Browser
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)


# In[36]:


html = browser.html
soup = bs(html,"lxml")
print(soup.prettify())


# In[57]:


img = soup.find_all('img', class_="thumb")
img_link = "https://www.jpl.nasa.gov"+img[0]["src"]
print(img_link)


# In[58]:


url2 = "https://twitter.com/marswxreport?lang=en"
browser.visit(url2)
html = browser.html
soup = bs(html,"lxml")
print(soup.prettify())


# In[64]:


weather = soup.find_all('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
mars_weather = weather[0].text
print(mars_weather)


# In[73]:


df = pd.read_html("https://space-facts.com/mars/")
df[0]


# In[85]:


url3 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
browser.visit(url3)
html = browser.html
soup = bs(html,"lxml")
#print(soup.prettify())
img_cerberus = soup.find_all('img', class_="wide-image")
img_cerberus_link = "https://astrogeology.usgs.gov/"+img_cerberus[0]["src"]
print(img_cerberus_link)


# In[86]:


url4 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
browser.visit(url4)
html = browser.html
soup = bs(html,"lxml")
#print(soup.prettify())
img_schiaparelli = soup.find_all('img', class_="wide-image")
img_schiaparelli_link = "https://astrogeology.usgs.gov/"+img_schiaparelli[0]["src"]
print(img_schiaparelli_link)


# In[87]:


url5 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
browser.visit(url5)
html = browser.html
soup = bs(html,"lxml")
#print(soup.prettify())
img_syrtis = soup.find_all('img', class_="wide-image")
img_syrtis_link = "https://astrogeology.usgs.gov/"+img_syrtis[0]["src"]
print(img_syrtis_link)


# In[88]:


url6 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
browser.visit(url6)
html = browser.html
soup = bs(html,"lxml")
#print(soup.prettify())
img_valles = soup.find_all('img', class_="wide-image")
img_valles_link = "https://astrogeology.usgs.gov/"+img_valles[0]["src"]
print(img_valles_link)


# In[89]:


hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov//cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov//cache/images/cfa62af2557222a02478f1fcd781d445_cerberus_enhanced.tif_full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov//cache/images/3cdd1cbf5e0813bba925c9030d13b62e_schiaparelli_enhanced.tif_full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov//cache/images/ae209b4e408bb6c3e67b6af38168cf28_syrtis_major_enhanced.tif_full.jpg"},
]


# In[ ]:
def scrape():
    urls = {"title":titles, "more explanation":explain, "current Featured Mars Image":img_link,
        "Mars Weather":mars_weather, "Mars Facts":df[0],"Mars Hemispheres":hemisphere_image_urls}




# In[ ]:




