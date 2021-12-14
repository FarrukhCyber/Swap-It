import names
import random # new libraries ^
from flask import Blueprint, render_template, request, flash, jsonify
from flask.helpers import url_for
from werkzeug import datastructures
from werkzeug.datastructures import V
from werkzeug.utils import redirect
from project.auth import session
from .db_config import create_db
from project import views

# done with -> student | instructor | timeslot | section | course | teaches | admin | takes
mysql = create_db()
cur = mysql.connect.cursor()
value = [0]*6
credit = [80,85,90,95,100]
dept = ["Computer Science", "Physics", "Biology", "Electrical Engineering", "Economics", "Law", "Accounting", "Management Sciences"]
roll_number = 23100100
# adds 5k student entries 
for i in range(5000): # adds 5k student entries
    value[1] = roll_number
    value[2] = names.get_full_name()
    value[3] = roll_number
    value[4] = str(roll_number) + "@lums.edu.pk"
    value[5] = random.choice(credit)
    value[6] = random.choice(dept)
    cur.execute("insert into student values(%s, %s, %s, %s, %s, %s)", value)
    cur.connection.commit()
    roll_number+=1

insid = 6
value = [0]*3
for i in range(50): # adds 50 instructors 
    value[0] = insid
    value[1] = names.get_full_name()
    value[2] = random.choice(dept)
    cur.execute("insert into instructor values(%s, %s, %s,)", value)
    cur.connection.commit()
    insid+=1

day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
course = [ ("CS300", "Advanced Programming"), ("CS100", "Introduction to Computer Science")]
section = ["S1","S2","S3"]
mode = ["On-Campus", "Online"]
t_val = [0]*4
c_val = [0]*5
s_val = [0]*3
te_val = [0]*3
course_id = 400
t_inst = 7
for i in range(100): # adds 100 courses and adjusts section + teaches + timeslot 
    t_sec = random.choice(section)
    time_slot = t_sec + str(course_id)
    t_day = random.choice(day)
    t_val = [time_slot, t_day, 0,0]
    cur.execute("Insert into timeslot(TimeSlotID,Day_,Start_Time, End_Time) values(%s,%s,%s, %s)", t_val)
    cur.connection.commit() # InstructorID | CourseID | SectionID |
    t_dept = random.choice(dept)
    title = t_dept + " " + str(course_id)  
    t_cred = random.choice(credit)
    t_mode = random.choice(mode)
    c_val = [course_id, title, t_dept, t_cred, t_mode]
    cur.execute("Insert into course(CourseID,Title,DepartmentName,Credits,ModesOfInstruction) values(%s,%s,%s,%s,%s)", c_val)
    cur.connection.commit() #SectionID | CourseID | InstructorID | TimeSlotID
    s_val = [t_sec, course_id, time_slot]
    cur.execute("Insert into section(SectionID,CourseID, TimeSlotID) values(%s,%s, %s)", s_val)
    cur.connection.commit() # InstructorID | CourseID | SectionID |
    te_val = [t_inst, course_id, t_sec]
    cur.execute("Insert into teaches(InstructorID,CourseID,SectionID) values(%s,%s,%s)", te_val)
    cur.connection.commit()
    course_id+=1
    t_inst+=1


admin_id = 10
for i in range(10): # adds 10 admin entries
    i_name = names.get_full_name()
    i_email = str(admin_id) + "@lums.edu.pk"
    i_val = [admin_id, i_name, admin_id, ]
    cur.execute("Insert into admin values(%s,%s,%s.%s)", )
    cur.connection.commit()
    admin_id+=1

ts_id = 23100115 
ts_cid = 100
for i in range(2000): # takes 
    ts_sec = random.choice(section)
    ts_dept = random.choice(dept)
    ts_course = ts_dept + str(ts_cid)
    ts_val = [ts_id,ts_course,ts_sec]
    cur.execute("Insert into takes values(%s,%s,%s)", ts_val)
    cur.connection.commit()
    ts_id+=1
    ts_cid+=1
