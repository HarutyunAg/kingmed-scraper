#!/bin/bash

echo "Create and activate a virtual environment using Poetry"
cd ./deps || exit
poetry install
poetry shell

cd ..
echo "Run the main.py file"
python main.py
