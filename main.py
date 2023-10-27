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

    links = {}
    for link in a_instances:
        url = link.get('href', '')
        if "/wiki/" in url:
            links[link.text.strip()] = wiki_link + ''.join(url)

    write_csv_files_from_dictionary(links)


def write_csv_files_from_dictionary(links):
    file = 'Physics.csv'
    with open(file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=links.keys())
        writer.writeheader()
        writer.writerow(links)


if __name__ == "__main__":
    link = "https://en.wikipedia.org/wiki/List_of_physics_concepts_in_primary_and_secondary_education_curricula"
    get_wikipedia_pages_and_links(link)
