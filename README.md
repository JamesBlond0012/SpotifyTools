# Spotify tools

This repo contains tools that utilize the SpotiPy library to comunicate with the Spotify API, analyses the user's library and gathers data.

## DuplicateChecker.py

This is a simple script that goes through all your libraries and finds duplicate songs. Duplicate songs are defined as songs that have the exact same title and author.

## Virtual environments

It is recommended to use virtual environments when running these scripts. A virtual environments allows you to install packages without the need of installing them for the whole system.

To set up the virtual environment:

```sh
# Creates a .venv folder containing the virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate # Linux
.\.venv\bin\activate.ps1  # Windows

# Install the required packages
pip install -r requirements.txt
```

A lot of functions require a Spotify API key. Get your credentials and put them in a `.env` file, like described in the `.env.default` file.

