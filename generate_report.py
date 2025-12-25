import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_data():
    """Load student data from CSV file"""
    df = pd.read_csv('student_data.csv')
    return df

def create_performance_report():
    """Generate exam performance report with visualizations"""
    # Load data
    df = load_data()
    
    # Calculate statistics by gender
    gender_stats = df.groupby('gender').agg({
        'attendance': 'mean',
        'exam_score': 'mean',
        'study_hours': 'mean'
    }).round(2)
    
    print("=" * 60)
    print("STUDENT EXAM PERFORMANCE REPORT")
    print("=" * 60)
    print("\nStatistics by Gender:")
    print(gender_stats)
    print("\n")
    
    # Create visualizations
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle('Student Exam Performance Report by Gender', fontsize=16, fontweight='bold')
    
    # 1. Attendance by Gender
    gender_groups = df.groupby('gender')['attendance'].mean()
    colors = ['#3498db', '#e74c3c']
    axes[0].bar(gender_groups.index, gender_groups.values, color=colors, alpha=0.7, edgecolor='black')
    axes[0].set_title('Average Attendance by Gender', fontweight='bold')
    axes[0].set_xlabel('Gender')
    axes[0].set_ylabel('Attendance (%)')
    axes[0].set_ylim(0, 100)
    axes[0].grid(axis='y', alpha=0.3)
    for i, v in enumerate(gender_groups.values):
        axes[0].text(i, v + 1, f'{v:.1f}%', ha='center', va='bottom', fontweight='bold')
    
    # 2. Exam Score by Gender
    exam_groups = df.groupby('gender')['exam_score'].mean()
    axes[1].bar(exam_groups.index, exam_groups.values, color=colors, alpha=0.7, edgecolor='black')
    axes[1].set_title('Average Exam Score by Gender', fontweight='bold')
    axes[1].set_xlabel('Gender')
    axes[1].set_ylabel('Exam Score')
    axes[1].set_ylim(0, 100)
    axes[1].grid(axis='y', alpha=0.3)
    for i, v in enumerate(exam_groups.values):
        axes[1].text(i, v + 1, f'{v:.1f}', ha='center', va='bottom', fontweight='bold')
    
    # 3. Study Hours by Gender
    study_groups = df.groupby('gender')['study_hours'].mean()
    axes[2].bar(study_groups.index, study_groups.values, color=colors, alpha=0.7, edgecolor='black')
    axes[2].set_title('Average Study Hours by Gender', fontweight='bold')
    axes[2].set_xlabel('Gender')
    axes[2].set_ylabel('Study Hours')
    axes[2].set_ylim(0, 30)
    axes[2].grid(axis='y', alpha=0.3)
    for i, v in enumerate(study_groups.values):
        axes[2].text(i, v + 0.5, f'{v:.1f}h', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('exam_performance_report.png', dpi=300, bbox_inches='tight')
    print("Report saved as 'exam_performance_report.png'")
    plt.show()

if __name__ == "__main__":
    create_performance_report()
