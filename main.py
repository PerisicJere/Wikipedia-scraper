import re

from bs4 import BeautifulSoup
import requests
import csv
import wikipedia as w


def get_wikipedia_pages_and_links(wiki_link_to_scrape):
    res = requests.get(wiki_link_to_scrape).text
    wiki_link = 'https://en.wikipedia.org'

    soup = BeautifulSoup(res, 'html.parser')
    div_instances = soup.find('div', class_='mw-parser-output')
    a_instances = div_instances.find_all('a')

    titles = []
    lst_links = []
    lst_text = []
    for link in a_instances:
        url = link.get('href', '')
        if "/wiki/" in url:
            to_check = link.text.strip()
            titles.append(link.text.strip())
            lst_links.append(wiki_link + ''.join(url))
            try:
                lst_text.append(w.summary(to_check, sentences=1))
            except Exception as e:
                lst_text.append('Exception occurred')
                print(f'Error occurred {e}')

    links = {'Wikipedia page': titles,
             'Text': lst_text,
             'Links': lst_links
             }
    write_csv_files_from_dictionary(links, len(titles))


def write_csv_files_from_dictionary(links, length):
    file = 'new.csv'
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(links.keys())
        for itr in range(length):
            writer.writerow([val[itr] for val in links.values()])
        print(f'Csv file is finished')


def see_also_links_titles(see_also_link):
    base_link = 'https://en.wikipedia.org/wiki/'
    titles = []
    lst_links = []
    lst_text = []
    clean_link = re.sub(base_link, '', see_also_link)
    see_also_cleaning = w.page(clean_link).section('See also')
    all_link_from_see_also = (see_also_cleaning.split("\n"))
    for link in all_link_from_see_also:
        titles.append(link)
        lst_links.append(base_link + link.replace(' ', '_'))
        try:
            lst_text.append(w.summary(link, sentences=1))
        except Exception as e:
            lst_text.append('Exception occurred')
            print(f'Error occurred {e}')
    links = {'Wikipedia page': titles,
             'Text': lst_text,
             'Links': lst_links
             }
    write_csv_files_from_dictionary(links, len(titles))


if __name__ == "__main__":
    print(f'''
    1. Choose if you want to scrape list (e.g. List of physics)
    2. Choose if you want to scrape "See also" section ''')
    choice = int(input(f'Choose 1 or 2: '))
    if choice == 1:
        link = input(f'Input link with "See also"')
        see_also_links_titles(link)
    elif choice == 2:
        lists = input(f'Input link with list')
        get_wikipedia_pages_and_links(lists)

