import re

from bs4 import BeautifulSoup
import requests
import csv
import wikipedia as w

def get_wikipedia_pages_and_links(wiki_link_to_scrape):
    res = requests.get(wiki_link_to_scrape).text
    wiki_link = 'https://en.wikipedia.org'

    soup = BeautifulSoup(res, "html.parser")
    div_instances = soup.find('div', class_='mw-parser-output')
    a_instances = div_instances.find_all('a')

    titles = []
    lst_links = []
    for link in a_instances:
        url = link.get('href', '')
        if "/wiki/" in url:
            titles.append(link.text.strip())
            lst_links.append(wiki_link + ''.join(url))
    links = {'Wikipedia page': titles,
             'Links': lst_links
             }
    write_csv_files_from_dictionary(links, len(titles))


def write_csv_files_from_dictionary(links, length):
    file = 'Physics.csv'
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(links.keys())
        for itr in range(length):
            writer.writerow([val[itr] for val in links.values()])
        print(f'Csv file is finished')


def see_also_links_titles():
    see_also_link = 'https://en.wikipedia.org/wiki/Linear_motion'
    base_link = 'https://en.wikipedia.org/wiki/'
    titles = []
    lst_links = []
    clean_link = re.sub(base_link,'',see_also_link)
    see_also = w.page(clean_link).section('See also')
    all_link_from_see_also = (see_also.split("\n"))
    for link in all_link_from_see_also:
        titles.append(link)
        lst_links.append(base_link+link.replace(' ','_'))
    print(lst_links)

    links = {'Wikipedia page': titles,
             'Links': lst_links
             }




if __name__ == "__main__":
    see_also_links_titles()
