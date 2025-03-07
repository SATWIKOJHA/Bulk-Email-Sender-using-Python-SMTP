import pandas as pd

csv_file = "fully_cleaned_hr_contacts.csv"  # Ensure this is the correct file

try:
    df = pd.read_csv(csv_file)
    print("✅ CSV Column Names:", df.columns.tolist())
except Exception as e:
    print(f"❌ Error reading CSV: {e}")
