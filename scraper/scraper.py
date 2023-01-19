from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re


def scrape_ap_sports():

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

    # root page
    url = 'https://apnews.com/hub/sports?utm_source=apnewsnav&utm_medium=navigation'
    driver.get(url)

    # soup for main page
    root_soup = BeautifulSoup(driver.page_source, 'html.parser')

    all_titles = []
    all_articles = []
    unique_links = set()

    # loop thru all the articles linked
    for link in root_soup.find_all('a', attrs={'href': re.compile("^/article/")}):
        path = link.get('href')

        # this is a link we wanna do something with 
        if path not in unique_links:
            unique_links.add(path)
            
            # now navigate to the article
            driver.get('https://apnews.com' + path)

            # get the paragraph tags from the artice, and also find and append the title
            soup  = BeautifulSoup(driver.page_source, 'html.parser')
            all_titles.append(soup.find("title").text[:-10])
            all_html = soup.find_all("p", {"class": "Component-root-0-2-67 p Component-p-0-2-58"})

            # add each paragraph to a list of paragraphs
            article_by_paragraph = []
            for para_html in all_html:
                para = para_html.text

                # check for first line and end of article
                if '(AP)' in para:
                    article_start = para.find("(AP)") + 7
                    article_by_paragraph.append(para[article_start:])
                elif para[0] == '_':
                    break
                else:
                    article_by_paragraph.append(para)

            all_articles.append(article_by_paragraph)

        if len(unique_links) == 5:
            break

    driver.quit()
    return all_titles, all_articles