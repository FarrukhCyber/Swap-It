from flask import Blueprint, render_template, request, flash, jsonify
from flask.helpers import url_for
from werkzeug.utils import redirect
from project.auth import session
from .db_config import create_db
from project import views


mysql = create_db()

admin = Blueprint('admin', __name__)


@admin.route('/admin', methods=['GET', 'POST'])
def admin_page():
    print("came here")
    return render_template("admin_home.html", session = session)

@admin.route('/admin/add', methods=['GET', 'POST'])
def add():
    print("in add")
    if request.method == 'POST':
        print("jere")
        details = request.form
        cid = details.get('cid') # course_id
        cname = details.get('cname') # course name
        dname = details.get('dname') # dept name
        cred = details.get('cred') # credits
        mode = details.get('options') # credits

        print(cname, dname)
        cur = mysql.connection.cursor()
        
        # ***    PUT A CHECK IF COURSE ALREADY EXISTS !!!   ***

        cur.execute("Insert into course(CourseID,Title,DepartmentName,Credits,ModesOfInstruction) values(%s,%s,%s,%s,%s)", [cid, cname, dname, cred, mode])
        cur.connection.commit()
        cur.close()
        print("leaving")
        return redirect(url_for('admin.admin_page'))

    return render_template("admin_add.html", session = session)

@admin.route('/admin/drop', methods=['GET', 'POST'])
def drop():
    print("in drop")

    cur = mysql.connect.cursor()
    cur.execute("Select* from course")
    result = cur.fetchall()
    cur.close()

    if result:
        session["drop"] = result
    else:
        session["drop"] = -1

    return redirect(url_for("admin.drop_del"))

@admin.route('/admin/drop_del', methods=['GET', 'POST'])
def drop_del():
    # SEND THIS RESULT TO HTML
    result = session["drop"]
    if request.method == 'POST':
        print("jere")
        details = request.form
        cid = details.get('options') # course_id
        print(cid)
        cur = mysql.connect.cursor()
        
        # ***    PUT A CHECK IF COURSE DOESNT EXISTS !!!   ***

        # cur.execute("delete from course where CourseID = %s", [cid])
        # cur.connection.commit()
        # cur.close()
        # cur = mysql.connect.cursor()
        cur.execute("select StudentID from takes where CourseID = %s", [cid])
        stid = cur.fetchall()

        cur.execute("select* from takes where CourseID = %s", [cid])
        check = cur.fetchall()
        if check: # if course is taken by anyone
            cur.execute("delete from takes where CourseID = %s", [cid])
            cur.connection.commit()
        cur.execute("select* from teaches where CourseID = %s", [cid])
        check = cur.fetchall()
        if check: # if course was taught by anyone
            cur.execute("delete from teaches where CourseID = %s", [cid])
            cur.connection.commit()

        cur.execute("select* from section where CourseID = %s", [cid])
        check = cur.fetchall()
        if check: # if course was taught by anyone
            cur.execute("delete from section where CourseID = %s", [cid])
            cur.connection.commit()
        cur.execute("delete from course where CourseID = %s", [cid])
        cur.connection.commit()
        cur.close()
        print("leaving")

        # UNCOMMENT WHEN TABLE IS MADE !!!
        # cur = mysql.connect.cursor()
        # mess = "The course with Course ID " + cid + " has been dropped and removed from your enrollment."
        # mess = mess + " Please take notice and update your enrollment accordingly. Sorry for any inconvinience."
        # for s in stid:
        #     cur.execute("insert into messages(id, mess) values(%s, %s)", [s, mess])
        #     cur.connection.commit()
        # cur.close()
        # TILL HERE 
        return redirect(url_for('admin.drop'))

    flag = True
    if result == -1:
        flag = False

    return render_template("admin_drop.html", data= result, flag=flag)

@admin.route('/admin/edit', methods=['GET', 'POST'])
def edit(): # fetches all the rows from table and sends it to edit_it
    print("in edit")
    cur = mysql.connect.cursor()
    cur.execute("Select* from course")
    result = cur.fetchall()
    cur.close()

    if result:
        session["edit"] = result
    else:
        session["edit"] = -1

    return redirect(url_for("admin.edit_it"))

@admin.route('/admin/edit_change', methods=['GET', 'POST'])
def edit_change():
    print("in change")
    cid = session["edit"]
    if request.method == 'POST':
        print("jere")
        details = request.form
        cname = details.get('cname') # course name
        dname = details.get('dname') # dept name
        cred = details.get('cred') # credits
        mode = details.get('options') # credits

        cur = mysql.connection.cursor()

        updated = []

        if cname:
            cur.execute("update course set Title = %s where CourseID = %s", [cname, cid])
            cur.connection.commit()  
            updated.append("Title")
        print(1)  
        if dname:
            cur.execute("update course set DepartmentName = %s where CourseID = %s", [dname, cid])
            cur.connection.commit() 
            updated.append("Department Name")   
        print(2)  
        if cred:
            cur.execute("update course set Credits = %s where CourseID = %s", [cred ,cid])
            cur.connection.commit() 
            updated.append("Credits")   
        print(3)  
        if mode:
            cur.execute("update course set ModesOfInstruction = %s where CourseID = %s", [mode, cid])
            cur.connection.commit()  
            updated.append("Mode of Instruction")  
        cur.close()
        print("leaving")

        # UNCOMMENT WHEN TABLE IS MADE !!!
        # cur = mysql.connect.cursor()
        # mess = "The Following attributes: " + updated + ", for Course with Course ID " + cid + " has been updated."
        # mess = mess + " Please take notice and update your enrollment accordingly. Sorry for any inconvinience."
        # for s in stid:
        #     cur.execute("insert into messages(id, mess) values(%s, %s)", [s, mess])
        #     cur.connection.commit()
        # cur.close()
        # TILL HERE 

        return redirect(url_for('admin.admin_page'))

    return render_template("admin_edit_change.html", session = session)


@admin.route('/admin/edit_it', methods=['GET', 'POST'])
def edit_it():
    result = session["edit"]
    if request.method == 'POST':
        print("jere")
        details = request.form
        cid = details.get('options') # course_id
        print(cid)
        session["edit"] = cid
        return redirect(url_for('admin.edit_change'))

    flag = True
    if result == -1:
        flag = False

    return render_template("admin_edit.html", data= result, flag=flag)

@admin.route('/admin/ins_add', methods=['GET', 'POST'])
def ins_add():
    print("ins add here")
    if request.method == 'POST':
        print("jere")
        details = request.form
        iid = details.get('iid') # course_id
        iname = details.get('iname') # course name
        dname = details.get('dname') # dept name

        cur = mysql.connect.cursor()
        print(iid, iname, dname)
        # ***    PUT A CHECK IF COURSE ALREADY EXISTS !!!   ***

        cur.execute("Insert into instructor(InstructorID,Name_,DepartmentName) values(%s,%s,%s)", [iid, iname, dname])
        cur.connection.commit()
        cur.close()
        print("leaving")
        return redirect(url_for('admin.admin_page'))

    return render_template("admin_ins_add.html", session = session)


@admin.route('/admin/ins_drop', methods=['GET', 'POST'])
def ins_drop():
    print("drop here")
    cur = mysql.connect.cursor()
    cur.execute("Select* from instructor")
    result = cur.fetchall()
    cur.close()

    if result:
        session["ins_drop"] = result
    else:
        session["ins_drop"] = -1

    return redirect(url_for("admin.ins_drop_del"))

@admin.route('/admin/ins_drop_del', methods=['GET', 'POST'])
def ins_drop_del():
    # SEND THIS RESULT TO HTML
    result = session["ins_drop"]
    if request.method == 'POST':
        print("jere")
        details = request.form
        iid = details.get('options') # course_id
        print(iid)
        cur = mysql.connect.cursor()
        
        # ***    PUT A CHECK IF COURSE DOESNT EXISTS !!!   ***

        # cur.close()
        # cur = mysql.connect.cursor()
        cur.execute("select* from teaches where InstructorID = %s", [iid])
        check = cur.fetchall()
        if check:
            cur.execute("delete from teaches where InstructorID = %s", [iid])
            cur.connection.commit()

        cur.execute("delete from instructor where InstructorID = %s", [iid])
        cur.connection.commit()
        cur.close()
        print("leaving")
        return redirect(url_for('admin.ins_drop'))

    flag = True
    if result == -1:
        flag = False

    return render_template("admin_ins_drop.html", data= result, flag=flag)


