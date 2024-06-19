# Building An API in Flask

## Getting started

1. Clone this repo, or select "Use Template" on the top-right.
2. When you have your repo, select the "Code" dropdown and swap to the "Codespaces" tab.
3. Click "Create Codespace on main"

## Running this project

1. Open a terminal and run `python -m venv ./venv` to create a virtual environment.
2. After that, enter `source .venv/bin/activate` to activate the environment.
3. Once you have that set up, you can use `pip install -r requirements.txt` to install the project requirements.
4. Once the packages have installed (and we've gotten the Flask app set up), run `flask --app main run --debug`

## Goals

- Build a simple CRUD API to allow users to perform the following functions:
  - CREATE a recipe
  - READ all recipes
  - READ a single recipe
  - UPDATE a single recipe
  - DELETE a single recipe
