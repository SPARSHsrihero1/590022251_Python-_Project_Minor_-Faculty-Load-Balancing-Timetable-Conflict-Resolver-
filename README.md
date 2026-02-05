# Faculty Load Balancing System using Python 
Date: 05 Feb, 2026 !st year, 2nd Sem

A simple Python-based system designed to analyze faculty teaching workload and suggest better distribution of classes to reduce overload and manual effort in colleges.

---

## 📌 Problem Statement

In day-to-day college life, classes often get rescheduled or cancelled because some faculty members are overloaded while others have comparatively fewer teaching hours. Faculty may also feel stressed due to uneven workload distribution. Since workload management is usually handled manually, identifying such issues and correcting them takes time and effort.

---

## 🎯 Objective

The objective of this project is to create a simple, menu-driven Python application that:
- Stores faculty teaching data day-wise
- Calculates total weekly teaching workload
- Identifies overloaded faculty
- Suggests better workload distribution
- Reduces manual effort in workload management
- Generates a clear and readable report

---

## ⚙️ Features

- Add faculty teaching data
- Update faculty data  
  - Update all existing days  
  - Update a specific day  
  - Add new teaching days
- View faculty details
- Calculate weekly teaching workload
- Generate **multiple realistic load-balancing suggestions**
- Generate a text-based report (`report.txt`)
- Simple, user-friendly, menu-driven interface

---

## 🛠️ Technologies Used

- **Programming Language:** Python  
- **Concepts Used:**  
  - Dictionaries  
  - Functions  
  - Loops  
  - Conditional statements  
  - File handling  
  - Menu-driven programming  

No external libraries are required.

---

## ▶️ How to Run the Project


1. Make sure Python is installed on your system.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Run the program using:
bash
python faculty_load_balancer.py
Follow the on-screen menu instructions.

📊 Sample Output

====== MENU ======
1. Add Faculty Data
2. Update Faculty Data
3. View Faculty Details
4. Calculate Faculty Workload
5. Suggest Load Balancing
6. Generate Report
7. Exit

Faculty Workload:
IR: 48 hours/week
AB: 14 hours/week

📄 Report Generation
The program generates a file named report.txt which contains:

Faculty name
Total weekly teaching load
Day-wise teaching hours

Sample report.txt
yaml
Copy code
FACULTY LOAD BALANCING REPORT

Faculty: IR
Total Load: 48 hours/week
Mon: 8 hours
Tue: 8 hours
Wed: 8 hours
Thu: 8 hours
Fri: 8 hours
Sat: 8 hours

🔍 Project Scope Clarification

This project focuses on workload-based analysis, not exact time-slot conflict detection.
Teaching hours are used as the primary metric, which is commonly used in academic workload management.
Time-slot based conflict detection can be added as a future enhancement.

🚀 Future Scope

Time-slot based timetable conflict detection
Database integration for persistent data storage
Web-based interface for easier access
Department-wise and subject-wise workload analysis
Graphical workload visualization

👨‍🏫 Conclusion

This project successfully demonstrates how basic Python programming can be used to solve real-world problems in an academic environment. By automating workload calculation and providing practical suggestions, the system helps reduce manual effort and supports fair distribution of teaching responsibilities.
