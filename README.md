
# Project Title
This project involves building an attendance system which utilizes facial recognition to mark the Attendance of Students.
When students enter the classroom, a teacher may take their attendance, and it can also collect the attendance of several
pupils at the same time.
It covers facial detection and recognition along with the development of a web application to cater to various use cases 
of the system such as adding new Staff, Students,Courses,Subjects,etc.by the Hod, viewing attendance reports, etc.





## Features

The system mainly works around 3 types of users

1.Hod
2.Staff
3.Student

For logging into the system, you'll need an email address and a password.

1.Hod (email = a@gmail.com, password=12345)

2.Staff (email = ashok@gmail.com, password=12345)

3.Student(email = ag@gmail.com, password=12345)


## Project specifications

1.Visual Studio Installer

![visual studio](https://user-images.githubusercontent.com/104299247/170819588-4e2d10b3-2779-4431-9785-e73134844b30.jpg)

2.Your photo must be in jpg format and saved in the student_images folder with your name (ex. Rishika.jpg).

## Running / Way to Execute

1.install the required libraries(requirements.txt) using the command:
  pip3 install -r requirements.txt

  and run the following command in the command prompt (make sure you are in student directory of project):
  python manage.py runserver

2.Click on Take Attendance after logging in with the staff email address and password.

3.To create your own credential for logging into the application:
  python manage.py createsuperuser 
  
4.After taking attendance, we must hit the Esc key to switch off the cemra.
