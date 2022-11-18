from flask import Flask ,render_template, request, session,flash,redirect

import ibm_db

app = Flask(__name__)

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30367;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=gzx16769;PWD=CIOWl8d3r3syjfcj","","")
print (conn)
print("connection successfull")


@app.route('/login', methods=['POST', "GET"])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        pssword = request.form.get('password')

        sql = "select * from GZX16769.IVM where username = ? and password = ?"
        stmt = ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt, 1, username)
        ibm_db.bind_param(stmt, 2, pssword)
        ibm_db.execute(stmt)
        user = ibm_db.fetch_assoc(stmt)
        if user:
              session['username'] = user['username']
              session['is_loggedin'] = True
              return redirect("rl_for('dashboard')")

        user = ibm_db.fetch_assoc(stmt)

        if user:
            print(user)
            print(user['ID'])
            user_password = user['PSSWORD']
            
        else:
                flash('Password is incorrect')
                return render_template('login.html')
       




@app.route('/signup', methods=['POST', "GET"])
def signup():
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        username = request.form.get('username')
        email = request.form.get('email')
        pssword = request.form.get('password')
        
        
        sql = "INSERT INTO GZX16769.IVM(fullname,username,email,pssword) VALUES('{}','{}','{}','{}')".format(fullname,username,email,pssword)
        ibm_db.exec_immediate(conn,sql)


       
       
        return render_template('login.html')
    else:
        return render_template('signup.html')


if __name__ == "__main__":
    app.run(debug=True)
