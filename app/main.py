import feedparser
from sources import SOURCES

print("\n/!\ TECHRADAR - VEILLE TECHNOLOGIQUE /!\\n")

for source in SOURCES:
    print("\n" + "=" * 60)
    print(f"🔵 {source['name']}")
    print("=" * 60 + "\n")

    try:
        feed = feedparser.parse(source["url"])

        if not feed.entries:
            print(" Aucun contenu trouvé pour cette source.\n")
            continue

        for entry in feed.entries[:5]:
            print(f"🟡 Titre : {entry.title}")
            print(f" Lien  : {entry.link}")
            print("-" * 40)

    except Exception as e:
        print(f" Erreur source {source['name']} : {e}")

    print("\n")