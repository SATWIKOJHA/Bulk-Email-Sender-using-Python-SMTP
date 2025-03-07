import pandas as pd

# Load the CSV file
csv_file = "hr_contacts.csv"  # Ensure this file is in the same folder
try:
    df = pd.read_csv(csv_file, error_bad_lines=False, warn_bad_lines=True)  # Remove bad rows
except Exception as e:
    print(f"❌ Error reading CSV: {e}")
    exit()

# Save the cleaned file
cleaned_csv_file = "cleaned_hr_contacts.csv"
df.to_csv(cleaned_csv_file, index=False)

print(f"✅ CSV file cleaned and saved as '{cleaned_csv_file}'")
