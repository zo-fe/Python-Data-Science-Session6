# Python-Data-Science-Session6

This repository contains exercises and solutions for the **Netflix** and **Titanic** datasets as part of **Session 6** of Python for Data Science. The exercises focus on data manipulation and analysis using Pandas.

## Files
- `exercise_netflix.py`: Python script for Netflix dataset analysis.
- `exercise_titanic.py`: Python script for Titanic dataset analysis.
- `netflix_titles.csv`: Dataset containing Netflix title information.
- `train_and_test2.csv`: Titanic dataset for survival analysis.

## Netflix Exercises
1. Check for missing ratings.
2. Count the number of films from 2021 corresponding to Italy.
3. Determine the number of movies in 2020 with complete information.
4. Identify the year with the most titles released.
5. Calculate the average number of releases per year since 2010.

## Titanic Exercises
1. Calculate survival percentage based on gender.
2. Calculate survival percentages grouped by gender and passenger class.
3. Count the missing values in each column.
4. Fill missing 'Age' values with the mean age.
5. Fill missing 'Embarked' values with the most common value (mode).
6. Filter and display passengers who paid a fare above the average.
7. Add a new column `FamilySize` (sum of `sibsp` and `Parch`).

## Requirements
- Python 3.x
- Pandas

## How to Run
1. Clone the repository:
   git clone https://github.com/zo-fe/Python-Data-Science-Session6.git
2. Navigate to the project directory:
   cd Python-Data-Science-Session6
3. Run the scripts:
   - For Netflix:
     python exercise_netflix.py
   - For Titanic:
     python exercise_titanic.py
