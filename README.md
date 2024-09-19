# Fetch-test
For fetch coding test

This Python utility retrieves location data (latitude, longitude, place name, state, and country) from the OpenWeatherMap API based on a city, state (optional), or zip code.

### Usage:
Install required dependencies:
Bash
pip install requests

Replace API key: Replace YOUR_API_KEY in the geo_requests.py file with your actual OpenWeatherMap API key.
Run the utility:
Bash
python geo_requests.py

Enter city, state (optional), or zip code when prompted and press q when all entries made or when you wish to quit. The utility will print the retrieved location information.

### Testing:
To run the integration tests, execute the following command:

Bash
python testing.py


### Features:
Handles both city/state and zip code formats.
Returns latitude, longitude, place name, state (if available), and country.
Provides informative error messages for invalid locations or API errors.
Includes integration tests to ensure correct functionality.


### Limitations:
Currently only return the first available result for locations that share the same name e.g. Hyderabad, India VS Hyderabad, Pakistan.
City and states with the same name will result in city location taking priority over state e.g. New York city VS New York state.
Relies on the OpenWeatherMap API, which may have rate limits or other restrictions.
