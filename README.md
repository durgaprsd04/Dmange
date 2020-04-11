

# dManage
An open source software for managing academic activities.


## Update 2020410
> Due to amount of complexity involved I am trimming down the project to a very small hobby project. All the things mentioned below would still stand, but i have decided a more structural approach would work in order to achieve this. 

> Certain points to note include.
* Code repo would be cleared of all the existing code.
* Basic structure would be put up below.
* Development process would begin from these steps.
* Daily/Routine changes would include updating this file.

## Structure 20200410
| Student       | Faculty          | Course      | Department |Courses4Year |Reg4year     |
| ------------- |:----------------:| -----------:|-----------:|------------:|------------:|
| roll number   | fac id           | course id   | code       | course_id   | c4_id       |
| name          | name             | Department  | Name       | facutlty_id | roll_number |
| Department    | Department       | Course name |            | Year        |             |  
|               |                  |             |            | c4_id       |             |
    
## Action Items
1. Faculties create courses.
2. Students register for them.


### Initial ideas setting up
As of now we are planning to do a repository based on the JSP servlet. There are several issues associated with the same, but the idea behind remains a UI friendly interface preferably in JSP with functionalities embedded within the same, quite similar to  our DSS. There should be separate database mostly postgres for the work done.

Separate logins for students, faculties, staff and ultimately admin should be there. The students should be able to login check their marks, faculties should be able to enter the mark of students as \textbf{.csv files or \textbf{.xls files. The staff should be able to access the data of several students batch wise or individually and should be limited to certain aspects defined later. There is process of registration of students to preceding semesters and thus there is the process of mark entering, which is again defined by the faculty, usually 20, 20, 10 but the 100 marks can be defined by the faculty as it seems. I am just listing out the major requirements as they come to my mind. The basic structure will be evolving soon enough. First few pull requests might be having a lot of clutter and repetition, which will be clarified later on. 

As of now the for students the process of detail entering the very first step in registering. After they have registered as users in the system, one or two days before the process of registration they will get a mail regarding the starting of process of registration. After that they are supposed to login to the system and select the courses they want. In the case of electives, every staff from all departments will be able to login and add a list of electives to the department page. On adding the electives the details of students who can choose the elective should be made available, details such as the semester they should belong, minimum cgpa etc. If the elective is first come first serve then that can be selected along or without the CGPA restriction. All these are decided before registration and on completion of this process the course will be visible to all eligble students who can apply for the same. Once they get the list of courses they might be able to select these only if they are eligible. If the course is overrun they will get a notification and won't be able to register. The course faculty can be specified at the time of creation of course, if more students request for the elective the faculty can login and add them. The eligiblity criteria for the course are mentioned in section \ref{sec:eligibility.


El
Contribute the initial ideas to the project.
Please see the project wiki and issues.
~~
### What all things can staff do?

This lists the duties that a staff can perform. Their power is somewhat limited and is mostly restricted to 
 
* Adding courses to the department page. 
* They cannot remove courses as at the time of adding course a faculty must be selected and only this faculty is able to remove the course. They can only deactivate the course. Deactivate means it will not be visible to all the logins it was used to be visible.
* On adding a faculty the course, faculty gets the notification he has been added as the course faculty and on login he gets the access to the course. He can at his will remove or add students who fail to satisfy the eligiblity criteria. 
* There will be a faculty associated with every student and can remove him from any course as he pleases. This is usually the role of faculty advisor. Usually every faculty will have chance to select the students  to whom he/she will be the faculty advisor. 
* The no due certificate from all the required departments is provided in such a way that a \textbf{csv with roll number with dues is uploaded on the day of registration and on remittance the staff in the respective department will remove their name from the list on producing necessary documents.
* Registration process for users is a three step, one step the user can fill in data and in the next steps verification takes place. I am a little doubtful here. We will clarify it later on.
* On remittance of late fee should be able to unlock the student account and let him do the process. 
 
### What all things students can do?
Usually the thigns students can do include 
 
* They can login and select the courses they can choose.
* They can view their results anytime.
* They get notifications when there is a pending activity which includes.
 
* Teacher Evaluvation.
* Fee payment details filling.
* Course registration.
 
* If they are delayed then the course registration automatically stops and they need remit some fee amount. 
* The students will be notified via mail about this. After this their account will be locked.
* After registration with/without delay they will get a softcopy to their mail with all the details mentioend. They are supposed to take two copies of the same and give one to the faculty and keep one to themselves. This is a one time generated softcopy and will be given in print to the student at the time or registration along with signature of the staff. The FA has to keep it and the same with the student.
 
### What all things can faculties do?
This section list all the possible functions of faculties.
 
* They all have login and can start a course or staffs can start a course and add faculty to the course.
* On login they will be requested to take the course and if they accept they get to manage the course. 
* Once they accept staff will loose power of the course and faculty will get all the power over the course.
* Faculty can also create a course and will have the same power. 
* HOD of the department will also have a login, so that all course details can be viewed. 
* Staffs can also watch all courses and can see the list of marks and all the associated documents as soon as the faculty upload them.
* Other faculties cannot see what one faculty does but if two faculties are added for asingle course he can see what the other faculty does.
* If a faculty change happens, one faculty can assign another and he will have monitoring status over the course. That is he can watch the course but cannot enter marks or delete/add students. He can also add a co-faculty who will have the same power as the main faculty but this time both can add marks. Individual editing of marks are possible only for one faculty at a time.
* At the time of registration he can add students to the course by searching mentioned in \ref{sec:eligibility. Once the day for registration is over, the student has to pay an amount and only after that the faculty can add the student. Faculty should get notification when a student is added for the course by the other faculty. At the time of registration anyway these mailing wil be off. So that only a few mails are send. If he need a round the clock history he can turn on notifications so that he might get the a notification every time the registration process is complete. 
 
### Registration Process
 This is somewhat the main process happening . 
  
 * Usually the date of registration is put in by admin. 
 * At the date staff with privilege level above a particular one will be able to login.
 * On login they will be given a login with option to start registration. All the student who are supposed to register should register on that day.
 * They will be given a data box where the roll number will be entered. 
 * A page will appear with information regarding the student such as 
  
 * Name rollnumber department  
*  No due from place 1.
 * No due from place 2.
 * No due from place 3.
 * Fee remittance with details.
 * Fee2 remittance with details.
 * Semester registered. 
 * from date-to date.
* A unique hash. 
  
 After this a small strip of paper with from date-todate a hash (8-10 alphanumeric) semester UG branch will be generated. This is printed on to a sticker and pasted behind the id card. At the time of registration a paper with fee details and other essentialities are printed on to a paper and this is has got the same hash. A softcopy will be generated with the hash as file name  and will be kept in the folder mentioned earlier as well as one will be printed along with the sticker. The bottom part is the one tore off. 
  
### Eligibility for Electives\label{sec:eligibility
This is usually a strict requirement for elective but most of the time some kind of a human judgement is needed for the same. Any student who is eligible will be able to select the elective, if it had not run out of its maximum participant limit. This is usually 80 or set at the time of creation of elective. There are certain cases such 
 
* The maximum limit is over.
* The student has got no eligibility there, these conditions are listed below.
 
* Minimum CGPA.
* Minimum grade in any subject.
* A previous elective or course.
 
Faculties should be able to login and apply relaxations to any of the above criteria. On request of the student the faculty can login and add  a student in the system by selecting his department or simply typing the roll number or just a part of name and then selecting as student for a particular elective. Only the faculty can login and do this and staffs should not be permitted to this. 
 
### On Course Completion
On course completion the faculty/staff will be able to check out the student from the system. For this student has to collect several no dues from all the labs and departments and then remit the dues get no dues from there and go to a staff who is able to grant all the no dues related with the student.

### Types of Staff
As mentioned above  there are two types of staff logins. The first type are the people who are in academic section. They can add courses and associate faculties with courses. The second type are those who can register/ deregister/check out students. They have the permission to register students for a particular course. They can complete registration for students based on no dues and all. There is a little doubt here. You can edit it accordingly so that the basic idea is conveyed. Usually there is a set of course related works that should be done by academic staff, which should not be done by purely academic staff. So a distinction of employees are needed. But the idea is more or less to have a two distinct set of staff, one with a previlege level for accessing and creating courses and one who can approve the students and register accordingly. We will have a problem over here.



## Tools used
Well as of now we have switched to java and tomcat as the servlet. The basic things to do are first setting up the servlet. Just download binary, put it somewhere and add to path. Then compile the __.java__ file you want to and copy the __.class__ file to the examples folder under webapp in the tomcat directory. After this make the appropriate changes in the web.xml file. These could be found in the tutorials point site, but I am just mentioning the facts here so that every body is on the same page. For database access we will be using jdbc and __araj, melvin__ can we use twitter bootstrap stylesheet. Please see how we could use it, and somebody study how jdbc can be used to write/read from the database(only jdbc) not through servlet( You can do that  through servlet if you are interested).

###  To do as of 13/6/2015

Well as on now, database access has worked, we will be doing two important
things. First as we have database access, we will be having a table for
students with all their details, with roll number as primary key. This is just
a suggestion, usually everything is done with roll number. Now we need to check
the compatibility/usability of __twitter bootstrap__. This style if possible
could be used.

###  An initial test system.(Phase 1)

After proper database access has been developed we will go for a development
model we will develop a simple UI with a login and a password, for every
student. On logged in  he should be able to see his details, such as name, roll
number, branch, semester etc. Note that all these are stored in a database with
roll number as primary key. With this in mind, generate a random data set and
input it to the  database. This __.csv__ / __.xls__ file could be uploaded via
web or root into the database. After this, login should be made for all
students to access and modify their data. All the above data are fixed. There
should be a profile information with address/blood group/ other trivial
informations. 

So we should have the following set of functions.
* A bulk uploader via command line/web ui 
* Students should get login after they are added via bulk/batch or single user
  add facility.
* After login students should be able to edit some data.
* An administrator page where students can be deleted or added.
* Administrator can also remove/add/edit student information and that too all
  of them.
* As of now only these, we will modify these later.

So it should contain a number of small programs rather than a huge one, for
readability and ease of editing. There is also a great deal of ease if the
functionality is split into smaller classes. Please do accordingly, with
putting all the functions with database access in one folder, WEBUI in one
folder and so on.

###  Phase 2 things to be done

After the above implementations are done we will adding be features to these. The next set of jobs include creation of a user group known as faculties. They will be also uploade via a __.csv___ or __.xls__ file and will have associated metadata. All of their metadata except designation and  department are editable by the group faculties itself. Every faculty will be associated with department and each department will have an hod. This may not be a separate user. Usually hod has the permission to choose next HOD. On choosing the next HOD, from next login onwards he/she will loose the privileges of HOD. The privileges of HOD include
* Approving courses started by the faculties.
* Assign/Add faculties to a course.
* Approve final/interim marklists, which on approval will be finalized.

The above tasks are too complex for a direct implementation, so a simple step by step procedure is added below.
####  Step 1
To make the process simple we will go through this step by step, first a user group named faculty is created, with their email id as login and password as 'password'. Then they are granted the power of course creation, which means in their UI they will have an option to create a course. The course will be containing department, course-code, course-name, a brief summary, portions and textbooks. The next step include adding students which is done using a __.csv__ file or __.xls__ file. After creation of these all students who are registered on login should be able to see this particular course on courses registered. Faculty should have the option for adding new members individually to the course. The primary key to be used is roll number. Thus after all faculties have added all their courses, students on login will be able to see a page where the courses they have registered will be shown. 

####  Step 2
The next step would be approval of courses. This is a tricky part. Note that any faculty can start a course and register students but students should only be registered after it is approved from another login. Usually this login is known as the HOD login. They should have quite a lot of permissions of which only a few are discussed here. They will be added later on. As of now the three permissions given above would suffice. Note that the implementation done here is for a single department. Keep in mind that the faculty will have a department as his metadata. And an HOD with the same department as metadata is the only one who would be able to approve the courses. So the work flow would be something like this. First the faculty creates a course and a notification goes to HOD. The HOD then approves the course and after that only does it goes to students.

####  Electives
This is a little too much to add now, but the idea is basically the same. Once you have set up the above seciton, there would be an option which chooses, whether it is an elective or it is a core subject. If elective then it can be global or local. Then there is a case for cut off and prerequsities. All these are optional and can be over riden by the course faculty. The electives section has got a detailed paragraph on that. Please have look. With this we wrap the Phase 2. 
~~
