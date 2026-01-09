# Attendance System Using Django

A complete **Student Management & Attendance System** built using **Django (Function-Based Views)**.  
This project supports **Student CRUD operations**, **Attendance marking**, and **PDF export** functionality.

---

## 🚀 Features

- Student Management (Add, Edit, Delete, View)
- Attendance Management (Mark Present/Absent)
- Attendance List View
- Export Attendance Report to PDF
- PostgreSQL / SQLite Database Support
- Clean UI using HTML & CSS
- Function-Based Views (No API)

---

## 🛠️ Technologies Used

- Python 3
- Django
- HTML5, CSS3
- PostgreSQL / SQLite
- xhtml2pdf (for PDF export)

---

## 📁 Project Structure

Attendance-System-Using-Django/
│
├── student_crud/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── students/
│ ├── migrations/
│ ├── templates/
│ │ ├── students.html
│ │ ├── student_list.html
│ │ ├── attendance.html
│ │ └── attendance_pdf.html
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── forms.py
│
├── manage.py
└── README.md

📄 Database Models
**Student**
1. Name
2. Roll Number
3. Email
4. Phone
5. Gender
6. Department
7. Date of Birth
8. Marks
9. Status

**Attendance**
1. Student (Foreign Key)
2. Date
3. Status (Present / Absent)

**📤 Export PDF**
Attendance report can be exported as PDF using xhtml2pdf library.

🧑‍💻 Author
Ansaar Sathiq Batcha
GitHub: [Ansaarsathiq-45](https://github.com/Ansaarsathiq-45)
