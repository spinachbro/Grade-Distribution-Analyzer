"""
Grade Distribution Analyzer - Flask Web Application

This Flask application helps students visualize and understand grade distributions
by calculating statistical measures and creating visual histograms from inputted grades.

Educational Purpose:
- Teaches students about statistical concepts (mean, median, standard deviation)
- Provides visual representation of data distribution
- Demonstrates how grades cluster around certain values
- Shows the relationship between different statistical measures

Author: Created with Claude Code
"""

# Import required libraries
from flask import Flask, render_template, request, jsonify  # Web framework components
import numpy as np  # Numerical computing library for statistical calculations
import matplotlib  # Plotting library
matplotlib.use('Agg')  # Set matplotlib to use non-interactive backend (required for web apps)
import matplotlib.pyplot as plt  # Plotting functions
import io  # Input/output operations for handling image data in memory
import base64  # For encoding images to base64 strings for web display

# Initialize Flask application
app = Flask(__name__)

@app.route('/')
def index():
    """
    Home page route that displays the main interface.
    
    Returns:
        HTML template with the grade input form and results display area
    """
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_grades():
    """
    Main analysis route that processes submitted grades and returns statistical analysis.
    
    This function:
    1. Receives comma-separated grades from the web form
    2. Converts them to a NumPy array for mathematical operations
    3. Calculates key statistical measures
    4. Creates a histogram visualization
    5. Returns both statistics and plot as JSON
    
    Returns:
        JSON response containing:
        - stats: Dictionary with mean, median, std dev, min, max, count
        - plot: Base64-encoded PNG image of the histogram
        - grades: List of processed grade values
        
    Error handling:
        - Returns error message for invalid input formats
        - Handles empty input gracefully
    """
    try:
        # Extract grades from form data submitted by the user
        grades_input = request.form['grades']
        
        # Parse the comma-separated string into a list of floating-point numbers
        # This comprehension splits by comma, strips whitespace, and converts to float
        # Only processes non-empty strings to avoid errors
        grades = [float(x.strip()) for x in grades_input.split(',') if x.strip()]
        
        # Validate that we have at least one grade to analyze
        if not grades:
            return jsonify({'error': 'Please enter valid grades'})
        
        # Convert Python list to NumPy array for efficient mathematical operations
        grades_array = np.array(grades)
        
        # Calculate comprehensive statistical measures using NumPy functions
        stats = {
            'mean': np.mean(grades_array),        # Average grade (sum ÷ count)
            'median': np.median(grades_array),    # Middle value when sorted
            'std': np.std(grades_array),          # Standard deviation (measure of spread)
            'min': np.min(grades_array),          # Lowest grade
            'max': np.max(grades_array),          # Highest grade
            'count': len(grades_array)            # Total number of grades
        }
        
        # Create histogram visualization using matplotlib
        fig, ax = plt.subplots(figsize=(10, 6))  # Create figure with specified size
        
        # Generate histogram with 10 bins
        # alpha=0.7 makes bars semi-transparent for better visual appeal
        ax.hist(grades_array, bins=10, alpha=0.7, color='skyblue', edgecolor='black')
        
        # Add vertical lines to show mean and median on the histogram
        # These help students visualize where the center of the distribution lies
        ax.axvline(stats['mean'], color='red', linestyle='--', linewidth=2, 
                  label=f'Mean: {stats["mean"]:.2f}')
        ax.axvline(stats['median'], color='green', linestyle='--', linewidth=2, 
                  label=f'Median: {stats["median"]:.2f}')
        
        # Label the axes and add title for clarity
        ax.set_xlabel('Grade')
        ax.set_ylabel('Frequency')  # How many students got grades in each range
        ax.set_title('Grade Distribution')
        
        # Add legend to explain the colored lines
        ax.legend()
        
        # Add grid for easier reading of values
        ax.grid(True, alpha=0.3)
        
        # Convert matplotlib plot to base64 string for web display
        # This process allows us to embed the image directly in the JSON response
        img_buffer = io.BytesIO()  # Create in-memory buffer
        plt.savefig(img_buffer, format='png', bbox_inches='tight')  # Save plot to buffer
        img_buffer.seek(0)  # Reset buffer position to beginning
        img_string = base64.b64encode(img_buffer.read()).decode()  # Encode as base64 string
        plt.close()  # Close the plot to free memory
        
        # Return all results as JSON for the frontend JavaScript to process
        return jsonify({
            'stats': stats,           # Statistical measures
            'plot': img_string,       # Base64-encoded histogram image
            'grades': grades          # Original grade values for reference
        })
        
    except ValueError:
        # Handle cases where input cannot be converted to numbers
        return jsonify({'error': 'Please enter valid numeric grades separated by commas'})
    except Exception as e:
        # Catch any other unexpected errors and return them to the user
        return jsonify({'error': str(e)})

# Main application entry point
if __name__ == '__main__':
    # Run the Flask development server
    # host='0.0.0.0' makes it accessible from any network interface
    # port=8080 avoids conflicts with macOS Control Center on port 5000
    # debug=True enables automatic reloading and error details
    app.run(host='0.0.0.0', port=8080, debug=True)