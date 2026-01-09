from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Attendance
from .forms import StudentForm, AttendanceForm
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa



# =========================
# STUDENT CRUD VIEW
# =========================

def home_view(request):
    return render(request, 'home.html')


def student_view(request):
    action = request.GET.get('action')
    student_id = request.GET.get('id')

    # CREATE
    if action == 'add' and request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/students/')

    # EDIT
    elif action == 'edit' and student_id:
        student = get_object_or_404(Student, id=student_id)

        if request.method == 'POST':
            form = StudentForm(request.POST, instance=student)
            if form.is_valid():
                form.save()
                return redirect('/students/')
        else:
            form = StudentForm(instance=student)

        students = Student.objects.all()
        return render(request, 'students.html', {
            'form': form,
            'students': students,
            'edit_mode': True,
            'edit_id': student.id
        })

    # DELETE
    elif action == 'delete' and student_id:
        student = get_object_or_404(Student, id=student_id)
        student.delete()
        return redirect('/students/')

    # READ / LIST
    form = StudentForm()
    students = Student.objects.all()
    return render(request, 'students.html', {'form': form, 'students': students})


# =========================
# ATTENDANCE VIEW
# =========================
def attendance_view(request):
    action = request.GET.get('action')
    attendance_id = request.GET.get('id')

    # =======================
    # EDIT ATTENDANCE
    # =======================
    if action == 'edit' and attendance_id:
        attendance = get_object_or_404(Attendance, id=attendance_id)

        if request.method == 'POST':
            form = AttendanceForm(request.POST, instance=attendance)
            if form.is_valid():
                form.save()
                return redirect('/attendance/')
        else:
            form = AttendanceForm(instance=attendance)

        attendance_list = Attendance.objects.select_related('student').order_by('-date')

        return render(request, 'attendance.html', {
            'form': form,
            'attendance_list': attendance_list,
            'edit_mode': True,
            'edit_id': attendance.id
        })

    # =======================
    # DELETE ATTENDANCE
    # =======================
    if action == 'delete' and attendance_id:
        attendance = get_object_or_404(Attendance, id=attendance_id)
        attendance.delete()
        return redirect('/attendance/')

    # =======================
    # CREATE ATTENDANCE
    # =======================
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/attendance/')

    # =======================
    # LIST ATTENDANCE
    # =======================
    form = AttendanceForm()
    attendance_list = Attendance.objects.select_related('student').order_by('-date')

    return render(request, 'attendance.html', {
        'form': form,
        'attendance_list': attendance_list
    })

def export_attendance_pdf(request):
    attendance_list = Attendance.objects.select_related('student').order_by('-date')

    template_path = 'attendance_pdf.html'
    context = {
        'attendance_list': attendance_list
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="attendance_report.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors while generating the PDF')
    return response