import os
from flask import *

from src.test_face import test_face

app=Flask(__name__)
import pymysql
from werkzeug.utils import secure_filename
con=pymysql.connect(host="localhost", user='root', passwd='root', port=3306, db='unique id')
cmd=con.cursor()

from src.rsa import *

app= Flask(__name__)
app.secret_key = 'abc'

@app.route('/login',methods=['GET','POST'])
def login():
    try:
        con = pymysql.connect(host="localhost", user='root', passwd='root', port=3306, db='unique id')
        cmd = con.cursor()
        uname=request.form['uname']
        passwd=request.form['pass']
        try:
            cmd.execute("select * from login where username='"+uname+"' and password='"+passwd+"' and  usertype='student'")
            s=cmd.fetchone()
            con.close()
            print(s)
            if s is  not None:
                id=s[0]
                print(id)

                return jsonify({'task': str(id)})

            else:
                return jsonify({'task': "invalid"})
        except Exception as e:
            print(str(e))
            con.close()

            return jsonify({'task': "invalid"})
    except Exception as e:
            print(e)
            return jsonify({'task': "success"})

@app.route('/reg', methods=['GET', 'POST'])
def reg():
    try:
        con = pymysql.connect(host="localhost", user='root', passwd='root', port=3306, db='unique id')
        cmd = con.cursor()
        name = request.form['name']
        registerno = request.form['regno']
        course = request.form['course']
        gender = request.form['gender']
        score = request.form['rank']
        year = request.form['yearofpass1'] + "," + request.form['yearofpass2']
        email = request.form['email']
        phone = request.form['phone']
        files = request.files['files']
        college= request.form['college']
        sem=request.form['sem']
        fname = secure_filename(files.filename)
        files.save(os.path.join('static/students',fname))

        # user=request.form['user']
        # pwd2=request.form['pwd']

        cmd.execute("insert into login values(null,'" + email + "','" + registerno + "','pending')")
        id = con.insert_id()
        cmd.execute("insert into student values(null,'" + name + "','" + registerno + "','" + course + "','" + gender + "','" + score + "','" + year + "','" + fname + "','" + email + "','" + phone + "','" + str(id) + "','"+college+"')")
        cmd.execute("insert into studsem values('"+str(id)+"','"+sem+"')")
        con.commit()
        con.close()
        return jsonify({'task': "success"})
    except Exception as e:
        print("err" + str(e))

@app.route('/change_password', methods=['GET','POST'])
def change_password():
    con = pymysql.connect(host="localhost", user='root', passwd='root', port=3306, db='unique id')
    cmd = con.cursor()
    newpassword = request.form['newpassword']
    cid = request.form['id']
    cpassword = request.form['cpassword']
    confpassword = request.form['confpasssword']
    cmd.execute("select password from login where password='"+cpassword+"' and id='"+str(cid)+"' ")
    con.close()
    s=cmd.fetchone()
    if s is not None:
        if newpassword == confpassword:
            cmd.execute("update login set password='" + newpassword + "' where id='" + str(cid) + "'")
            con.commit()
            con.close()
            return jsonify({'task': "success"})
        else:
            return jsonify({'task': "invalid"})

@app.route('/view_mark', methods=['GET','POST'])
def view_mark():
    type=request.form['type']
    sid=request.form['id']
    con = pymysql.connect(host="localhost", user='root', passwd='root', port=3306, db='unique id')
    cmd = con.cursor()
    if type=='internal':
        cmd.execute("SELECT `internal_marks`.`mark`,`subject`.`subject` FROM `internal_marks` INNER JOIN `subject` ON `subject`.`id`=`internal_marks`.`subject_id` JOIN `student` ON `student`.`register_number`=`internal_marks`.`register_number`  WHERE  `student`.`login_id`='"+str(sid)+"'")
    else:
        cmd.execute("SELECT `gpa`,`file` FROM `external` INNER JOIN `student` ON `student`.`register_number`=`external`.`register_number` WHERE `student`.`login_id`='"+str(sid)+"'")
    s=cmd.fetchall();
    print(s)
    con.close()
    row_headers=[x[0] for x in cmd.description]
    json_data=[]
    for result in s:
        json_data.append(dict(zip(row_headers,result)))
    print(json_data)
    return jsonify(json_data)

@app.route('/view_profile', methods=['GET','POST'])
def view_profile():
    con = pymysql.connect(host="localhost", user='root', passwd='root', port=3306, db='unique id')
    cmd = con.cursor()
    sid=request.form['id']
    cmd.execute("select * from student where login_id='"+str(sid)+"'")
    s = cmd.fetchall();
    con.close()
    print(s)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in s:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)


@app.route('/view_course',methods=['GET','POST'])
def view_course():
    con = pymysql.connect(host="localhost", user='root', passwd='root', port=3306, db='unique id')
    cmd = con.cursor()
    cmd.execute("select * from `course`")
    m=cmd.fetchall();
    con.close()
    print(m)
    row_headers = [x[0] for x in cmd.description]
    json_data = []
    for result in m:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)





@app.route('/verification2',methods=['POST','GET'])
def verification2():
    con = pymysql.connect(host="localhost", user='root', passwd='root', port=3306, db='unique id')
    cmd = con.cursor()
    regno = request.form['regno']
    msg= request.form['msg']
    print(regno)
    cmd.execute("SELECT  login_id FROM student WHERE `register_number`='"+regno+"'")
    s=cmd.fetchone()
    print("s",s)
    # encrypted_msg=flask.request.form['decode_data']
    encrypted_msg=msg
    # print(encrypted_msg)
    cmd.execute("SELECT `pubkey` FROM `cipher_text` WHERE `uid`='"+str(s[0])+"'")
    publickey=cmd.fetchone()
    key=publickey[0]
    pk = RSA.importKey(key)
    print('pk--------------',pk)
    decrypted_msg =decrypt_message(encrypted_msg,pk)
    print("decy msg"+ str(decrypted_msg))
    print(type(decrypted_msg))
    data = str(decrypted_msg.decode('utf-8')).split('#')
    ipd=data[0]
    icd=data[1]
    ocd=data[2]
    res=ocd+"#"+ipd+"#"+icd
    con.close()


    return jsonify({'task': res})



@app.route('/photoupload', methods=['POST','GET'])
def photoupload():
    con = pymysql.connect(host="localhost", user='root', passwd='root', port=3306, db='unique id')
    cmd = con.cursor()
    file=request.files['files']
    rgno=request.form['regno']
    filename=str(secure_filename(file.filename))
    print(file.filename)
    file.save(filename)
    print(filename)
    mk = test_face()
    cmd.execute("select image from student where register_number='"+rgno+"'")
    print("select image from student where register_number='" + rgno + "'")
    s=cmd.fetchone()

    s = mk.test_face1(filename,s[0])
    print("s---",s)
    session['v_mnk'] = s
    # data = s.split('#')
    # ipd = float(data[0])
    # icd = float(data[1])
    # ocd = float(data[2])
    con.close()
    return jsonify({'task': s})


# @app.route('/downloadhall', methods=['POST','GET'])
# def downloadhall():
#     sid=request.form['sid']
#     cmd.execute(
#         "SELECT `student`.`register_number`,`student`.`name`,`student`.`gender`,`course`.`course`,`cipher_text`.`id`,`student`.`image`,`course`.`id`,studsem.sem FROM student INNER JOIN course ON student.`course_id`=`course`.`id` INNER JOIN `cipher_text` ON `student`.`login_id`=`cipher_text`.`uid` JOIN `studsem` ON `studsem`.`lid`=`student`.`login_id` WHERE `student`.`login_id`= '" + str(
#             sid) + "'")
#     s = cmd.fetchall()
#     print(s, "certificate")
#     cmd.execute("select * from subject where course_id='" + str(s[0][6]) + "' and sem='" + str(s[0][7]) + "'")
#     res = cmd.fetchall()



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)