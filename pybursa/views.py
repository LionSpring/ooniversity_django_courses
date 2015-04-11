from django.shortcuts import render

from courses.models import Course, Lesson
from students.models import Student


# Ooniversity site pages - Django Control 5

def ooniversity(request):
    courses = Course.objects.all()
    return render(request, 'courses/ooniversity.html', {'courses': courses})

def course(request, id_course):
    id_course_int = int(id_course)
    course = Course.objects.get(id = id_course_int)
    lessons = Lesson.objects.filter(course__title = course.title)
    return render(request, 'courses/courses.html', {'course': course, 'lessons': lessons})

def students(request):
    if request.GET.get('course_id') != None:
        request_int = int(request.GET.get('course_id'))
        students = Student.objects.filter(courses__id = request_int)
        return render(request, 'students/students.html', {'students': students})
    else:
        students = Student.objects.all()
        return render(request, 'students/students.html', {'students': students})

def student_info(request, id_stud):
    id_stud_int = int(id_stud)
    student = Student.objects.get(id = id_stud_int)
    return render(request, 'students/student_info.html', {'student': student})



# PyBursa site pages - Django Control 3

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def student_detail(request):
    return render(request, 'student_detail.html')

def student_list(request):
    return render(request, 'student_list.html')
