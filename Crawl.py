
# coding: utf-8

# In[3]:

#套件區
from lxml import etree  
import requests  
import sys
import pymssql


#SQL區
conn = pymssql.connect("server", "user", "password", "DB")
cursor = conn.cursor()
cursor.execute("  select  *   FROM [Farmdata].[dbo].[JPNEWS] where len(contect)<2" )
row=cursor.fetchall()


for x in row:
    try:
        result = requests.get(x[1])
        result.encoding='utf8'
        root = etree.fromstring(result.content, etree.HTMLParser())
        content='-1'
        content=root.xpath("//div[@id='main']//p[@class='hbody']/text()")
        if len(content)>0:
            cursor.execute("update table set [contect]=  N'%s' where [id]='%s' "
                           %(content[0].replace("'", ""),x[0]) )
            conn.commit()
            print(x[0])
    except ValueError:
        print(ValueError)
 







#套件區
from lxml import etree  
import requests  
import sys
import pymssql
#SQL區
conn = pymssql.connect("server", "user", "password", "DB")
cursor = conn.cursor()
cursor.execute("  select  *   FROM Table" )
row=cursor.fetchall()
#爬蟲區
for x in row:
    try:
        result = requests.get(x[1])
        result.encoding='utf8'
        root = etree.fromstring(result.content, etree.HTMLParser())
        content='-1'
        #Xpath
        content=root.xpath("//div[@id='main']//p[@class='hbody']/text()")
        if len(content)>0:
            cursor.execute("update [Farmdata].[dbo].[JPNEWS] set [contect]=  N'%s' where [id]='%s' "
                           %(content[0].replace("'", ""),x[0]) )
            conn.commit()
            print(x[0])
    except ValueError:
        print(ValueError)
 


#套件區
from lxml import etree

result = requests.get("http://patft.uspto.gov/netacgi/nph-Parser?Sect1=PTO2&Sect2=HITOFF&u=%2Fnetahtml%2FPTO%2Fsearch-adv.htm&r=0&f=S&l=50&d=PTXT&OS=AN%2FSymantec&RS=AN%2FSymantec&Query=AN%2FSymantec&TD=3125&Srch1=Symantec.ASNM.&NextList2=Next+50+Hits")
result.encoding='utf8'
root = etree.fromstring(result.content, etree.HTMLParser())
hrefs = root.xpath(u"//table//tr//td//a")

for href in hrefs:
    if(type(href.text)is str ):
        print (" %s " %(href.attrib))


