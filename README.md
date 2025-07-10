# Grade Distribution Analyzer

A Flask web application that helps students and educators visualize and understand grade distributions through statistical analysis and interactive charts.

## Features

- **Statistical Analysis**: Calculates mean, median, standard deviation, minimum, maximum, and count
- **Visual Distribution**: Generates histogram charts with mean and median indicators
- **Interactive Interface**: Clean, responsive web interface for easy grade input
- **Real-time Results**: Instant analysis and visualization of grade data
- **Educational Value**: Helps students understand statistical concepts and data distribution

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone or download the repository**
   ```bash
   cd grade_distribution_analyzer
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the application**
   ```bash
   python app.py
   ```

2. **Access the application**
   Open your web browser and navigate to: `http://localhost:8080`

3. **Analyze grades**
   - Enter comma-separated grades in the text area
   - Click "Analyze Grades" to see results
   - View statistical measures and histogram visualization

## Example Input

```
85, 92, 78, 88, 95, 82, 90, 87, 91, 84
```

## Technical Details

### Dependencies
- **Flask**: Web framework for Python
- **NumPy**: Numerical computing library for statistical calculations
- **Matplotlib**: Plotting library for creating histograms

### Architecture
- **Backend**: Flask application with two routes:
  - `/` - Serves the main interface
  - `/analyze` - Processes grade data and returns JSON results
- **Frontend**: HTML template with embedded CSS and JavaScript
- **Data Flow**: Form submission → Flask processing → JSON response → Dynamic UI update

### Statistical Measures
- **Mean**: Average of all grades
- **Median**: Middle value when grades are sorted
- **Standard Deviation**: Measure of grade distribution spread
- **Min/Max**: Lowest and highest grades
- **Count**: Total number of grades

## File Structure

```
grade_distribution_analyzer/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Web interface template
└── venv/              # Virtual environment (if created)
```

## Educational Purpose

This application demonstrates:
- Statistical concepts (central tendency, variability)
- Data visualization principles
- Web application development with Flask
- Frontend-backend communication
- Responsive web design

## Development

To modify the application:
1. Edit `app.py` for backend changes
2. Edit `templates/index.html` for frontend changes
3. Update `requirements.txt` for new dependencies
4. Test changes by restarting the Flask server

## Troubleshooting

- **Port conflicts**: If port 8080 is in use, modify the port in `app.py`
- **Module not found**: Ensure virtual environment is activated and dependencies are installed
- **Plotting errors**: Matplotlib uses 'Agg' backend for web compatibility

## License

Created with Claude Code for educational purposes.