from bs4 import BeautifulSoup
import requests
import urllib
import csv
import time

# query = 'black pants'
query= str(input("search result="))


# -------------------------------------------- SETTING UP CSV FILE ------------------------------------------

#csv file 
csv_file = open('product_details.csv', 'w')
csv_writer = csv.writer(csv_file, delimiter='\t') 

#headings for csv file 
csv_writer.writerow(['brand', 'name', 'price', 'composition', 'link', 'image'])


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    'Accept-Language': 'en-CA,en-US;q=0.9,en;q=0.8'
}

#--------------------------------------------- H&M prodcuts -----------------------------------------------------
# getting the link from a query
dict_handm={"q":urllib.parse.quote(query)}
r_handm= requests.get('https://www2.hm.com/en_ca/search-results.html?', params=dict_handm)
url_handm = urllib.parse.unquote(r_handm.url)

# creating soup object + getting html code

source_handm= requests.get(url_handm, headers=headers).text
soup_handm= BeautifulSoup(source_handm, 'lxml')

#getting main container where everything is 
main_handm= soup_handm.find('ul', class_='products-listing small')

# looping over list elements + only 10
count=0
for product in main_handm.find_all('li', class_='product-item'):
    
    #only getting first 10 elements 
    if count>= 10:
        break
    count+=1
    
    # making sure to treate errros
    try:
        # the specific info 
        name= product.article.div.a['title']
        price= product.article.find('div', class_='item-details').strong.span.text
        link="https://www2.hm.com" + product.article.div.a['href']
        image= "https:" + product.article.div.a.img['data-src']
        brand= 'H&M'
        # brand= product.article['data-brand']


        #getting composition= would have to go to actual product page
        source_comp= requests.get(link, headers=headers).text
        soup_comp= BeautifulSoup(source_comp, 'lxml')
        t= soup_comp.find('div', id='section-materialsAndSuppliersAccordion')
        composition= [each for each in t.p.text.strip().split(',')]

        try:
            s= "additional: "
            for each in t.find_all('ul')[1].find_all('li'):
                s+= each.text.strip('\n').strip('\t') +", "
            composition.append(s[:-2])
        except:
            pass

        # writing this data to a csv file
        csv_writer.writerow([brand, name, price, composition, link, image])
    except:
        pass
    
    

#---------------------------------------------- ARITZIA products ----------------------------------------------------

#getting link from a query
dict_aritzia={"q":urllib.parse.quote(query)}
r_aritzia= requests.get('https://www.aritzia.com/en/search?', params=dict_aritzia)
url_aritzia = urllib.parse.unquote(r_aritzia.url)

# creating soup object + getting html code
source_aritzia= requests.get(url_aritzia, headers=headers).text
soup_aritzia= BeautifulSoup(source_aritzia, 'lxml')

#getting main container where list is
main_aritzia= soup_aritzia.find('ul', class_='ar-product-grid__container js-product-grid__container list flex flex-wrap justify-between justify-start-ns')

if main_aritzia==None:
    main_aritzia= soup_aritzia.find('ul', class_='ar-product-grid__container js-product-grid__container list flex flex-wrap justify-center-ns justify-center')   
    product_aritzia=main_aritzia.find_all('li', class_='ar-product-grid__tile relative border-box ph1 w-50 w-25-ns')
else:
    product_aritzia=main_aritzia.find_all('li', class_='ar-product-grid__tile js-product-grid__tile js-user-sp relative border-box ph1 w-50 w-25-ns')


#for loop to iterate over list items + making sure to only do 10 products 
count=0
for product in product_aritzia:

    #making sure only do 10 products
    if count>=10:
        break

    count+= 1

    try: 
        # getting specific info from website 
        name= product.a['title'].title()
        price= product.find('span', title='Regular Price').text.strip()
        link=product.a['href']
        image= product.img['data-original']
        brand= 'Aritzia'

        #composition= visiting product page to get materials info
        source_comp= requests.get(link, headers=headers).text
        soup_comp= BeautifulSoup(source_comp, 'lxml')
        
        #getting places where composition is stored
        all_aritizia= soup_comp.find('div', class_='pa3 pv3-ns ph4-ns mv2 mh3-ns')
        c_aritzia= all_aritizia.find_all('div', class_='js-product-accordion__content',recursive=False)[1]

        composition=[]
        for each in c_aritzia.find_all('li'):
            if "%" in each.text:
                composition= [element.strip() for element in each.text.split(':')[1].strip().split(',')]
                break
        
        #writing data to the csv file 
        csv_writer.writerow([brand, name, price, composition, link, image])    
    except:
        count-=1
        pass


# --------------------------------------------------- ARDENE products -----------------------------------------------
#getting link from a query
dict_ardene={"q":urllib.parse.quote(query)}
r_ardene= requests.get('https://www.ardene.com/ca/en/search?', params=dict_ardene)
url_ardene = urllib.parse.unquote(r_ardene.url)



#creating soup object + getting html code
source_ardene= requests.get(url_ardene, headers=headers).text
soup_ardene= BeautifulSoup(source_ardene, 'lxml')


#getting main container where everything is 
main_ardene= soup_ardene.find('ul', id='search-result-items')
product_ardene=main_ardene.find_all('li', class_='grid-tile')

#for loop to iterate over list items + making sure to only do 10 products 
count=0
for product in product_ardene:
    
    #making sure only do 10 products
    if count>=10:
        break
    count+=1

    try: 
        # getting specific info from website 
        name= product.h3.text.strip()
        price= product.find('div', class_='product-pricing').span.p.text.strip()
        link= product.a['href']
        image= product.div.a.find_all('img')[1]['data-src']
        brand= 'Ardene'

        #composition = visiting product page to get materials info
        source_comp= requests.get(link, headers=headers).text
        soup_comp= BeautifulSoup(source_comp, 'lxml')
        c_ardene= soup_comp.find('div', class_='tab-content')
        composition=[]
        for each in c_ardene.find_all('li'):
            if "%" in each.text:
                composition= [element.strip() for element in each.text.strip().split(',')]
                break
        
        #writing data to the csv file 
        csv_writer.writerow([brand, name, price, composition, link, image])

    except:
        pass


# ------------------------------------------------------------------------------------------------------------------------
    

csv_file.close()