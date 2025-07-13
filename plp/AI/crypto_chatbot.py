import requests

# Define basic sustainability scores manually
sustainability_scores = {
    "bitcoin": {"energy_use": "high", "sustainability_score": 3},
    "ethereum": {"energy_use": "medium", "sustainability_score": 6},
    "cardano": {"energy_use": "low", "sustainability_score": 8}
}

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'ids': 'bitcoin,ethereum,cardano',
        'order': 'market_cap_desc',
        'per_page': 3,
        'page': 1,
        'sparkline': 'false'
    }
    response = requests.get(url, params=params)
    return response.json()

def analyze_crypto(data):
    crypto_db = {}
    for coin in data:
        name = coin['id']
        price_change = coin['price_change_percentage_24h']
        market_cap = coin['market_cap']
        trend = "rising" if price_change > 0 else "falling" if price_change < 0 else "stable"
        sustainability = sustainability_scores.get(name, {"energy_use": "unknown", "sustainability_score": 0})
        
        crypto_db[name] = {
            "price_trend": trend,
            "market_cap": market_cap,
            "energy_use": sustainability["energy_use"],
            "sustainability_score": sustainability["sustainability_score"]
        }
    return crypto_db

def get_response(user_query, crypto_db):
    user_query = user_query.lower()

    if "sustainable" in user_query or "eco" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"🌱 Invest in {recommend.capitalize()}! It’s eco-friendly and has long-term potential."

    elif "trending" in user_query or "rising" in user_query:
        trending = [coin.capitalize() for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        return f"📈 Trending coins: {', '.join(trending)}" if trending else "No coins are trending up right now."

    elif "long-term" in user_query or "growth" in user_query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] >= 7:
                return f"🚀 {coin.capitalize()} is rising and has strong sustainability. Great for long-term growth!"
        return "🤔 No coin fully meets the long-term criteria right now."

    elif "profitable" in user_query or "best investment" in user_query:
        high_profit = sorted(
            [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"],
            key=lambda c: crypto_db[c]["market_cap"],
            reverse=True
        )
        if high_profit:
            return f"💰 {high_profit[0].capitalize()} looks profitable with a strong market cap and upward trend!"
        return "📉 No coins are currently showing high-profit indicators."

    elif "bye" in user_query or "exit" in user_query:
        return "👋 Goodbye! Remember, crypto is risky — always do your own research."

    else:
        return "🤖 I'm still learning! Try asking about trends, sustainability, or long-term growth."

# Run chatbot
print("👋 Hello! I'm CryptoBuddy (Real-Time Edition). Let's talk crypto! ")
crypto_data = fetch_crypto_data()
crypto_db = analyze_crypto(crypto_data)

while True:
    user_input = input("\nYou: ")
    reply = get_response(user_input, crypto_db)
    print("CryptoBuddy:", reply)
    if "goodbye" in reply.lower():
        break
