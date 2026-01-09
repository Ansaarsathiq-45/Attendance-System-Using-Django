from django.db import models


class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    DEPARTMENT_CHOICES = [
        ('CSE', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('ECE', 'Electronics & Communication'),
        ('EEE', 'Electrical & Electronics'),
        ('MECH', 'Mechanical'),
        ('CIVIL', 'Civil'),
        ('AI&DS', 'AI & Data Science'),
    ]

    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField(verbose_name="Date of Birth")
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)
    address = models.TextField()
    join_date = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    marks = models.IntegerField(default=0)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.roll_no})"


class Attendance(models.Model):
    STATUS_CHOICES = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"
