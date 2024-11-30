import pandas as pd

# Load the Titanic dataset
titanic_path = '/Users/lorenzoferrantin/Python-Data-Science-Session6/train_and_test2.csv'
titanic_df = pd.read_csv(titanic_path)

# 1. Calculate Gender-Based Survival Percentage
gender_survival = titanic_df.groupby('Sex')['2urvived'].mean() * 100
print("Gender-Based Survival Percentage:")
print(gender_survival)

# 2. Calculate Survival Percentage Grouped by Gender and Class
gender_class_survival = titanic_df.groupby(['Sex', 'Pclass'])['2urvived'].mean() * 100
print("\nSurvival Percentage Grouped by Gender and Class:")
print(gender_class_survival)

# 3. Count the Missing Values in Each Column
missing_values = titanic_df.isna().sum()
print("\nMissing Values in Each Column:")
print(missing_values)

# 4. Fill Missing 'Age' Values with the Mean Age
titanic_df['Age'] = titanic_df['Age'].fillna(titanic_df['Age'].mean())
print("\nMissing 'Age' values filled with mean.")

# 5. Fill Missing 'Embarked' Values with the Mode
mode_embarked = titanic_df['Embarked'].mode()[0]
titanic_df['Embarked'] = titanic_df['Embarked'].fillna(mode_embarked)
print("Missing 'Embarked' values filled with mode.")

# 6. Filter and Display Passengers Who Paid a Fare Above the Average Fare
average_fare = titanic_df['Fare'].mean()
high_fare_passengers = titanic_df[titanic_df['Fare'] > average_fare]
print("\nPassengers Who Paid a Fare Above the Average Fare:")
print(high_fare_passengers)

# 7. Add a New Column Indicating Family Size
titanic_df['FamilySize'] = titanic_df['sibsp'] + titanic_df['Parch']
print("\nNew column 'FamilySize' added.")