from bs4 import BeautifulSoup
import requests
import csv
import os


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


if __name__ == "__main__":
    print(f'Wikipedia link must be from wikipedia pages (e.g., List of physics concepts in primary and secondary education curricula)')
    print(f'Please pass valid wikipedia link')
    link = input('Valid link: ')
    get_wikipedia_pages_and_links(link)
