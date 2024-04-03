import os
from dotenv import load_dotenv

load_dotenv()


# Global DEBUG mode
ENV_DEBUG = os.getenv('DEBUG')

# DB connection settings
ENV_DB_NAME = os.getenv('DB_NAME')
ENV_DB_USER = os.getenv('DB_USER')
ENV_DB_PASSWORD = os.getenv('DB_PASS')
ENV_DB_HOST = os.getenv('DB_HOST')
ENV_DB_PORT = os.getenv('DB_PORT')

# Django configuration
ENV_DJ_SECRET = os.getenv('DJ_SECRET')

# App cofiguration
BOT_AGENT_NAME = os.getenv('BOT_AGENT_NAME')

# API Ninjas configuration
API_N_TOKEN = os.getenv('API_N_TOKEN')
