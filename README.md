# STUDENTS EXAM PERFORMANCE REPORT

A comprehensive report analyzing student exam performance across different genders. This report visualizes the relationship between attendance, exam scores, and study hours for male and female students.

## Features

- **Attendance Analysis**: Compare average attendance rates by gender
- **Exam Score Analysis**: Analyze exam performance differences between genders
- **Study Hours Analysis**: Compare average study hours invested by each gender
- **Visual Graphs**: Clear bar charts showing all three metrics side by side

## Requirements

- Python 3.7+
- pandas
- matplotlib
- numpy

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Michael-7ke/STUDENTS-EXAM-PREDICTION-REPORT.git
cd STUDENTS-EXAM-PREDICTION-REPORT
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the report generation script:
```bash
python generate_report.py
```

This will:
1. Load student data from `student_data.csv`
2. Calculate statistics by gender
3. Generate visualizations showing attendance, exam scores, and study hours
4. Save the report as `exam_performance_report.png`

## Data Format

The `student_data.csv` file contains the following columns:
- `student_id`: Unique identifier for each student
- `gender`: Student's gender (Male/Female)
- `attendance`: Attendance percentage
- `exam_score`: Exam score (0-100)
- `study_hours`: Hours spent studying per week

## Output

The script generates a comprehensive report with three side-by-side graphs:
1. **Average Attendance by Gender**: Shows attendance percentages
2. **Average Exam Score by Gender**: Displays exam performance
3. **Average Study Hours by Gender**: Compares study time investment

## Sample Data

The repository includes sample data for 30 students (15 male, 15 female) with realistic performance metrics.
