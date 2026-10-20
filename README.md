# Weather Dashboard

A command-line Python app that shows the current weather for any city using the OpenWeatherMap API.

## Features

- Fetches live weather data from a REST API
- Displays temperature, "feels like" temperature, humidity, wind speed, and conditions
- Handles errors gracefully: misspelled cities, invalid API keys, rate limits, and network failures
- Keeps the API key secure using environment variables
- Includes unit tests with pytest

## Tech Stack

- Python 3
- `requests` for HTTP requests
- `python-dotenv` for loading environment variables
- `pytest` for testing
- OpenWeatherMap API

## Setup

1. Clone the repository:
```
   git clone https://github.com/skogileru/weather-dashboard.git
   cd weather-dashboard
```

2. Create and activate a virtual environment:
```
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # Mac/Linux
```

3. Install the dependencies:
```
   pip install -r requirements.txt
```

4. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api), then create a `.env` file in the project folder containing:
```
   OPENWEATHER_API_KEY=your_key_here
```

## Usage

```
python main.py
```

Example output:

```
Enter a city: Bangalore

Bangalore: light rain
Temperature: 20.57°C (feels like 19.14°C)
Humidity: 94%  |  Wind: 3.97 m/s
```

## Running Tests

```
python -m pytest
```

## What I Learned

- How to make HTTP requests to a REST API and work with JSON responses
- How to handle HTTP status codes and network errors
- How to keep secrets out of source code with environment variables
- How to structure a project by separating data logic from the user interface
- How to write unit tests using fake data