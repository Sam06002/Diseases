# Disease Features Cleaner

A Streamlit web application for cleaning and removing duplicate rows from disease features datasets.

## Features

- **Excel File Support**: Upload and process `.xlsx` files
- **Duplicate Detection**: Automatically identifies and removes completely duplicate rows
- **Whitespace Cleaning**: Strips whitespace from all cells for better duplicate detection
- **Web Interface**: User-friendly Streamlit web interface
- **Download Results**: Download cleaned files directly from the web app

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Sam06002/Diseases.git
cd Diseases
```

2. Install required dependencies:
```bash
pip install streamlit pandas openpyxl
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run disease.py
```

2. Open your browser and navigate to `http://localhost:8502`

3. Upload your Excel file (`disease_features.xlsx`) using the file uploader

4. The app will:
   - Read the Excel file (skipping the first row)
   - Strip whitespace from all cells
   - Remove completely duplicate rows
   - Display statistics about duplicates found and removed
   - Provide a download button for the cleaned file

## File Structure

- `disease.py` - Main Streamlit application
- `disease_features.xlsx` - Sample input file (if available)
- `disease_features_cleaned.xlsx` - Output file after cleaning

## How It Works

The application processes Excel files by:
1. Reading the uploaded file with pandas
2. Stripping whitespace from all string cells
3. Identifying completely duplicate rows (all columns match)
4. Keeping only the first occurrence of each unique row
5. Allowing users to download the cleaned dataset

## Requirements

- Python 3.7+
- streamlit
- pandas
- openpyxl

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE). 