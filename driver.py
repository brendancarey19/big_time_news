from nlp.summarize import PreSum
from ai.gpt import AIBot
from nlp.summarize import PreSum
from ai.gpt import AIBot
from scraper.scraper import scrape_ap_sports

TOKEN = "<redacted>"
URL = "https://api.openai.com/v1/completions"

if __name__ == "__main__":
    titles, articles = scrape_ap_sports()
    for article in articles:
        #summary = PreSum(article, "Brendan Carey").summary
        summary = " ".join(article)
        run = AIBot(summary, TOKEN, URL).response
