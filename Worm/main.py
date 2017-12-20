from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    open('worm-arc1.txt','w').close()
    text = open('worm-arc1.txt','w',encoding='utf8')


    url = 'https://parahumans.wordpress.com/category/stories-arcs-1-10/arc-1-gestation/'
    soup = BeautifulSoup(requests.get(url).content,'html.parser')
    p = soup.find_all('p')
    for line in p:
        print(str(line.string))
        text.write(str(line.string))

    """
    for link in soup.find_all('p'):
        link_str = link.string
        print(link_str)
        text.write(str(link_str))


        string_link = str(link)
        starting_index = string_link.index('>')+1
        ending_index = string_link[starting_index:-1].index('<') - 1
        text.write(string_link[starting_index:ending_index]+"\n\n")
        """
