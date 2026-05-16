import feedparser

RSS_URL = "https://www.cert.ssi.gouv.fr/feed/"

feed = feedparser.parse(RSS_URL)

for entry in feed.entries[:5]:
    print(f"Titre : {entry.title}")
    print(f"Lien : {entry.link}")
    print("-" * 50)