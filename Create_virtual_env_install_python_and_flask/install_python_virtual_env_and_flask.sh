#!/bin/bash

# 1. Update and Upgrade the System
sudo apt-get update
sudo apt-get upgrade -y

# 2. Install Python
sudo apt-get install python3 python3-pip -y

# 3. Install Virtual Environment
sudo apt-get install python3-venv -y

# 4.  Create a Virtual Environment
mkdir my_flask_app
cd my_flask_app
python3 -m venv venv

# 5. Activate the Virtual Environment
source venv/bin/activate

# 6. Install Flask and requests module
pip install Flask requests

# 7. Verify Installation
flask --version



