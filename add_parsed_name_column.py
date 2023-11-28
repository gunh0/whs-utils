import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("result.csv")

# Extract the "Title" column
df["Parsed Name"] = df["Title"].str.extract(r"([ㄱ-힣]{3})/")

# Display the DataFrame
print(df)

# Save the DataFrame back to the CSV file
df.to_csv("result_with_parsed_names.csv", index=False)
