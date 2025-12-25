# Google Sheets Workout Logger

Small Python script that takes a natural-language description of your workout (for example: “ran 5km and did 20 minutes of cycling”) and logs it into a Google Sheet via the Sheety API.

## Main features

- Prompts you with a question like: `What exercise did you do today?`
- Sends your answer, together with your weight, height, age and gender, to an exercise-tracking API that can understand natural language.
- Reads the first exercise from the JSON response and extracts:
  - `name` of the exercise  
  - `duration_min` (how many minutes the workout took)  
  - `nf_calories` (estimated calories burned)
- Uses `datetime` to get today’s date and time and formats them as:
  - `date` – `DD/MM/YY`  
  - `time` – hour in `HH` format
- Builds a `sheet_insert` dictionary containing:
  - `date`, `time`, `exercise`, `duration`, `calories`
- Sends this data to the Sheety endpoint so a new row is added to your Google Sheet automatically.
- Stores all API keys, usernames and passwords in environment variables loaded with `os.environ`, so no secrets are hard-coded in the script.

## What I learned

- Sending POST requests with `requests` and working with JSON responses from REST APIs.
- Using a natural-language exercise API to turn free-text input into structured data.
- Formatting dates and times with `datetime` for logging and reporting.
- Pushing data into Google Sheets through the Sheety API instead of handling the full Google Sheets API.
- Keeping credentials (API keys, usernames, passwords, endpoint URLs) in environment variables instead of in plain text inside the code.
- Designing a small automation that connects user input → external API → Google Sheets.

## Project structure

- `main.py` – single script that:
  - loads configuration from environment variables  
    - `App_id` and `App_key` for the exercise API  
    - `Username` and `Password` for Sheety basic auth  
    - `Sheety_url` for the Google Sheet endpoint
  - asks the user what exercise they did today,
  - sends the request to the exercise API and parses the JSON response,
  - constructs a workout record (`date`, `time`, `exercise`, `duration`, `calories`),
  - POSTs that record to Sheety so it appears as a new row in the Google Sheet.

## How to run

1. Make sure you have Python 3 installed.
2. Install the required package:  
   `pip install requests`
3. Create a free account for an exercise-tracking API that supports natural-language workout input and obtain:
   - an application ID (`APP_ID`)  
   - an application key (`APP_KEY`)
4. Create a Google Sheet with columns similar to: `Date`, `Time`, `Exercise`, `Duration`, `Calories`.
5. Go to **Sheety**, connect it to your Google Sheet and create an endpoint for the worksheet where you want to store workouts. Copy the endpoint URL and your Sheety credentials.
6. In your environment (for example, a `.env` file or your IDE’s run configuration), define:
   - `App_id` – your exercise API app ID  
   - `App_key` – your exercise API key  
   - `Username` – your Sheety username  
   - `Password` – your Sheety password  
   - `Sheety_url` – the Sheety endpoint URL for your workout sheet
7. Open `main.py` and, if needed, adjust the fixed values for:
   - `weight_kg`  
   - `height_cm`  
   - `age`  
   - `gender`
8. From the project folder, run:  
   `python main.py`
9. When the script asks `What exercise did you do today?`, type your workout in natural language and press Enter.

If everything is configured correctly, the script will send your description to the exercise API, read back the exercise name, duration and calories, then send a POST request to Sheety. A new row with today’s date, the current time, the exercise, the duration and the calories burned will appear automatically in your Google Sheet.
