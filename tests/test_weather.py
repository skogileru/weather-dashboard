from weather import parse_weather

def test_parse_weather():
    fake_data = {
        "name": "London",
        "main": {"temp": 14.2, "feels_like": 13.0, "humidity": 72},
        "weather": [{"description": "light rain"}],
        "wind": {"speed": 4.1},
    }
    result = parse_weather(fake_data)
    assert result["city"] == "London"
    assert result["temp"] == 14.2