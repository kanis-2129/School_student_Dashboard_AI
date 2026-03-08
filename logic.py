import pandas as pd

# --- Logic 1: ERP Attendance Processor ---
def process_attendance(file):
    df = pd.read_csv(file) if file.name.endswith('.csv') else pd.read_excel(file)
    # 1 to 31 dates columns-a mattum filter panrom
    day_cols = [str(i) for i in range(1, 32) if str(i) in df.columns]
    # 'P'-a count panni percentage calculate panrom
    df['Present_Count'] = df[day_cols].apply(lambda x: x.astype(str).str.upper().value_counts().get('P', 0), axis=1)
    df['Total_Days'] = len(day_cols)
    df['Attendance_%'] = (df['Present_Count'] / df['Total_Days']) * 100
    return df[['Student_Name', 'Present_Count', 'Attendance_%']]

# --- Logic 2: AI Risk Prediction (Marks + Attendance) ---
def get_ai_prediction(att_df, marks_df):
    # Rendu file-ayum Student Name vachi join panrom
    final_df = pd.merge(att_df, marks_df, on="Student_Name")
    
    def predict_status(row):
        # AI Logic: Multi-condition check
        if row['Attendance_%'] < 75 or row['HalfYearly_Marks'] < 40:
            return "🔴 High Risk (Needs Help)"
        elif row['HalfYearly_Marks'] < row['Quarterly_Marks']:
            return "🟡 Performance Dropping"
        else:
            return "🟢 Safe & Steady"
            
    final_df['AI_Status'] = final_df.apply(predict_status, axis=1)
    return final_df
