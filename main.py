import re
from bs4 import BeautifulSoup
import requests
import csv
import wikipedia as w


# Function to scrape Wikipedia pages and links
def get_wikipedia_pages_and_links(wiki_link_to_scrape):
    # Send a GET request to the provided Wikipedia link and parse the HTML response
    res = requests.get(wiki_link_to_scrape).text
    wiki_link = 'https://en.wikipedia'

    # Use BeautifulSoup to parse the HTML
    soup = BeautifulSoup(res, 'html.parser')

    # Find the main content div
    div_instances = soup.find('div', class_='mw-parser-output')

    # Find all anchor tags (links) within the main content div
    a_instances = div_instances.find_all('a')

    # Initialize empty lists to store titles, links, and text
    titles = []
    lst_links = []
    lst_text = []

    # Iterate through the anchor tags
    for link in a_instances:
        url = link.get('href', '')

        # Check if the URL contains "/wiki/"
        if "/wiki/" in url:
            to_check = link.text.strip()
            titles.append(link.text.strip())
            lst_links.append(wiki_link + ''.join(url))

            # Try to get a short summary of the Wikipedia page
            try:
                lst_text.append(w.summary(to_check, sentences=1))
            except Exception as e:
                lst_text.append('Exception occurred')
                print(f'Error occurred {e}')

    # Call the see_also_links_titles function to scrape "See also" links
    see_also_links_titles(lst_links)

    # Create a dictionary to store the collected data
    links = {
        'Wikipedia page': titles,
        'Text': lst_text,
        'Links': lst_links
    }

    # Write the data to a CSV file
    write_csv_files_from_dictionary(links, len(titles))


# Function to write data from a dictionary to a CSV file
def write_csv_files_from_dictionary(links, length):
    file = 'new.csv'
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(links.keys())
        for itr in range(length):
            writer.writerow([val[itr] for val in links.values()])
        print(f'Csv file is finished')


# Function to scrape "See also" links and titles
def see_also_links_titles(see_also_link):
    base_link = 'https://en.wikipedia.org/wiki/'
    titles = []
    lst_links = []
    lst_text = []

    # Clean the link to extract the title
    clean_link = re.sub(base_link, '', see_also_link)

    # Use the Wikipedia library to get the "See also" section
    see_also_cleaning = w.page(clean_link).section('See also')

    # Split the "See also" section into individual links
    all_link_from_see_also = see_also_cleaning.split("\n")

    # Iterate through the links
    for link in all_link_from_see_also:
        titles.append(link)
        lst_links.append(base_link + link.replace(' ', '_'))

        # Try to get a short summary of the linked pages
        try:
            lst_text.append(w.summary(link, sentences=1))
        except Exception as e:
            lst_text.append('Exception occurred')
            print(f'Error occurred {e}')

    # Create a dictionary to store the collected data
    links = {
        'Wikipedia page': titles,
        'Text': lst_text,
        'Links': lst_links
    }

    # Write the data to a CSV file
    write_csv_files_from_dictionary(links, len(titles))


# Main program
if __name__ == "__main":
    print('''
    1. Choose if you want to scrape a list (e.g. List of physics)
    2. Choose if you want to scrape the "See also" section ''')

    choice = int(input('Choose 1 or 2: '))

    if choice == 1:
        link = input('Input link with "See also"')
        see_also_links_titles(link)
    elif choice == 2:
        lists = input('Input link with a list')
        get_wikipedia_pages_and_links(lists)
