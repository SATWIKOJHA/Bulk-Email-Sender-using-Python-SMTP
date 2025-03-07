import pandas as pd

# Load the CSV file and clean bad rows
csv_file = "cleaned_hr_contacts.csv"

try:
    df = pd.read_csv(csv_file, on_bad_lines="skip", delimiter=",", dtype=str)  
except Exception as e:
    print(f"❌ Error reading CSV: {e}")
    exit()

# Drop rows where essential fields (Email, Name, Company) are missing
df = df.dropna(subset=["Email", "Name", "Company"])

# Save the fully cleaned CSV
cleaned_file = "fully_cleaned_hr_contacts.csv"
df.to_csv(cleaned_file, index=False)

print(f"✅ Fully cleaned CSV saved as '{cleaned_file}'")
