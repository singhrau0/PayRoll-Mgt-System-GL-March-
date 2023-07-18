from flask import Flask, render_template,jsonify,request
from employee import Employee
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/employee/signup', methods=['GET','POST'])
def signup():
    if request.method=='POST':
        eid = request.form.get('eid')
        ename = request.form.get('ename')
        dptid = request.form.get('dptid')
        designation = request.form.get('designation')
        email = request.form.get('email')
        contact = request.form.get('contact')
        address = request.form.get('address')
        print(eid,ename,dptid)
        emp = Employee()
        emp.empinsert(eid = eid,ename=ename,dptid = dptid,designation=designation,email=email,contact=contact,address=address)
        return render_template('message.html')
    else:
        return render_template('signup.html')



if __name__=='__main__':
    app.run()


