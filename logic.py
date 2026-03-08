import pandas as pd

def process_attendance(file):
    # Excel or CSV read panrom
    df = pd.read_csv(file) if file.name.endswith('.csv') else pd.read_excel(file)
    
    # 1 to 31 dates columns-a identify panrom
    day_cols = [str(i) for i in range(1, 32) if str(i) in df.columns]
    
    # 🔥 Logic: 'P' count panni percentage mathurom
    # Case-insensitive (p or P) handle pannum
    df['Present_Days'] = df[day_cols].apply(lambda x: x.astype(str).str.upper().value_counts().get('P', 0), axis=1)
    df['Total_Working_Days'] = len(day_cols)
    df['Attendance_Percentage'] = (df['Present_Days'] / df['Total_Working_Days']) * 100
    
    # AI Risk based on Attendance alone
    def attendance_risk(pct):
        if pct < 75: return "🔴 Shortage (High Risk)"
        elif pct < 85: return "🟡 Borderline"
        return "🟢 Good"
        
    df['Attendance_Status'] = df['Attendance_Percentage'].apply(attendance_risk)
    
    return df[['Student_Name', 'Present_Days', 'Total_Working_Days', 'Attendance_Percentage', 'Attendance_Status']]
