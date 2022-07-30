# My Stock Portfolio Project

This is a django project

## Project Set Up
1. `pip install -r requirements.txt`
2. Create an `.env` file to store your environment variables. There is a sample of it in `sample_env.txt`
3. Create a free account at [Financial Modeling Prep Api](https://site.financialmodelingprep.com/developer/docs/)
4. Get your API key and put it in the `.env` file
5. Generate a secret key for `DJANGO_SETTINGS_SECRET_KEY` using whatever method you prefer.

## How to run the website
1. Make migration: `python manage.py migrate `
2. Start server: `python manage.py runserver`

# Notes
1. The timezone for this project is set to "America/New_York" to make it easier to follow NYSE time

*Data provided by [Financial Modeling Prep](https://site.financialmodelingprep.com/developer/docs/)*