import streamlit as st
import pandas as pd
from io import BytesIO

# Note: Requires 'openpyxl' for Excel writing. Install with: pip install openpyxl

st.title("Disease Features Cleaner (Excel)")

uploaded_file = st.file_uploader("Upload your disease_features.xlsx file", type=["xlsx"])

if uploaded_file is not None:
    try:
        # Read Excel file (skip header row)
        df = pd.read_excel(uploaded_file, header=None, skiprows=1)
        
        # Strip whitespace from all string cells
        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        
        # Count completely duplicate rows
        total_duplicates = df.duplicated().sum()
        st.write(f"Completely duplicate rows found: {total_duplicates}")
        
        # Remove completely duplicate rows (keeping first occurrence)
        df_cleaned = df.drop_duplicates(keep='first')
        
        st.write(f"Removed {len(df)-len(df_cleaned)} completely duplicate rows")
        st.write(f"Original: {len(df)} rows | Cleaned: {len(df_cleaned)} rows")
        
        # Download cleaned data as Excel
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:  # type: ignore
            df_cleaned.to_excel(writer, index=False, header=False)
        output.seek(0)
        st.download_button(
            label="Download Cleaned Excel",
            data=output,
            file_name="disease_features_cleaned.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    except Exception as e:
        st.error(f"Error: {str(e)}")
else:
    st.info("Please upload an Excel file to begin.")