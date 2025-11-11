# Solar Challenge Week 0

This repository contains the **Solar Challenge Week 0** project. The project focuses on performing **Exploratory Data Analysis (EDA)** on solar radiation and meteorological data across multiple countries. It includes data cleaning, visualization, and cross-country analysis.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Folder Structure](#folder-structure)  
3. [Environment Setup (Conda)](#environment-setup-conda)  
4. [Usage](#usage)  
5. [Example Output](#example-output)  
6. [Running Tests](#running-tests)  
7. [Contributing](#contributing)  
8. [License](#license)  

---

## Project Overview

The goals of this project are:

- Analyze solar radiation and weather data for multiple countries.  
- Generate summary statistics and visualizations.  
- Compare trends across countries in a structured way.  
- Create clean, reproducible analysis scripts.  
- (Optional) Prepare interactive dashboards for visual insights.

---

## Folder Structure

```text
solar-challenge-week0/
├── data/                  # Raw and cleaned datasets
├── notebooks/             # Jupyter notebooks for EDA and analysis
├── scripts/               # Python scripts for data cleaning, visualization
├── tests/                 # Unit tests for functions and scripts
├── outputs/               # Generated plots, tables, and reports
├── requirements.txt       # Python dependencies
├── main.py                # Main script to run the project
└── README.md              # Project documentation

# 1. Clone the repository
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# 2. Create a conda environment with Python 3.11
conda create --yes --name solar-env python=3.11

# 3. Activate the environment
conda activate solar-env

# 4. Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# 5. (Optional) Install common packages if requirements.txt doesn't exist
pip install requests flask pytest pandas matplotlib seaborn

# 6. Freeze installed packages into requirements.txt
pip freeze > requirements.txt

# 7. Verify the environment
python --version
pip --version
pip list

python main.py


