# This file is used to set environment variables for the Django project. 
# It helps in switching between development (SQLite) and production (PostgreSQL) databases 
# without modifying the Django settings file directly.
#
# How to use:
# - To use SQLite for local development, ensure DEV_DB is set to "True".
# - To use PostgreSQL, set DEV_DB to "False" or remove it entirely.
# - Modify values as needed before running the Django server.
# - Environment variables can also be overridden by system-wide settings.

import os

ENV_SETTINGS = {
    # Control Django DEBUG mode
    "DEBUG": os.getenv("DEBUG", "True"),  # Defaults to True if not set

    # Use SQLite for local development
    "DEV_DB": os.getenv("DEV_DB", "True"),  # Defaults to True if not set
    
    # PostgreSQL connection string (used in production)
    #"DATABASE_URL": os.getenv(
    #    "DATABASE_URL",
    #    "postgresql://lazydog_db_owner:9FwfN1bxsqeo"
    #    "@ep-rapid-block-a26wpvv9.eu-central-1.aws.neon.tech"
    #    "/lazydog_db?sslmode=require"
    #),
    
    # Django secret key
    #"SECRET_KEY": os.getenv("SECRET_KEY", "jorgenjorgen123"),
}

# Set environment variables in the system
for key, value in ENV_SETTINGS.items():
    os.environ[key] = value