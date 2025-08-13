
from flask import Flask, render_template, request, redirect, url_for
from urllib.parse import quote_plus

import requests
##nes fetching

import os
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
print("Loaded NEWS_API_KEY:", NEWS_API_KEY)

app = Flask(__name__)



##UPDATE WITH MORE SPECIFIC"##..
##default news wuery##
DEFAULT_QUERY =(
        
'"women\'s sports" OR "WNBA" OR "NWSL" OR "LPGA" OR "female athletes" OR "women\'s soccer" OR "women\'s tennis" OR "women\'s softball" OR "women\'s basketball" OR '
'"women\'s gymnastics" OR "women\'s track" OR "women\'s racing" OR "women\'s fencing" OR "women\'s football"'
)

##global ticket sites##
ticket_sites = [
    {"name": "WNBA Tickets", "url": "https://www.wnba.com/tickets/"},
    {"name": "NWSL Tickets", "url": "https://www.nwslsoccer.com/schedule"},
    {"name": "LPGA Events", "url": "https://www.lpga.com/tournaments"},
    {"name": "WTA Tickets", "url": "https://www.wtatennis.com/tournaments"},
    {"name": "FIFA Women's World Cup Tickets", "url": "https://www.fifa.com/tickets"},
    {"name": "USA Gymnastics Events", "url": "https://usagym.org/pages/events/"},
    {"name": "USATF Events", "url": "https://www.usatf.org/events"},
    {"name": "USA Softball Tickets", "url": "https://www.teamusa.org/usa-softball"},
    {"name": "USA Volleyball Tickets", "url": "https://www.teamusa.org/usa-volleyball"},
    {"name": "World Rugby Events", "url": "https://www.world.rugby/tournaments"},
    {"name": "UCI Women's Cycling Events", "url": "https://www.uci.org/calendar"},
    {"name": "FIBA Women’s Basketball Events", "url": "https://www.fiba.basketball"},
    {"name": "ICC Women’s Cricket Tickets", "url": "https://www.icc-cricket.com/tickets"},
    {"name": "USA Swimming Events", "url": "https://tickets.usaswimming.org/"},
    {"name": "NCAA Women's Championships", "url": "https://www.ncaa.com/championships"},
    {"name": "StubHub - General Sports", "url": "https://www.stubhub.com"},

    ]

    



merch_sites = [
    {"name": "WNBA Store", "url": "https://www.wnbastore.nba.com"},
    {"name": "NWSL Shop", "url": "https://shop.nwslsoccer.com"},
    {"name": "LPGA Shop", "url": "https://www.lpga.com/shop"},
    {"name": "WTA Official Store", "url": "https://shop.wtatennis.com"},
    {"name": "FIFA Women's World Cup Store", "url": "https://www.fifastore.com"},
    {"name": "USA Gymnastics Store", "url": "https://shopusagym.com"},
    {"name": "USA Track & Field Shop", "url": "https://www.teamusashop.com"},
    {"name": "USA Softball Store", "url": "https://www.usasoftballstore.com"},
    {"name": "USA Volleyball Store", "url": "https://www.usavolleyballshop.com"},
    {"name": "US Fencing Gear", "url": "https://www.absolutefencinggear.com"},
    {"name": "USA Lacrosse Store", "url": "https://store.usalacrosse.com"},
    {"name": "World Rugby Shop", "url": "https://www.worldrugbyshop.com"},
    {"name": "UCI Cycling Store", "url": "https://uci-store.com"},
    {"name": "WSL Surf Shop", "url": "https://shop.worldsurfleague.com"},
    {"name": "ICC Cricket Shop", "url": "https://shop.icc-cricket.com"},
    {"name": "USA Swimming Official Fan Shop", "url": "https://fanshop.usaswimming.org/"},
    {"name": "Nike Women Athletes", "url": "https://www.nike.com/w/womens-sportswear"},
    {"name": "Adidas Women Athletes", "url": "https://www.adidas.com/us/women-sports"},
    ]

  


social_media_sites = [
    {"name": "WNBA on X (Twitter)", "url": "https://twitter.com/WNBA"},
    {"name": "WNBA on Instagram", "url": "https://www.instagram.com/wnba/"},
    {"name": "NWSL on X (Twitter)", "url": "https://twitter.com/NWSL"},
    {"name": "NWSL on Instagram", "url": "https://www.instagram.com/nwsl/"},
    {"name": "LPGA on X (Twitter)", "url": "https://twitter.com/LPGAGolf"},
    {"name": "LPGA on Instagram", "url": "https://www.instagram.com/lpgagolf/"},
    {"name": "WTA on X (Twitter)", "url": "https://twitter.com/WTA"},
    {"name": "WTA on Instagram", "url": "https://www.instagram.com/wta/"},
    {"name": "USA Gymnastics on X (Twitter)", "url": "https://twitter.com/USAGym"},
    {"name": "USA Gymnastics on Instagram", "url": "https://www.instagram.com/usagym/"},
    {"name": "NCAA Women's Sports on X (Twitter)", "url": "https://twitter.com/NCAA"},
    {"name": "NCAA Women's Sports on Instagram", "url": "https://www.instagram.com/ncaa/"},
    {"name": "World Rugby Women on X (Twitter)", "url": "https://twitter.com/WorldRugbyWomen"},
    {"name": "World Rugby Women on Instagram", "url": "https://www.instagram.com/worldrugbywomen/"},
    {"name": "US Fencing on X (Twitter)", "url": "https://twitter.com/USFencing"},
    {"name": "US Fencing on Instagram", "url": "https://www.instagram.com/usfencing/"},
    {"name": "USA Volleyball on X (Twitter)", "url": "https://twitter.com/usavolleyball"},
    {"name": "USA Volleyball on Instagram", "url": "https://www.instagram.com/usavolleyball/"},
    {"name": "FIBA Women's Basketball on X (Twitter)", "url": "https://twitter.com/FIBA_WWC"},
    {"name": "FIBA Women's Basketball on Instagram", "url": "https://www.instagram.com/fiba_wwc/"},
    {"name": "USATF Women's Track & Field on X (Twitter)", "url": "https://twitter.com/USATF"},
    {"name": "USATF Women's Track & Field on Instagram", "url": "https://www.instagram.com/usatf/"},
    {"name": "NWHL on X (Twitter)", "url": "https://twitter.com/NWHL"},
    {"name": "NWHL on Instagram", "url": "https://www.instagram.com/nwhl/"},
    {"name": "USA Softball on X (Twitter)", "url": "https://twitter.com/USASoftball"},
    {"name": "USA Softball on Instagram", "url": "https://www.instagram.com/usasoftball/"},
    {"name": "US Lacrosse on X (Twitter)", "url": "https://twitter.com/USLacrosse"},
    {"name": "US Lacrosse on Instagram", "url": "https://www.instagram.com/uslax/"},
    {"name": "UCI Women's Cycling on X (Twitter)", "url": "https://twitter.com/UCI_cycling"},
    {"name": "UCI Women's Cycling on Instagram", "url": "https://www.instagram.com/uci_cycling/"},
    {"name": "World Surf League on X (Twitter)", "url": "https://twitter.com/WSLSurf"},
    {"name": "World Surf League on Instagram", "url": "https://www.instagram.com/worldsurfleague/"},
    {"name": "ICC Women's Cricket on X (Twitter)", "url": "https://twitter.com/ICC"},
    {"name": "ICC Women's Cricket on Instagram", "url": "https://www.instagram.com/icc/"},
    {"name": "FIFA Women's World Cup on X (Twitter)", "url": "https://twitter.com/FIFAWWC"},
    {"name": "FIFA Women's World Cup on Instagram", "url": "https://www.instagram.com/fifawomensworldcup/"},
    {"name": "USA Swimming on X (Twitter)", "url": "https://twitter.com/USASwimming"},
    {"name": "USA Swimming on Instagram", "url": "https://www.instagram.com/usaswimming/"}
    ]   



def get_news(query=DEFAULT_QUERY):
    if not NEWS_API_KEY:
        raise RuntimeError("NEWS_API_KEY is not set in environment variables.")
    
    encoded_query = quote_plus(query)
    url = f"https://newsapi.org/v2/everything?q={encoded_query}&language=en&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"News API request failed with status {response.status_code}")
        return []

    articles = response.json().get('articles', [])

    women_sports_keywords = [
        "women", "female", "women's", "female athlete",
        "wnba", "nwsl", "lpga", "wta", "ncaa women's",
        "women's basketball", "women's soccer", "women's tennis",
        "women's softball", "women's gymnastics", "women's track",
        "team usa women", "uswnt", "women’s sports"
    ]

    def article_mentions_womens_sports(article):
        content = f"{article.get('title', '')} {article.get('description', '')} {article.get('content', '')}".lower()
        return any(keyword in content for keyword in women_sports_keywords)

    filtered_articles = [article for article in articles if article_mentions_womens_sports(article)]

    return filtered_articles
    






@app.route('/')
def home():
    articles = get_news()
    main_articles = articles[:5] if len(articles) >= 5 else articles
    sidebar_articles = articles[5:9] if len(articles) > 5 else []

    #temp needs api for live updates
    




    return render_template(
        "index.html", 
        articles=articles,
        main_articles=main_articles,
        sidebar_articles=sidebar_articles,
        ticket_sites=ticket_sites,
        merch_sites=merch_sites,
        social_media_sites=social_media_sites,
    )

@app.route('/basketball')
def basketball():
    basketball_query = '"WNBA" OR "women\'s basketball"'
    articles = get_news(basketball_query)
    main_articles = articles[:5] 
    sidebar_articles = articles[5:9] 

    basketball_tickets = [t for t in ticket_sites if "basketball" in t["name"].lower() or "wnba" in t["name"].lower() or "stubhub" in t["name"].lower() or "ncaa" in t["name"].lower() or "fiba" in t["name"].lower()]
    basketball_merch = [m for m in merch_sites if "basketball" in m["name"].lower() or "wnba" in m["name"].lower() or "nike" in m["name"].lower() or "adidas" in m["name"].lower()]
    basketball_social = [s for s in social_media_sites if "basketball" in s["name"].lower() or "wnba" in s["name"].lower() or "ncaa" in s["name"].lower()]


    
    return render_template(
        'basketball.html',
        title="Women's Basketball",
        main_articles=main_articles,
        sidebar_articles=sidebar_articles, 
        ticket_sites=basketball_tickets,
        merch_sites=basketball_merch,
        social_media_sites=basketball_social,
    )

@app.route('/soccer')
def soccer():
    soccer_query = '"NWSLA" OR "women\'s soccer" OR "FIFA"'
    articles = get_news(soccer_query)
    main_articles = articles[:5] 
    sidebar_articles = articles[5:9] 

    soccer_tickets = [t for t in ticket_sites if "soccer" in t["name"].lower() or "wta" in t["name"].lower() or "stubhub" in t["name"].lower() or "ncaa" in t["name"].lower() or "fifa" in t["name"].lower()]
    soccer_merch = [m for m in merch_sites if "soccer" in m["name"].lower() or "nwsl" in m["name"].lower() or "nike" in m["name"].lower() or "adidas" in m["name"].lower() or "fifa" in m["name"].lower()]
    soccer_social = [s for s in social_media_sites if "soccer" in s["name"].lower() or "fifa" in s["name"].lower() or "ncaa" in s["name"].lower() or "nwsl" in s["name"].lower()]


    
    return render_template(
        'soccer.html',
        title="Women's Soccer",
        main_articles=main_articles,
        sidebar_articles=sidebar_articles, 
        ticket_sites=soccer_tickets,
        merch_sites=soccer_merch,
        social_media_sites=soccer_social,
    )

@app.route('/softball')
def softball():
    softball_query = '"softball" OR "women\'s softball"'
    articles = get_news(softball_query)
    main_articles = articles[:5] 
    sidebar_articles = articles[5:9] 

    softball_tickets = [t for t in ticket_sites if "softball" in t["name"].lower() or "ncaa" in t["name"].lower() or "stubhub" in t["name"].lower() or "ncaa" in t["name"].lower()]
    softball_merch = [m for m in merch_sites if "softball" in m["name"].lower() or "nike" in m["name"].lower() or "adidas" in m["name"].lower()]
    softball_social = [s for s in social_media_sites if "softball" in s["name"].lower() or "ncaa" in s["name"].lower()]


    
    return render_template(
        'softball.html',
        title="Women's Softball",
        main_articles=main_articles,
        sidebar_articles=sidebar_articles, 
        ticket_sites=softball_tickets,
        merch_sites=softball_merch,
        social_media_sites=softball_social,
    )

@app.route('/tennis')
def tennis():
    tennis_query = '"tennis" OR "women\'s tennis" OR "wta"'
    articles = get_news(tennis_query)
    main_articles = articles[:5] 
    sidebar_articles = articles[5:9] 

    tennis_tickets = [t for t in ticket_sites if "tennis" in t["name"].lower() or "ncaa" in t["name"].lower() or "stubhub" in t["name"].lower() or "ncaa" in t["name"].lower() or "wta" in t["name"].lower()]
    tennis_merch = [m for m in merch_sites if "tennis" in m["name"].lower() or "nike" in m["name"].lower() or "adidas" in m["name"].lower() or "wta" in m["name"].lower()]
    tennis_social = [s for s in social_media_sites if "tennia" in s["name"].lower() or "ncaa" in s["name"].lower() or "wta" in s["name"].lower()]


    
    return render_template(
        'tennis.html',
        title="Women's Tennis",
        main_articles=main_articles,
        sidebar_articles=sidebar_articles, 
        ticket_sites=tennis_tickets,
        merch_sites=tennis_merch,
        social_media_sites=tennis_social,
    )

@app.route('/track')
def track():
    track_query = '"track" OR "women\'s track" OR "women\'s usatf"'
    articles = get_news(track_query)
    main_articles = articles[:5] 
    sidebar_articles = articles[5:9] 

    track_tickets = [t for t in ticket_sites if "track" in t["name"].lower() or "ncaa" in t["name"].lower() or "stubhub" in t["name"].lower() or "usatf" in t["name"].lower()]
    track_merch = [m for m in merch_sites if "track" in m["name"].lower() or "nike" in m["name"].lower() or "adidas" in m["name"].lower() or "usatf" in m["name"].lower()]
    track_social = [s for s in social_media_sites if "track" in s["name"].lower() or "ncaa" in s["name"].lower() or "usatf" in s["name"].lower()]


    
    return render_template(
        'track.html',
        title="Women's Track & Field",
        main_articles=main_articles,
        sidebar_articles=sidebar_articles, 
        ticket_sites=track_tickets,
        merch_sites=track_merch,
        social_media_sites=track_social,
    )


@app.route('/cricket')
def cricket():
    cricket_query = '"cricket" OR "women\'s cricket" OR "women\'s icc"'
    articles = get_news(cricket_query)
    main_articles = articles[:5] 
    sidebar_articles = articles[5:9] 

    cricket_tickets = [t for t in ticket_sites if "cricket" in t["name"].lower() or "icc" in t["name"].lower() or "stubhub" in t["name"].lower() or "cricket" in t["name"].lower()]
    cricket_merch = [m for m in merch_sites if "cricket" in m["name"].lower() or "nike" in m["name"].lower() or "adidas" in m["name"].lower() or "icc" in m["name"].lower()]
    cricket_social = [s for s in social_media_sites if "cricket" in s["name"].lower() or "ncaa" in s["name"].lower() or "icc" in s["name"].lower()]


    
    return render_template(
        'cricekt.html',
        title="Women's Cricket",
        main_articles=main_articles,
        sidebar_articles=sidebar_articles, 
        ticket_sites=cricket_tickets,
        merch_sites=cricket_merch,
        social_media_sites=cricket_social,
    )

@app.route('/cycling')
def cycling():
    cycling_query = '"cycling" OR "women\'s cycling" OR "women\'s uci"'
    articles = get_news(cycling_query)
    main_articles = articles[:5] 
    sidebar_articles = articles[5:9] 

    cycling_tickets = [t for t in ticket_sites if "cycling" in t["name"].lower() or "ncaa" in t["name"].lower() or "stubhub" in t["name"].lower() or "uci" in t["name"].lower()]
    cycling_merch = [m for m in merch_sites if "cycling" in m["name"].lower() or "nike" in m["name"].lower() or "adidas" in m["name"].lower() or "uci" in m["name"].lower()]
    cycling_social = [s for s in social_media_sites if "cycling" in s["name"].lower() or "ncaa" in s["name"].lower() or "uci" in s["name"].lower()]


    
    return render_template(
        'cycling.html',
        title="Women's Cycling",
        main_articles=main_articles,
        sidebar_articles=sidebar_articles, 
        ticket_sites=cycling_tickets,
        merch_sites=cycling_merch,
        social_media_sites=cycling_social,
    )

@app.route('/fencing')
def fencing():
    fencing_query = '"fencing" OR "women\'s fencing"'
    articles = get_news(fencing_query)
    main_articles = articles[:5] 
    sidebar_articles = articles[5:9] 

    fencing_tickets = [t for t in ticket_sites if "fencing" in t["name"].lower() or "ncaa" in t["name"].lower() or "stubhub" in t["name"].lower()]
    fencing_merch = [m for m in merch_sites if "fencing" in m["name"].lower() or "nike" in m["name"].lower() or "adidas" in m["name"].lower()]
    fencing_social = [s for s in social_media_sites if "fencing" in s["name"].lower() or "ncaa" in s["name"].lower()]


    
    return render_template(
        'fencing.html',
        title="Women's Fencing",
        main_articles=main_articles,
        sidebar_articles=sidebar_articles, 
        ticket_sites=fencing_tickets,
        merch_sites=fencing_merch,
        social_media_sites=fencing_social,
    )

@app.route('/golf')
def golf():
    track_query = '"golf" OR "women\'s golf" OR "women\'s lgpa"'
    articles = get_news(track_query)
    main_articles = articles[:5] 
    sidebar_articles = articles[5:9] 

    golf_tickets = [t for t in ticket_sites if "golf" in t["name"].lower() or "ncaa" in t["name"].lower() or "stubhub" in t["name"].lower() or "lgpa" in t["name"].lower()]
    golf_merch = [m for m in merch_sites if "golf" in m["name"].lower() or "nike" in m["name"].lower() or "adidas" in m["name"].lower() or "lgpa" in m["name"].lower()]
    golf_social = [s for s in social_media_sites if "golf" in s["name"].lower() or "ncaa" in s["name"].lower() or "lgpa" in s["name"].lower()]


    
    return render_template(
        'golf.html',
        title="Women's Golf",
        main_articles=main_articles,
        sidebar_articles=sidebar_articles, 
        ticket_sites=golf_tickets,
        merch_sites=golf_merch,
        social_media_sites=golf_social,
    )

@app.route('/gymnastics')
def gymnastics():
    gymnastics_query = '"gymnastics" OR "women\'s gymnastics"'
    articles = get_news(gymnastics_query)
    main_articles = articles[:5] 
    sidebar_articles = articles[5:9] 

    gymnastics_tickets = [t for t in ticket_sites if "gymnastics" in t["name"].lower() or "ncaa" in t["name"].lower() or "stubhub" in t["name"].lower()]
    gymnastics_merch = [m for m in merch_sites if "gymnastics" in m["name"].lower() or "nike" in m["name"].lower() or "adidas" in m["name"].lower()]
    gymnastics_social = [s for s in social_media_sites if "gymnastics" in s["name"].lower() or "ncaa" in s["name"].lower()]


    
    return render_template(
        'gymnastics.html',
        title="Women's Gymnastics",
        main_articles=main_articles,
        sidebar_articles=sidebar_articles, 
        ticket_sites=gymnastics_tickets,
        merch_sites=gymnastics_merch,
        social_media_sites=gymnastics_social,
    )

@app.route('/hockey')
def hockey():
    hockey_query = '"hockey" OR "women\'s hockey" OR "nwhl"'
    articles = get_news(hockey_query)
    main_articles = articles[:5] 
    sidebar_articles = articles[5:9] 

    hockey_tickets = [t for t in ticket_sites if "hockey" in t["name"].lower() or "ncaa" in t["name"].lower() or "stubhub" in t["name"].lower() or "nwhl" in t["name"].lower()]
    hockey_merch = [m for m in merch_sites if "hockey" in m["name"].lower() or "nike" in m["name"].lower() or "adidas" in m["name"].lower() or "nwhl" in m["name"].lower()]
    hockey_social = [s for s in social_media_sites if "hockey" in s["name"].lower() or "ncaa" in s["name"].lower() or "nwhl" in s["name"].lower()]


    
    return render_template(
        'hockey.html',
        title="Women's Hockey",
        main_articles=main_articles,
        sidebar_articles=sidebar_articles, 
        ticket_sites=hockey_tickets,
        merch_sites=hockey_merch,
        social_media_sites=hockey_social,
    )

@app.route('/lacrosse')
def lacrosse():
    lacrosse_query = '"lacrosse" OR "women\'s lacrosse"'
    articles = get_news(lacrosse_query)
    main_articles = articles[:5] 
    sidebar_articles = articles[5:9] 

    lacrosse_tickets = [t for t in ticket_sites if "lacrosse" in t["name"].lower() or "ncaa" in t["name"].lower() or "stubhub" in t["name"].lower()]
    lacrosse_merch = [m for m in merch_sites if "lacrosse" in m["name"].lower() or "nike" in m["name"].lower() or "adidas" in m["name"].lower()]
    lacrosse_social = [s for s in social_media_sites if "lacrosse" in s["name"].lower() or "ncaa" in s["name"].lower()]


    
    return render_template(
        'lacrosse.html',
        title="Women's Lacrosse",
        main_articles=main_articles,
        sidebar_articles=sidebar_articles, 
        ticket_sites=lacrosse_tickets,
        merch_sites=lacrosse_merch,
        social_media_sites=lacrosse_social,
    )

@app.route('/rugby')
def rugby():
    rugby_query = '"rugby" OR "women\'s rugby"'
    articles = get_news(rugby_query)
    main_articles = articles[:5] 
    sidebar_articles = articles[5:9] 

    rugby_tickets = [t for t in ticket_sites if "rugby" in t["name"].lower() or "ncaa" in t["name"].lower() or "stubhub" in t["name"].lower()]
    rugby_merch = [m for m in merch_sites if "rugby" in m["name"].lower() or "nike" in m["name"].lower() or "adidas" in m["name"].lower()]
    rugby_social = [s for s in social_media_sites if "rugby" in s["name"].lower() or "ncaa" in s["name"].lower()]


    
    return render_template(
        'rugby.html',
        title="Women's Rugby",
        main_articles=main_articles,
        sidebar_articles=sidebar_articles, 
        ticket_sites=rugby_tickets,
        merch_sites=rugby_merch,
        social_media_sites=rugby_social,
    )

@app.route('/surf')
def surf():
    surf_query = '"surf" OR "women\'s surf"'
    articles = get_news(surf_query)
    main_articles = articles[:5] 
    sidebar_articles = articles[5:9] 

    surf_tickets = [t for t in ticket_sites if "surf" in t["name"].lower() or "ncaa" in t["name"].lower() or "stubhub" in t["name"].lower()]
    surf_merch = [m for m in merch_sites if "surf" in m["name"].lower() or "nike" in m["name"].lower() or "adidas" in m["name"].lower()]
    surf_social = [s for s in social_media_sites if "surf" in s["name"].lower() or "ncaa" in s["name"].lower()]


    
    return render_template(
        'surf.html',
        title="Women's Surf",
        main_articles=main_articles,
        sidebar_articles=sidebar_articles, 
        ticket_sites=surf_tickets,
        merch_sites=surf_merch,
        social_media_sites=surf_social,
    )

@app.route('/swimming')
def swimming():
    swimming_query = '"swimming" OR "women\'s swimming" OR "women\'s swim"'
    articles = get_news(swimming_query)
    main_articles = articles[:5] 
    sidebar_articles = articles[5:9] 

    swimming_tickets = [t for t in ticket_sites if "swimming" in t["name"].lower() or "ncaa" in t["name"].lower() or "stubhub" in t["name"].lower()]
    swimming_merch = [m for m in merch_sites if "swimming" in m["name"].lower() or "nike" in m["name"].lower() or "adidas" in m["name"].lower()]
    swimming_social = [s for s in social_media_sites if "swimming" in s["name"].lower() or "ncaa" in s["name"].lower()]


    
    return render_template(
        'swimming.html',
        title="Women's Swimming",
        main_articles=main_articles,
        sidebar_articles=sidebar_articles, 
        ticket_sites=swimming_tickets,
        merch_sites=swimming_merch,
        social_media_sites=swimming_social,
    )

@app.route('/volleyball')
def volleyball():
    volleyball_query = '"volleyball" OR "women\'s volleyball"'
    articles = get_news(volleyball_query)
    main_articles = articles[:5] 
    sidebar_articles = articles[5:9] 

    volleyball_tickets = [t for t in ticket_sites if "volleyball" in t["name"].lower() or "ncaa" in t["name"].lower() or "stubhub" in t["name"].lower()]
    volleyball_merch = [m for m in merch_sites if "volleyball" in m["name"].lower() or "nike" in m["name"].lower() or "adidas" in m["name"].lower()]
    volleyball_social = [s for s in social_media_sites if "volleyball" in s["name"].lower() or "ncaa" in s["name"].lower() or "usatf" in s["name"].lower()]


    
    return render_template(
        'volleyball.html',
        title="Women's Volleyball",
        main_articles=main_articles,
        sidebar_articles=sidebar_articles, 
        ticket_sites=volleyball_tickets,
        merch_sites=volleyball_merch,
        social_media_sites=volleyball_social,
    )





@app.route('/search')
def search():
    user_query = request.args.get("query", "").strip().lower()
    if not user_query:
        return render_template("not_found.html", query=user_query)    
    # Keywords mapping
    search_map = {
        # Sports
        "basketball": "basketball",
        "wnba": "basketball",
        "soccer": "soccer",
        "nwsl": "soccer",

        "softball": "softball",
        "tennis": "tennis",
        "track": "track",
        "golf": "golf",
        "gymnastics": "gymnastics",
        "rugby": "rugby",
        "fencing": "fencing",
        "volleyball": "volleyball",
        "hockey": "hockey",
        "lacrosse": "lacrosse",
        "cycling": "cycling",
        "surf": "surf",
        "cricket": "cricket",
        "swimming": "swimming",

        # Notable players
        "serena williams": "tennis",
        "williams": "tennis",
        "serena": "tennis",
        "venus williams": "tennis",
        "coco gauff": "tennis",
        "gauff": "tennis",
        "coco": "tennis",
        "naomi osaka": "tennis",
        "osaka": "tennis",
        "naomi": "tennis",
        "ashleigh barty": "tennis",
        "ashleigh": "tennis",
        "barty": "tennis",

        "alex morgan": "soccer",
        "alex": "soccer",
        "morgan": "soccer",
        "megan rapinoe": "soccer",
        "rapinoe": "soccer",
        "megan": "soccer",
        "trinity rodman": "soccer",
        "trinity": "soccer",
        "rodman": "soccer",

        "sue bird": "basketball",
        "sue": "basketball",
        "bird": "basketball",
        "diana taurasi": "basketball",
        "taurasi": "basketball",
        "diana": "basketball",
        "caitlin clark": "basketball",
        "clark": "basketball",
        "caitlin": "basketball",
        "angel reese": "basketball",
        "reese": "basketball",
        "angel": "basketball",
        "a'ja wilson": "basketball",
        "a'ja": "basketball",
        "aja": "basketball",
        "wilson": "basketball",
        "paige bueckers": "basketball",
        "paige": "basketball",
        "bueckers": "basketball",




        "simone biles": "gymnastics",
        "simone": "gymnastics",
        "biles": "gymnastics",
        "sunisa lee": "gymnastics",
        "sunisa": "gymnastics",
        "lee": "gymnastics",
        "aly raisman": "gymnastics",
        "aly": "gymnastics",
        "raisman": "gymnastics",

        "allyson felix": "track",
        "felix": "track",
        "allyson": "track",
        "katie ledecky": "swimming",
        "katie": "swimming",
        "ledecky": "swimming"
    }
#check if keyword is in userquery
    for keyword, route in search_map.items():
        if keyword in user_query:
            return redirect(url_for(route))
        
# If no keyword matches, do a general news search with the user query
    articles = get_news(query=user_query)
    if articles:
        return render_template("search_results.html", query=user_query, articles=articles)
    else:
        return render_template("not_found.html", query=user_query)
# Custom 404 Page
@app.errorhandler(404)
def not_found(e):
    return render_template("not_found.html", query=""), 404





# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)









