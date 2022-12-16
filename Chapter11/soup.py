import urllib.request, urllib.parse, urllib.error
import collections
collections.Callable = collections.abc.Callable
from BeautifulSoup import bs4
import ssl
url =  'http://py4e-data.dr-chuck.net/comments_42.html'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = bs4.soup('a')
def main():

    
    for tag in tags:
     # Look at the parts of a tag
        print('TAG:',tag)
        print('URL:',tag.get('href', None))
        print('Contents:',tag.contents[0])
        print('Attrs:',tag.attrs)








main()