'''
Table structure for table Student
'''
DROP TABLE IF EXISTS Student;
CREATE TABLE Student
(   
    StudentID varchar(255) NOT NULL,
    StudentName varchar(255) NOT NULL,
    Password_ varchar(255) NOT NULL,
    Email varchar(255) NOT NULL,
    TotalCreditHours int(255) NOT NULL,
    DepartmentName varchar(255) NOT NULL,
    primary key(StudentID)
);

INSERT INTO Student ('StudentID' ,'StudentName', 'Password_','Email', 'TotalCreditHours',  'DepartmentName') VALUES
    ('23100100', 'Sarah Khan', 'helloWorld1', '23100100@lums.edu.pk', 62, 'Computer Science'),
    ('23100101', 'Ayesha Ahmad', 'thisismypassword', '23100101@lums.edu.pk', 89, 'Mathematics'),
    ('23100080', 'Abdullah Masood', 'ok2103asy', '23100080@lums.edu.pk', 115, 'Economics'),
    ('23100001', 'Mahnoor Malik', 'php01php', '23100001@lums.edu.pk', 32, 'History'),
    ('23100276', 'Eman Batool', 'slackhi90', '23100276@lums.edu.pk', 18, 'Physics');



'''
Table structure for table Course
'''
DROP TABLE IF EXISTS Course;
CREATE TABLE Course
(   
    CourseID varchar(255) NOT NULL,
    Title varchar(255) NOT NULL,
    DepartmentName varchar(255) NOT NULL,
    Credits int(255) NOT NULL,
    ModesOfInstruction varchar(255) NOT NULL,
    primary key(CourseID)
);

INSERT INTO Course ('CourseID', 'Title', 'DepartmentName', 'Credits', 'ModesOfInstruction') VALUES
    ('CS100', 'Intro to Computer Science', 'Computer Science', 3, 'Online'),
    ('CAL101', 'Calculus 1', 'Mathematics', 3, 'On-campus'),
    ('PHY101', 'Mechanics', 'Physics', 4, 'Online'),
    ('HIST124', 'Intro to Modern History', 'History', 3, 'On-campus'),
    ('ECO111','MicroEconomics','Economics', 3, 'Online');



'''
Table structure for table Section
'''
DROP TABLE IF EXISTS Section;
CREATE TABLE Section
(
    SectionID varchar (255) NOT NULL,
    CourseID varchar(255) NOT NULL,
    InstructorID varchar(255) NOT NULL,
    Semester varchar(255) NOT NULL,
    Year_ int(4) NOT NULL,
    TimeSlotID varchar(255) NOT NULL,
    primary key(SectionID, Semester, Year_),
    foreign key (CourseID) references Course,
    foreign key (InstructorID) references Instructor,
    foreign key (TimeSlotID) references TimeSlot
);

INSERT INTO Section ('SectionID', 'CourseID', 'InstructorID', 'Semester', 'Year_', 'TimeSlotID') VALUES
    ('S1','CS100', '001', 'Fall', 2019, '1'),
    ('S2','CAL101', '002', 'Spring', 2019, '2'),
    ('S1', 'PHY101', '003', 'Fall', 2020, '3'),
    ('S3', 'ECO111', '005', 'Fall', 2020, '4'),
    ('S1', 'HIST124', '004', 'Spring', 2020, '5');



'''
Table structure for table TimeSlot
'''
DROP TABLE IF EXISTS TimeSlot;
CREATE TABLE TimeSlot 
(
    TimeSlotID varchar(255) NOT NULL,
    Day_ varchar(255) NOT NULL,
    Start_Time varchar(255) NOT NULL,
    End_Time varchar(255) NOT NULL,
    primary key (TimeSlotID, End_Time, Day_, Start_Time)
);
INSERT INTO TimeSlot(TimeSlotID, Day_, Start_Time, End_Time)VALUES
    ('01', 'Monday', '8:00', '8:50'),
    ('02', 'Tuesday', '9:00', '9:50'),
    ('03', 'Wednesday', '11:00', '11:50'),
    ('04', 'Thursday', '5:00', '5:50'),
    ('05', 'Friday', '6:00', '6:50');



'''
Table structure for table PreReq
'''
DROP TABLE IF EXISTS PreReq;
CREATE TABLE PreReq 
(
    PreReqID varchar(255) NOT NULL,
    CourseID varchar(255) NOT NULL,
    primary key (PreReqID),
    foreign key (CourseID) references Course
);
INSERT INTO PreReq(PreReqID, CourseID)VALUES
    ('CS100', 'CS200'),
    ('PRE-CAL', 'CAL101'),
    ('PHY101', 'PHY104'),
    ('HIS101', 'HIST124'),
    ('ECO100', 'ECO111');



'''
Table structure for table Takes
'''
DROP TABLE IF EXISTS Takes;
CREATE TABLE Takes
(
    TakesID varchar (255) NOT NULL,
    CourseID varchar(255) NOT NULL,
    SectionID varchar (255) NOT NULL,
    Semester varchar(255) NOT NULL,
    Year_ int(4) NOT NULL,
    Grade varchar(255) NOT NULL, 
    primary key (TakesID,Grade)
    foreign key (CourseID) references Course,
    foreign key (SectionID, Semester, Year_) references Section 
);

INSERT INTO Takes ('TakesID', 'CourseID', 'SectionID', 'Semester', 'Year_', 'Grade') VALUES
    ('23100100','CS100', 'S1', 'Fall', 2019, 'A'),
    ('23100101','CAL101', 'S2', 'Spring', 2019, 'B+'),
    ('23100080', 'PHY101', 'S1', 'Fall', 2020, 'A-'),
    ('23100001', 'ECO111', 'S3', 'Fall', 2020, 'C'),
    ('23100276', 'HIST124', 'S1', 'Spring', 2020, 'F');



'''
Table structure for table Instructor
'''
DROP TABLE IF EXISTS Instructor;
CREATE TABLE Instructor
(
    InstructorID varchar(255) PRIMARY KEY,
    Name varchar(255) NOT NULL,
    DepartmentName varchar(255)
);

INSERT INTO Instructor
VALUES ("001", "Naveed Arshad", "Computer Science");
INSERT INTO Instructor
VALUES ("002", "Basit Shafeeq", "Computer Science");
INSERT INTO Instructor
VALUES ("003", "Suleman Shahid", "Computer Science");
INSERT INTO Instructor
VALUES ("004", "Adam Zaman", "Physics");
INSERT INTO Instructor
VALUES ("005", "Baqar Syed", "Religious Studies");


'''
Table structure for table Teaches
'''
DROP TABLE IF EXISTS Teaches;
CREATE TABLE Teaches
(
    InstructorID varchar(255),
    CourseID varchar(255),
    SectionID varchar(255),
    Semester varchar(255),
    Year_ int(4) NOT NULL,
    PRIMARY KEY(InstructorID, CourseID, SectionID, Semester, Year_)
);
INSERT INTO Teaches
VALUES ("001", "CS200", "S1", "Fall", 2021);
INSERT INTO Teaches
VALUES ("002", "CS301", "S1", "Fall", 2021);
INSERT INTO Teaches
VALUES ("003", "CS466", "S1", "Fall", 2021);
INSERT INTO Teaches
VALUES ("001", "PHY101", "S2", "Fall", 2019);
INSERT INTO Teaches
VALUES ("005", "SS101", "S1", "Spring", 2020);


'''
Table structure for table Admin
'''
DROP TABLE IF EXISTS Admin;
CREATE TABLE Admin
(
    AdminID varchar(255) PRIMARY KEY,
    AdminName varchar(255) NOT NULL,
    AdminPassword varchar(255) NOT NULL,
    AdminEmail varchar(255) NOT NULL
);
INSERT INTO Admin
VALUES ("101", "Mohid Tanvir", "PassWord123.", "mohid.tanvir@lums.edu.pk");
INSERT INTO Admin
VALUES ("102", "Laiba Usman", "PassWord321.", "laiba.usman@lums.edu.pk");
INSERT INTO Admin
VALUES ("103", "Tayyab Nasir", "PassWord.123", "tayyab.nasir@lums.edu.pk");
INSERT INTO Admin
VALUES ("104", "Zoha Aqil", "PassWord.321", "zoha.aqil@lums.edu.pk");
INSERT INTO Admin
VALUES ("105", "Soha Amir", "PassWord12335.", "soha.amir@lums.edu.pk");


'''
Table structure for table SwapIt
'''
DROP TABLE IF EXISTS SwapIt;
CREATE TABLE SwapIt
(
    RequestID varchar(255) NOT NULL,
    HaveCourseID varchar(255) NOT NULL,
    WantCourseID varchar(255) NOT NULL,
    AcceptID varchar(255) NOT NULL,
    primary key (RequestID)
);
INSERT INTO SwapIt(RequestID,HaveCourseID,WantCourseID,AcceptID) VALUES
    ('23100253', 'CS100', 'CS200', '6:50'),
    ('23100115', 'ECO100', 'ECO111', '6:50'),
    ('23100277', 'HIST100', 'CS200', '6:50'),
    ('23100126', 'CAL101', 'MGMT142', '6:50'),
    ('23100289', 'ENG111', 'CAL101', '6:50');