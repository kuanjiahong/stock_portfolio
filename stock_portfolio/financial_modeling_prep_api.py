"""A module to interact with Financial Modeling Prep API"""

from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("FINANCE_MODELING_PREP_API_KEY")
