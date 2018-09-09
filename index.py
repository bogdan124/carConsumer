from flask import Flask,render_template,request,redirect,url_for,flash,session,jsonify
import pymysql
from flask_socketio import SocketIO ,send,emit


app=Flask(__name__)
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg', 'gif','obj','mtl'])
app.config['SECRET_KEY'] = 'mysecret'
socketio=SocketIO(app)
connection=pymysql.connect(host='localhost',use_unicode=True,charset="utf8",user='root',password='',db='energysaver',autocommit=True) 
app.config['MYSQL_DATABASE_CHARSET'] = 'utf8mb4'
con=connection.cursor()



@app.route('/verify_login',methods=['POST','GET'])
def verify_login():
            if request.method=='POST' :
                    uname_user=request.form['uname']
                    uname_pass=request.form['pass']
                    sql="SELECT * FROM users WHERE email='"+str(uname_user)+"' AND pass='"+str(uname_pass)+"'"
                    second=con.execute(sql)
                    print(second)
                    if int(second)==1:                
                            rewq=con.fetchall()
                            session['connect']='connect'
                            connect=session['connect']
                            for i in rewq:
                                session['id']=i[0]
                            id12=session['id']
                            print(id12)
                            session.permanent=True
                            return url_for("profile",id=id12,connect=connect)                        
                    elif int(second)!=1:
                        return "Wrong email or password!"

                    
@app.route('/main_page',methods=['POST','GET'])
def main_page():
    if session.get('id')!=None and session.get('connect'):
        return redirect(url_for("profile",id=session['id'],connect=session['connect']))
    return render_template("main.html")


@app.route('/profile',methods=['POST','GET'])
def profile():
     id=request.args['id']
     id13=session['id']
     connect=session['connect']
     if id13=='':
         return redirect(url_for('logout'))
##     if url=="":
##         return redirect(url_for('logout'))
     if id13==None :
         return redirect(url_for('logout'))
     if int(id)!=int(id13):
         return redirect(url_for('logout'))
     if request.args['connect'] != 'connect':
         return redirect(url_for('logout'))
     if request.args['connect'] == '':
         return redirect(url_for('logout'))   
     return render_template("lateral_menu.html")

@app.route('/cars_to_show',methods=['POST','GET'])
def cars_to_show():
     id=request.args['id']
     id13=session['id']
     connect=session['connect']
     if id13=='':
         return redirect(url_for('logout'))
##     if url=="":
##         return redirect(url_for('logout'))
     if id13==None :
         return redirect(url_for('logout'))
     if int(id)!=int(id13):
         return redirect(url_for('logout'))
     if request.args['connect'] != 'connect':
         return redirect(url_for('logout'))
     if request.args['connect'] == '':
         return redirect(url_for('logout'))  
     return render_template("profile.html")


@app.route('/logout',methods=['POST','GET'])
def logout():
    session.pop('id', None)
    session.pop('connect', None)
    return redirect(url_for('login'))



@app.route('/login',methods=['POST','GET'])
def login():
    if session.get('id')!=None and session.get('connect'):
        return redirect(url_for("profile",id=session['id'],connect=session['connect']))
    return render_template("login.html")







@app.route('/',methods=['POST','GET'])
def index():
    if session.get('id')!=None and session.get('connect'):
        return redirect(url_for("profile",id=session['id'],connect=session['connect']))
    else:
        return redirect(url_for("logout"))
    return render_template("profile.html")



@app.route('/pricing',methods=['POST','GET'])
def pricing():
    if session.get('id')!=None and session.get('connect'):
        return redirect(url_for("profile",id=session['id'],connect=session['connect']))
    return render_template("pricing.html")    



@app.route('/documentation',methods=['POST','GET'])
def documentation():
    if session.get('id')!=None and session.get('connect'):
        return redirect(url_for("profile",id=session['id'],connect=session['connect']))
    return render_template("documentation.html")






@app.route('/location',methods=['POST','GET'])
def location():
    return render_template("location.html")

@app.route('/vehicle',methods=['POST','GET'])
def vehicle():
    return 'vehicle'

@app.route('/parking',methods=['POST','GET'])
def parking():
    return 'parking'

@app.route('/energy',methods=['POST','GET'])
def energy():
    return 'energy'


@app.route('/parking_slots',methods=['POST','GET'])
def parking_slots():
     id=request.args['id']
     id13=session['id']
     connect=session['connect']
     if id13=='':
         return redirect(url_for('logout'))
##     if url=="":
##         return redirect(url_for('logout'))
     if id13==None :
         return redirect(url_for('logout'))
     if int(id)!=int(id13):
         return redirect(url_for('logout'))
     if request.args['connect'] != 'connect':
         return redirect(url_for('logout'))
     if request.args['connect'] == '':
         return redirect(url_for('logout'))   
     return render_template("parking_slots.html")
    
@app.errorhandler(500)
def page_not_found(e):
    return redirect(url_for('logout'))


@app.route('/accidents',methods=['POST','GET'])
def accidents():
     id=request.args['id']
     id13=session['id']
     connect=session['connect']
     if id13=='':
         return redirect(url_for('logout'))
##     if url=="":
##         return redirect(url_for('logout'))
     if id13==None :
         return redirect(url_for('logout'))
     if int(id)!=int(id13):
         return redirect(url_for('logout'))
     if request.args['connect'] != 'connect':
         return redirect(url_for('logout'))
     if request.args['connect'] == '':
         return redirect(url_for('logout')) 
     return render_template("accidets.html")

@app.route('/get_data_accidets',methods=['POST','GET'])
def get_data_accidets():
    start=request.args['start']
    finish=request.args['finish']
    sql="SELECT * FROM cars_data LIMIT "+str(start)+","+str(finish)+""
    con.execute(sql)
    data=con.fetchall()
    return jsonify(data)





@app.route('/get_car_data',methods=['POST','GET'])
def get_car_data():
##     id=request.args['id']
##     id13=session['id']
##     connect=session['connect']
##     if id13=='':
##         return redirect(url_for('logout'))
####     if url=="":
####         return redirect(url_for('logout'))
##     if id13==None :
##         return redirect(url_for('logout'))
##     if int(id)!=int(id13):
##         return redirect(url_for('logout'))
##     if request.args['connect'] != 'connect':
##         return redirect(url_for('logout'))
##     if request.args['connect'] == '':
##         return redirect(url_for('logout'))   
     start=request.args['start']
     finish=request.args['finish']
     sql="SELECT * FROM cars LIMIT "+str(start)+","+str(finish)
     con.execute(sql)
     get_cars_data=con.fetchall()
     return jsonify(get_cars_data)


@app.route('/parking_2',methods=['POST','GET'])
def parking_2():
    start=request.args['start']
    finish=request.args['finish']
    sql="SELECT * FROM parking LIMIT "+str(start)+","+str(finish)+""
    con.execute(sql)
    select_parking_slot=con.fetchall()
    return jsonify(select_parking_slot)

@app.route('/maps_show',methods=['POST','GET'])
def maps_show():
    return render_template("show_maps.html")


if __name__=='__main__':
      app.secret_key="uhsd;iuasdf2f23rgvugersdfdsfsdfsdsdfswq2314123234124gergw["
      socketio.run(app,host='0.0.0.0',port=5000)
