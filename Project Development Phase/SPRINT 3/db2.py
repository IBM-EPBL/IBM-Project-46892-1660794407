from flask import Flask ,render_template, request, session,flash,redirect
import ibm_db

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30367;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=gzx16769;PWD=CIOWl8d3r3syjfcj","","")
print(conn)
print("connection successfull")

app = Flask(__name__)

@app.route('/signup',methods=['POST'])
def signup():
    print("checked")
    fullname=request.form[fullname]
    username=request.form[username]
    email=request.form[email]
    pssword=request.form[pssword]
    sql="SELECT * FROM user WHERE username=?"
    statement=ibm_db.prepare(conn,sql)
    ibm_db.bind_param(statement,1,username)
    ibm_db.execute(statement)
    acc=ibm_db.fetch_assoc(statement)
    if acc:
        "username already exists"
        
    else:
        sql="INSERT INTO user(username,password,fullname,email) values(?,?,?,?)"
        statement=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(statement,1,fullname)
        ibm_db.bind_param(statement,2,username)
        ibm_db.bind_param(statement,3,email)
        ibm_db.bind_param(statement,4,pssword)
        ibm_db.execute(statement)
        print("created")
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)