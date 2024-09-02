import pandas as pd

# Replace 'your_file.csv' with the actual path to your CSV file
file_path = 'QA_options.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# # Split the 'Incorrect Answers' column into separate columns
# split_incorrect = df['Correct Answers'].str.split(';', expand=True)

# # Rename the new columns (if there are up to 4 incorrect answers)
# split_incorrect.columns = [f'Correct_Answer_{i+1}' for i in range(split_incorrect.shape[1])]

# Concatenate the split columns back to the original dataframe
# df = pd.concat([df, split_incorrect], axis=1)
# Drop the original 'answers' column if needed
# Concatenate Column1 and Column2, separated by a semicolon
# df['Options'] = df['Incorrect Answers'].astype(str) + ';' + df['Best Answer'].astype(str)
# Drop the original columns
df.drop(columns=['Source'], inplace=True)

# Save the new DataFrame to a new CSV file
df.to_csv('QA_options.csv', index=False)