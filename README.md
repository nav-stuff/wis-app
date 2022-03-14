# WIS APP

## Problem statement
### Scenario: Western Institute of Studies (WIS)

Western Institute of Studies (WIS) is a fictitious tertiary educational institute. The WIS is one of the newly established New Zealand’s educational institute. WIS offers the following programs: two 6- months certificate (certificate in IT and certificate in business), and four 1-year diploma programmes (diploma in IT level 5, diploma in IT level 6, diploma in Business level 5, diploma in business level 6).

Due to the growth (increase number of students) it has become difficult for WIS management and staff to manage programs, lecturers, courses, students, and their marks manually. Therefore, the management team of WIS has decided to use automation software to run their business operations.

As a software developer, you are required to develop  a web-based application for WIS. The application should mainly consists of 6 modules: Programs, Lecturer’s information, Student’s information, Student Marks, and Students’ parent information and students’ tuition fee.

**For developing a web-based application for WIS**, you have to work in a team together with other two (2) software developers i.e. Michael and Jimmy. Your team have planned to develop a web application using open source technologies such as PHP as server-side script, and MySQL in the back-end. 

For code integration and delivery, Michael and Jimmy are keen to use continuous integration and delivery tools. You have been asked to attempt following task before starting web-based application development.

## DB Structure

Programs, Lecturer’s information, Student’s information, Student Marks, and Students’ parent information and students’ tuition fee.


- Students App
    - Student Table:
        - Name:
        - Father Name:
        - Mother Name:
    - Marks Table:
        - Student (FK)
        - Subject:
        - Marks:
    - Student Fee:
        - Student (FK)
        - Fee
        - Submitted_on

- Programs App
    - Program Table:
        - Program type
        - Program Name
        - Program Time
    - Lecturer's Table:
        - Name
        - Program (FK)