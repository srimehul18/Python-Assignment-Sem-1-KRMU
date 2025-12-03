# Gradebook Analyzer

##  Overview
Gradebook Analyzer is a Python program designed to read student grade data, calculate performance metrics, and provide useful feedback. It supports operations like calculating average scores, identifying highest/lowest marks, and assigning letter grades based on overall performance.

This tool helps automate grading tasks and ensures accuracy in student assessment.

---

##  Features
- Read and store student grades
- Calculate individual average scores
- Assign letter grades (A, B, C, D, F)
- Identify highest and lowest scoring students
- Display formatted grade reports

---

##  Technologies Used
- **Python 3.14**
- Core Python features:
  - Lists
  - Dictionaries
  - Loops & Functions
  - Conditional Statements

---

## How the Program Works
1. Stores student names and their marks in different subjects
2. Calculates the average mark for each student
3. Uses a grading scale to assign a final letter grade:
   - `90–100` → A  
   - `80–89`  → B  
   - `70–79`  → C  
   - `60–69`  → D  
   - `< 60`   → F
4. Prints a structured report containing:
   - Student Name
   - Subject Marks
   - Average Score
   - Final Grade

---

## Running the Program
1. Install Python 3 if not already installed
2. Save the program file as `gradebook_analyzer.py`
3. Run the file in a terminal or editor:

---

### Developed by:
Mehul Srivastava
   ```bash
   python gradebook_analyzer.py
