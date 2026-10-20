from weather import fetch_weather, parse_weather

city = input("Enter a city: ").strip()
data = fetch_weather(city)

if data:
    w = parse_weather(data)
    print(f"\n{w['city']}: {w['description']}")
    print(f"Temperature: {w['temp']}°C (feels like {w['feels_like']}°C)")
    print(f"Humidity: {w['humidity']}%  |  Wind: {w['wind']} m/s")