#!/usr/bin/env python
# coding: utf-8

# ### Getting the product links

# ## SCRAPPING LAPTOPS FROM FLIPKART WEBSITE

# In[1]:


## SCRAPPING LAPTOPS FROM FLIPKART WEBSITE

"""  We can scrap a website by parsing the HTML tags. Without using any external libraries such as Selenium or BeautifulSoup,
 it becomes a messy process as we have to extract the required tags manually.
 Here, I have tried to extract the LAPTOPS page from FLIPKART. The required information which I need are the product names
 and the individual product links"""

from html.parser import HTMLParser  #for parsing the HTML tags
import urllib.request
from itertools import chain 
import json   #to make the output readable

url = input("Enter the website: ")
print(" ")

#Import HTML from a URL
url = urllib.request.urlopen(url)
html = url.read().decode()
url.close()
 
class Parse(HTMLParser):
    def __init__(self):
    
        super().__init__()
        self.reset()
  
   # Defining what the method should output when called by HTMLParser.
    
    def handle_starttag(self, tag, attrs):  
     
        global links,names
        
        #GETTING THE PRODUCT NAMES
        global i
        ## Only parse the 'anchor' tag.
        if tag=='img':
            
            try:
                if attrs[1][0] == 'alt':   # names are stored in this tag
                    if i >=24:
                        return
                    
                    names.append(attrs[1][1].split('\n'))
                    i += 1
                    #print(names)
                    
            except Exception as e:
                pass
                
                
        # GETTING THE PRODUCT LINKS   
        global j
        if tag == "a":
            
            try:
                if attrs[0][1] == '_1fQZEK':   # links are stored in this tag
                    if j >=24:
                        return 
                
                    links.append("https://flipkart.com" + attrs[3][1])
                    j += 1
                    #print(links)
                    
            except Exception as e:
                pass
         
        
        
i,j = 0,0
names,links = [],[]    # names and links contain names and url of products respectively
p = Parse()
p.feed(html)
names = list(chain.from_iterable(names))  # converting a 2D list to a 1D list

#### result dictionary to store names of products and their links
result = {names[i]: links[i] for i in range(len(names))}

print("The laptop names and their links are: ")
print("******************************")
print(json.dumps(result, sort_keys=False, indent=4))


# In[ ]:




