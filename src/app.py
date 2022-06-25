from flask import *
import pymysql
from werkzeug.utils import secure_filename
import os
from src.rsa import *
import pyqrcode
from werkzeug.utils import secure_filename

from src.test_face import test_face

con = pymysql.connect(host="localhost", user='root', passwd='root', port=3306, db='unique id')
cmd = con.cursor()
app = Flask(__name__)
app.secret_key = 'abc'


@app.route('/')
def login():
    session.clear()
    return render_template("index.html")

@app.route('/index_signup')
def index_signup():
    return render_template("index_signup.html")

@app.route('/test')
def test():
    return render_template("test.html")

@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    if 'adid' in session:
         cmd.execute("select * from course")
         s = cmd.fetchall()
         return render_template("uni_add_manage_courses.html", val=s)
    else:
        return '''<script>alert("please login");window.location="/"</script>'''


@app.route('/view_course', methods=['GET', 'POST'])
def view_course():
    return render_template("uni_add_link_for_courses.html")


@app.route('/announce_exam', methods=['GET','POST'])
def announce_exam():
    return render_template("uni_announce_exam.html")


@app.route('/view_exam')
def view_exam():
    return render_template("uni_announce_exam_table.html")


@app.route('/approve_college')
def approve_college():
    return render_template("uni_approve_college.html")


@app.route('/certificate_generation1')
def certificate_generation1():
    if 'adid' in session:
        cmd.execute("Select * from college")
        d = cmd.fetchall()
        return render_template("uni_certificate generation1.html", nal=d)
    else:
        return '''<script>alert("please login");window.location="/"</script>'''




@app.route('/certificate_generation2')
def certificate_generation2():
    if 'adid' in session:
        sid=request.args.get('id')
        session['stid']=sid
        cmd.execute("SELECT image FROM `student` WHERE `login_id`="+str(sid))
        s=cmd.fetchone()

        mk = test_face()
        s = mk.test_face("static/students/" + str(s[0]))
        session['mnk'] = s
        ss=s.split("#")

        return render_template("uni_certificate generation2.html",val=ss)
    else:
        return '''<script>alert("please login");window.location="/"</script>'''



@app.route('/qr',methods=['POST','GET'])
def qr():
    if 'adid' in session:
         marks=session['mnk']
         privatekey, publickey = generate_keys()
         print("pub------"+str(publickey))
         print("prvt---------" + str(privatekey))
         encrypted_msg = encrypt_message(marks, privatekey)
         print(str(encrypted_msg))
         rsa_pvtkey=privatekey.exportKey("PEM")
         print('rsakeyy---------',rsa_pvtkey)
         rsa_pubkey=publickey.exportKey("PEM")
         print('rsapubkeyy---------', rsa_pubkey)
         # rsa_pub = PKCS1_OAEP.new(rsa_pubkey)
         cmd.execute("insert into cipher_text values(null,'"+str(session['stid'])+"','"+str(encrypted_msg.decode('utf-8'))+"','"+rsa_pvtkey.decode('utf-8')+"','"+rsa_pubkey.decode('utf-8')+"')")
         id=con.insert_id()
         session['cid']=id
         con.commit()
         big_code = pyqrcode.create(encrypted_msg, error='L', version=27, mode='binary')
         qrs = "static\\QR\\"+str(id)+".png"
         img_name=str(id)+".png"
         print("imggg--------------" + str(img_name))

         session['qr']=img_name
         big_code.png(qrs, scale=3, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
         print('ok')
         # cmd.execute("select student_reg.*,course.Course,student_mark.Description from student_reg  inner join course on  student_reg.Course=course.Course_id inner join login on student_reg.Student_id=login.Uid join student_mark on student_mark.student_id=student_reg.Student_id where student_reg.student_id='"+str(session['id'])+"'")
         cmd.execute(" SELECT `student`.`register_number`,`student`.`name`,`student`.`gender`,`college`.`college_name`,`student`.`image`,`course`.`course` FROM `course` JOIN `student` ON `student`.`course_id`=`course`.`id` INNER JOIN `college` ON `college`.`register_number`=`student`.`college` WHERE `student`.`login_id`="+str( session['stid'])+"")
         data=cmd.fetchone()
         print("imggg"+str(img_name))
         return render_template('ad_generate4.html',im=img_name,data=data)
    else: return '''<script>alert("please login");window.location="/"</script>'''

@app.route('/upcipher',methods=['POST','GET'])
def upcipher():
    if 'adid' in session:
        cmd.execute("SELECT `student`.`register_number`,`student`.`name`,`student`.`gender`,`course`.`course`,`cipher_text`.`id`,`student`.`image`,`course`.`id`,studsem.sem FROM student INNER JOIN course ON student.`course_id`=`course`.`id` INNER JOIN `cipher_text` ON `student`.`login_id`=`cipher_text`.`uid` JOIN `studsem` ON `studsem`.`lid`=`student`.`login_id` WHERE `student`.`login_id`= '" + str(session['stid']) + "'")
        s = cmd.fetchall()
        print(s, "certificate")
        cmd.execute("select * from subject where course_id='" + str(s[0][6]) + "' and sem='"+str(s[0][7])+"'")
        res = cmd.fetchall()
        return render_template('certificate_template.html',dt=s,val=res)
    else: return '''<script>alert("please login");window.location="/"</script>'''

@app.route('/downloadht',methods=['POST','GET'])
def downloadht():
    # if 'collegeid' in session:
        sid=request.args.get('id')
        cmd.execute("SELECT `student`.`register_number`,`student`.`name`,`student`.`gender`,`course`.`course`,`cipher_text`.`id`,`student`.`image`,`course`.`id`,studsem.sem FROM student INNER JOIN course ON student.`course_id`=`course`.`id` INNER JOIN `cipher_text` ON `student`.`login_id`=`cipher_text`.`uid` JOIN `studsem` ON `studsem`.`lid`=`student`.`login_id` WHERE `student`.`login_id`= '" + str(sid) + "'")
        s = cmd.fetchall()
        print(s, "certificate")
        cmd.execute("select * from subject where course_id='" + str(s[0][6]) + "' and sem='"+str(s[0][7])+"'")
        res = cmd.fetchall()
        return render_template('certificate_template.html',dt=s,val=res)
    # else: return '''<script>alert("please login");window.location="/"</script>'''



@app.route('/certificate_generation3')
def certificate_generation3():
    if 'adid' in session:
        return render_template("uni_certificate generation3.html")
    else:
        return '''<script>alert("please login");window.location="/"</script>'''

@app.route('/clg_change_password')
def clg_change_password():
    if 'collegeid' in session:
        return render_template("clg_CHANGE_PASSWORD.html")
    else:
        return '''<script>alert("please login");window.location="/"</script>'''

@app.route('/external_mark', methods=['GET','POST'])
def external_mark():
    return render_template("uni_external_mark.html")


@app.route('/external_mark_table',methods=['GET','POST'])
def external_mark_table():
    return render_template("uni_EXTERNAL_MARK_TABLE.html")


@app.route('/homepage')
def homepage():
    if 'adid' in session:
        return render_template("uni_homepage.html")
    else:
        return '''<script>alert("please login");window.location="/"</script>'''

@app.route('/collegehome')
def collegehome():
    if 'collegeid' in session:
        return render_template("clg_college.html")
    else:
        return '''<script>alert("please login");window.location="/"</script>'''

@app.route('/pkbhome')
def pkbhome():
    return render_template("pkb_PAREEKSHA_BHAVAN.html")


@app.route('/pkb_exam',methods=['GET', 'POST'])
def pkb_exam():
    return render_template("pkb_EXAM_MANAGEMENT.html")

@app.route('/pkb_exam_table')
def pkb_exam_table():
    cmd.execute("SELECT * FROM EXAM")
    s = cmd.fetchall()
    return render_template("pkb_exam_table.html",val=s)


@app.route('/pkb_hall')
def pkb_hall():

    return render_template("pkb_DOWNLOAD_HALL_TICKETS.html")


@app.route('/collegereg')
def collegereg():
    return render_template("log_college_registration.html")

@app.route('/edit_external_call')
def edit_external_call():
    id = request.args.get('id')
    session['id'] = id
    cmd.execute("select * from external where id='" +str(id)+ "'")
    s = cmd.fetchone()
    return render_template("uni_edit_external_mark.html",val=s)



@app.route('/edit_course')
def edit_course():
    id = request.args.get('id')
    session['id'] = id
    cmd.execute("select * from course where id='" + id + "'")
    s = cmd.fetchone()
    return render_template("uni_edit_link_for_courses.html", val=s)


@app.route('/log', methods=['GET', 'POST'])
def log():
    user = request.form['textfield']
    password = request.form['textfield2']
    cmd.execute("select * from login where username='" + user + "' and password='" + password + "'")
    s = cmd.fetchone()
    if s is None:
        return '''<script>alert("invalid");window.location="/"</script>'''
    elif s[3] == "admin":
        session['adid']=s[0]

        return '''<script>window.location="/homepage"</script>'''
    elif s[3] == "college":
        session["collegeid"]=s[0]
        return '''<script>window.location="/collegehome"</script>'''
    else:
        return '''<script>alert("invalid");window.location="/"</script>'''

    # elif s[3] == "pareekshabhavan":
    #     return '''<script>window.location="/pkbhome"</script>'''


@app.route('/collegeregistration', methods=['GET', 'POST'])
def collegeregistration():
    college_name = request.form['textfield']
    register_number = request.form['textfield2']
    place = request.form['textfield3']
    district = request.form['textfield4']
    post = request.form['textfield5']
    pincode = request.form['textfield6']
    email = request.form['textfield7']
    phone = request.form['textfield8']
    username = request.form['textfield9']
    password = request.form['password1']
    c_password = request.form['password2']
    if password == c_password:
        cmd.execute("insert into login values(null,'" + username + "','" + password + "','pending')")
        id = con.insert_id()
        cmd.execute("insert into college values('" + str(id) + "','" + college_name + "','" + register_number + "','" + place + "','" + district + "','" + post + "','" + pincode + "','" + email + "','" + phone + "')")
        con.commit()
    else:
        return '''<script>alert("password not same");window.location="/"</script>'''
    return '''<script>alert("Success");window.location="/"</script>'''


@app.route('/approve')
def approve():
    if 'adid' in session:
        cmd.execute("SELECT `college`.* FROM `college` INNER JOIN `login` ON `login`.`id`=`college`.`id` WHERE `login`.`usertype`='pending'")
        s = cmd.fetchall()
        return render_template("uni_approve_college.html", val=s)
    else:
        return '''<script>alert("plz login");window.location="/"</script>'''

@app.route('/approvecollege')
def approvecollege():
    id = request.args.get('id')
    cmd.execute("update login set usertype='college' where id='" + id + "'")
    con.commit()
    return render_template("uni_homepage.html")


@app.route('/rejectcollege')
def rejectcollege():
    id = request.args.get('id')
    cmd.execute("delete from login  where id='" + id + "'")
    cmd.execute("delete from college where id='" + id + "'")
    con.commit()
    return render_template("uni_homepage.html")


@app.route('/addcourse', methods=['GET', 'POST'])
def addcourse():
    course = request.form['textfield']
    duration = request.form['textfield2']
    cmd.execute("insert into course values(null,'" + course + "','" + duration + "')")
    con.commit()
    return '''<script>alert("successful");window.location="/add_course"</script>'''


@app.route('/edit_button', methods=['GET', 'POST'])
def edit_button():
    id = session['id']
    course = request.form['textfield']
    duration = request.form['textfield2']
    cmd.execute("update course set course='" + course + "',duration='" + duration + "' where id='" + str(id) + "'")
    con.commit()
    return '''<script>alert("updated");window.location="/add_course"</script>'''


@app.route('/delete')
def delete():
    id = request.args.get('id')
    cmd.execute("delete from course where id='" + id + "'")
    con.commit()
    return '''<script>alert("successful");windows:location="/add_course"</script>'''


@app.route('/exam_detail', methods=['GET', 'POST'])
def exam_detail():
    files = request.files['file']
    fname = secure_filename(files.filename)
    files.save(os.path.join('static/EXAMS', fname))
    title=request.form['textfield']
    cmd.execute("insert into exam values(null,'"+title+"','"+fname+"',curdate())")
    con.commit()
    return '''<script>alert("successful");windows:location="/pkb_exam_table"</script>'''

@app.route('/exam_view', methods=['GET','POST'])
def exam_table():
    if 'adid' in session:
        cmd.execute("SELECT * FROM EXAM")
        s = cmd.fetchall()
        return render_template("uni_announce_exam_table.html", val=s)
    else:
        return '''<script>alert("please login");window.location="/"</script>'''
@app.route('/delete_exam')
def delete_exam():
    id = request.args.get('id')
    cmd.execute("delete from exam where id='" + str(id) + "'")
    con.commit()
    return '''<script>alert("successful");windows:location="/exam_view"</script>'''

@app.route('/external_marks', methods=['GET', 'POST'])
def external_marks():
    regno = request.form['textfield']
    gpa = request.form['textfield2']
    files = request.files['file']
    fname = secure_filename(files.filename)
    files.save(os.path.join('static/EXTERNAL_MARKS', fname))
    cmd.execute("insert into external values(null,'"+regno+"','"+gpa+"','"+fname+"')")
    con.commit()
    return '''<script>alert("successful");windows:location="/external_view"</script>'''



@app.route('/external_view',methods=['GET','POST'])
def external_view():
    if 'adid' in session:
        cmd.execute("SELECT * FROM EXTERNAL")
        s = cmd.fetchall()
        return render_template("uni_EXTERNAL_MARK_TABLE.html", val=s)
    else:
        return '''<script>alert("please login");window.location="/"</script>'''

@app.route('/delete_external')
def delete_external():
    id = request.args.get('id')
    cmd.execute("delete from external where id='" +str(id)+ "'")
    con.commit()
    return '''<script>alert("successful");windows:location="/external_view"</script>'''

@app.route('/edit_external', methods=['GET', 'POST'])
def edit_external():

        id = session['id']
        regno = request.form['textfield']
        gpa = request.form['textfield2']
        try:
            files = request.files['file']
            fname = secure_filename(files.filename)
            cmd.execute("update external set register_number='" + regno + "',gpa='" + gpa + "',file='"+fname+"' where id='" + str(id) + "'")
            con.commit()
            return '''<script>alert("updated");window.location="/external_view"</script>'''
        except Exception as e:
            print(e)
            cmd.execute("update external set register_number='" + regno + "',gpa=" + gpa + " where id='" + str(
            id) + "'")
            con.commit()
            return '''<script>alert("updated");window.location="/external_view"</script>'''

@app.route('/getcertificate',methods=['GET','POST'])
def getcertificate():
    clg=request.form['select']
    con = pymysql.connect(host="localhost", user='root', passwd='root', port=3306, db='unique id')
    cmd = con.cursor()
    cmd.execute("Select * from college")
    d = cmd.fetchall()


    cmd.execute("SELECT * FROM `student` WHERE `college`='"+str(clg)+"'")
    s=cmd.fetchall()
    return  render_template('uni_certificate generation1.html',vals=s,nal=d)


@app.route('/add_internal',methods=['GET','POST'])
def add_internal():
    # cmd.execute("SELECT `register_number`,subject.`course_id`,`subject`.`sem` FROM student INNER JOIN SUBJECT ON  student.course_id=subject.course_id")
    # s = cmd.fetchall()
    cmd.execute("SELECT `id`,`course` FROM `course`")
    s = cmd.fetchall()
    return render_template("clg_ADD_INTERNAL_MARKS.html", val=s)

@app.route('/add_internal_list',methods=['GET','POST'])
def add_internal_list():
    if 'collegeid' in session:
        cmd.execute("SELECT `id`,`course` FROM `course`")
        s = cmd.fetchall()
        cmd.execute("SELECT `id`,`register_number` FROM `internal_marks`")
        d = cmd.fetchall()
        return render_template("clg_internal_marks_list.html", val=s, nal=d, sem=0)
    else:
        return '''<script>alert("please login");window.location="/"</script>'''

@app.route('/add_sub',methods=['GET','POST'])
def add_sub():
    if 'collegeid' in session:
        cmd.execute("SELECT `id`,`course` FROM `course`")
        s = cmd.fetchall()
        cmd.execute("select `id`,`sem` from `subject`")
        d = cmd.fetchall()
        return render_template("clg_ADD_MANAGE_STUD_1.html", val=s, nal=d)
    else:
        return '''<script>alert("please login");window.location="/"</script>'''


@app.route('/add_manage_sub',methods=['GET','POST'])
def add_manage_sub():
    if 'collegeid' in session:
         cmd.execute("SELECT `subject`.*,`course`.`course` FROM `course` JOIN `subject` ON `subject`.`course_id`=`course`.`id`")
         s=cmd.fetchall()
         return render_template("clg_ADD_MANAGE_STUD_TABLE2.html",val=s)
    else:
        return '''<script>alert("please login");window.location="/"</script>'''


@app.route('/approve_stud')
def approve_stud():
    if 'collegeid' in session:
        cmd.execute("select `register_number` FROM `college` WHERE id='"+str(session['collegeid'])+"' ")
        s1=cmd.fetchone()
        if s1 is not None:
            cmd.execute("SELECT `student`.* FROM `student` INNER JOIN `login` ON `login`.`id`=`student`.`login_id` WHERE `login`.`usertype`='pending' and student.college='"+str(s1[0])+"' ")
            s = cmd.fetchall()
            return render_template("clg_APPROVE_STUD.html", val=s)
        else:
            return "no value"
    else:
        return '''<script>alert("please login");window.location="/"</script>'''



@app.route('/approve_stud_table',methods=['GET', 'POST'])
def approve_stud_table():
    id=request.args.get('id')
    session['sid']=id
    cmd.execute("SELECT student.`name`,`student`.`register_number`,`student`.`gender`,`student`.`score`,`student`.`year_of_pass`,`student`.`email_id`,`student`.`phone_no`,course.course FROM student JOIN course ON student.course_id=course.id where student.login_id='"+str(id)+"'")
    s = cmd.fetchone()
    return render_template("clg_APPROVE_STUD_TABLE.html",val =s)


@app.route('/college')
def college():
    return render_template("clg_college.html")





@app.route('/downloadhall')
def downloadhall():
    if 'collegeid' in session:
        clg= session["collegeid"]

       # cid=request.form['select']
        cmd.execute("SELECT `student`.`register_number`,`student`.`name`,`student`.`gender`,`course`.`course`,`cipher_text`.`id`,`student`.`image`,`course`.`id`,studsem.sem,`student`.`login_id`FROM student INNER JOIN course ON student.`course_id`=`course`.`id` INNER JOIN `cipher_text` ON `student`.`login_id`=`cipher_text`.`uid` JOIN `studsem` ON `studsem`.`lid`=`student`.`login_id` JOIN `college` ON `college`.`register_number`=`student`.`college` WHERE `college`.`id`='"+str(clg)+"'")
        s = cmd.fetchall()
        return render_template("clg_DOWNLOAD_HALL_TICKETS.html", val=s)
    else:
        return '''<script>alert("please login");window.location="/"</script>'''


@app.route('/hall_verify')
def hall_verify():
    return render_template("clg_HALLTICKET_VERIFICATION.html")


@app.route('/int_mark')
def int_mark():
    cmd.execute("SELECT `id`,`course` FROM `course`")
    s = cmd.fetchall()
    cmd.execute("SELECT `id`,`course` FROM `course`")
    d = cmd.fetchall()
    return render_template("clg_ADD_MANAGE_STUD_1.html", val=s,nal=d)



@app.route('/exm_schedule')
def exm_schedule():
    if 'collegeid' in session:
        cmd.execute("SELECT * from exam")
        s = cmd.fetchall()
        return render_template("clg_view_examination_schedule.html", val=s)
    else:
        return '''<script>alert("please login");window.location="/"</script>'''


@app.route('/view_prof')
def view_prof():
    if 'collegeid' in session:
        cmd.execute("SELECT * FROM `college` where id='" + str(session["collegeid"]) + "'")
        s = cmd.fetchone()
        return render_template("clg_view_profile.html", i=s)
    else:
        return '''<script>alert("please login");window.location="/"</script>'''

@app.route('/get_sub',methods=['GET','POST'])
def get_sub():
    course=request.form['select']
    sem=request.form['select2']
    subject=request.form['textfield']
    cmd.execute("insert into subject values(null,'"+course+"','"+sem+"','"+subject+"')")
    con.commit()
    return '''<script>alert("sucessful");window.location="/add_manage_sub"</script>'''

@app.route('/edit_subject_call')
def edit_subject_call():
    id = request.args.get('id')
    session['id'] = id
    cmd.execute("SELECT `subject`.*,`course`.`course` FROM `course` JOIN `subject` ON `subject`.`course_id`=`course`.`id`  where subject.id='" +str(id)+ "'")
    s = cmd.fetchone()
    return render_template("clg_EDIT_MANAGE_STUD_1.html",val=s)



@app.route('/edit_subject', methods=['GET', 'POST'])
def edit_subject():
    course = request.form['select']
    sem = request.form['select2']
    subject = request.form['textfield']
    cmd.execute("update subject set course_id='"+course+"',sem='"+sem+"',subject='"+subject+"' where id='"+str(session['id'])+"'")
    con.commit()
    return '''<script>alert("sucessful");window.location="/add_manage_sub"</script>'''

@app.route('/approvestud2',methods=['GET', 'POST'])
def approvestud():

    btn=request.form['Submit']
    if btn=="APPROVE":
        cmd.execute("update login set usertype='student' where id='" +str(session['sid'])+"'")
        con.commit()
        return '''<script>alert("approved");window.location="/approve_stud"</script>'''

    else:
        cmd.execute("update login set usertype='rejected' where id='" +str(session['sid'])+"'")
        con.commit()
        return '''<script>alert("rejected");window.location="/approve_stud"</script>'''

@app.route('/get_internals', methods=['GET', 'POST'])
def get_internals():
    course = request.form['select']
    sem = request.form['select2']
    subject = request.form['textfield']
    cmd.execute("update subject set course_id='"+course+"',sem='"+sem+"',subject='"+subject+"' where id='"+str(session['id'])+"'")
    con.commit()
    return '''<script>alert("sucessful");window.location="/add_manage_sub"</script>'''

@app.route('/getinternalmarks', methods=['GET','POST'])
def getinternalmarks():
    registerno = request.form['select5']
    sem = request.form['select']
    course = request.form['select3']
    subject = request.form['select2']
    mark= request.form['textfield2']
    cmd.execute("insert into internal_marks values(null,'" + registerno + "','" +subject + "','" +mark+ "','" +course+ "','" +sem+ "')")
    con.commit()
    return '''<script>alert("sucessful");window.location="/add_internal"</script>'''

@app.route('/getinternalmarkslist', methods=['GET','POST'])
def getinternalmarkslist():
    cmd.execute("SELECT `id`,`course` FROM `course`")
    f = cmd.fetchall()
    registerno = request.form['select3']
    sem = request.form['select2']
    course =request.form['select']
    cmd.execute("SELECT internal_marks.`mark`,subject.subject FROM internal_marks INNER JOIN SUBJECT ON internal_marks.subject_id=subject.id WHERE (internal_marks.`register_number`='"+registerno+"') AND (internal_marks.`course_id`='" +str(course)+ "') AND (internal_marks.`sem`='" +sem+ "')")
    s=cmd.fetchall()
    return render_template("clg_internal_marks_list.html", vall=s,val=f,crse=int(course),sem=int(sem))

@app.route('/index', methods=['POST'])
def index():
    course = request.form['cr']
    sem=request.form['sem']

    cmd.execute("SELECT student.`register_number` FROM `student` JOIN `course` ON `course`.`id`=`student`.`course_id` WHERE `course`.`course`='"+course+"'")
    s=cmd.fetchall()
    cmd.execute("SELECT subject.`id`,subject.`subject` FROM `subject` JOIN `course` ON `subject`.`course_id`=`course`.`id` WHERE `course`.`course`='"+course+"' AND `subject`.`sem`='"+str(sem)+"'")
    s1=cmd.fetchall()
    re=['0','Select']
    for d in s:
        re.append(d[0])
        re.append(d[0])
    re.append("**")
    re.append("**")
    re =re+ ['0', 'Select']
    for d in s1:
        re.append(d[0])
        re.append(d[1])
    resp = make_response(jsonify( re))
    resp.status_code = 200
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/index1', methods=['POST'])
def index1():
    course = request.form['cr']
    sem=request.form['sem']

    cmd.execute("SELECT student.`register_number` FROM `student` JOIN `course` ON `course`.`id`=`student`.`course_id` WHERE `course`.`course`='"+course+"'")
    s=cmd.fetchall()
    re=['0','Select']
    for d in s:
        re.append(d[0])
        re.append(d[0])
    re.append("**")
    re.append("**")
    resp = make_response(jsonify( re))
    resp.status_code = 200
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/change_clg_password', methods=['GET','POST'])
def change_clg_password():
    cid=session['collegeid']
    newpassword = request.form['password2']
    confirmpass = request.form['password3']
    cpassword = request.form['password']
    cmd.execute("select password from login where password='"+cpassword+"' and id='"+str(cid)+"' ")
    s=cmd.fetchone()
    if s is not None:
        if newpassword==confirmpass:
            cmd.execute("update login set password='"+newpassword+"' where id='"+str(cid)+"'")
            con.commit()
            return '''<script>alert("password changed");window.location="/collegehome"</script>'''
        else:
            return '''<script>alert("password invalid");window.location="/collegehome"</script>'''

    return '''<script>alert("Invalid");window.location="/collegehome"</script>'''

@app.route('/delete_exam_pkb')
def delete_exam_pkb():
    id = request.args.get('id')
    cmd.execute("delete from exam where id='" + str(id) + "'")
    con.commit()
    return '''<script>alert("successful");windows:location="/pkb_exam_table"</script>'''


@app.route('/logout')
def logout():
	session.pop('email', None)
	return redirect('/')











































































































if __name__ == "__main__":
    app.run(host="192.168.43.123",port=5001)