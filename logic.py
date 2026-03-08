import pandas as pd

def process_attendance(file):
    # Unga image-la headers 2nd row-la irukku, so header=1 (index starts from 0)
    if file.name.endswith('.csv'):
        df = pd.read_csv(file, header=1)
    else:
        df = pd.read_excel(file, header=1)
    
    # 1. Clean empty rows (Oru vaela empty rows irundha remove pannum)
    df = df.dropna(subset=['Student Name'])

    # 2. Columns-a rename panrom code readability-kaga
    df = df.rename(columns={'Student Name': 'Student_Name'})
    
    # 3. Date columns-a identify panrom (Numbers 1 to 31)
    # Excel-la numbers integer-ah irukkum, adha string-ah mathi filter panrom
    day_cols = [c for c in df.columns if str(c).isdigit()]
    
    # 4. 🔥 'p'-a count panra logic
    # Strip() - space irundha remove pannum, Lower() - 'P' or 'p' rendaiyum eduthukkum
    def count_present(row):
        return sum(1 for val in row[day_cols] if str(val).strip().lower() == 'p')

    df['Present_Days'] = df.apply(count_present, axis=1)
    df['Total_Working_Days'] = len(day_cols)
    df['Attendance_Percentage'] = (df['Present_Days'] / df['Total_Working_Days']) * 100
    
    # 5. AI Risk Status Logic
    def attendance_risk(pct):
        if pct < 75: return "🔴 Shortage (High Risk)"
        elif pct < 85: return "🟡 Borderline"
        return "🟢 Good"
        
    df['Attendance_Status'] = df['Attendance_Percentage'].apply(attendance_risk)
    
    # Output Table
    return df[['Student_Name', 'Present_Days', 'Total_Working_Days', 'Attendance_Percentage', 'Attendance_Status']]
