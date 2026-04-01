import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import matplotlib.pyplot as plt

def main():
    url = "https://news.ycombinator.com/item?id=42919502"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    elements = soup.find_all(class_="ind", indent=0)
    comments = [e.find_next(class_="comment") for e in elements]

    # Sentiment counters
    sentiments = {"Positif 😊": 0, "Négatif 😞": 0, "Neutre 😐": 0}

    for comment in comments:
        comment_text = comment.get_text()
        analysis = TextBlob(comment_text)

        if analysis.sentiment.polarity > 0:
            sentiments["Positif 😊"] += 1
        elif analysis.sentiment.polarity < 0:
            sentiments["Négatif 😞"] += 1
        else:
            sentiments["Neutre 😐"] += 1

    print(sentiments)

    # Visualisation
    colors = ["green", "red", "gray"]
    plt.bar(sentiments.keys(), sentiments.values(), color=colors)
    plt.title("Analyse des sentiments - Hacker News")
    plt.xlabel("Sentiment")
    plt.ylabel("Nombre de commentaires")
    plt.show()

if __name__ == "__main__":
    main()