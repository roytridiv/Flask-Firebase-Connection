import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from flask import Flask, render_template , request

# Fetch the service account key JSON file contents
cred = credentials.Certificate('sanatan-cdd1b-firebase-adminsdk-56vl3-6bf19d7238.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://sanatan-cdd1b.firebaseio.com/'
})



app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/result',methods = ['POST'])
def result():
   if request.method == 'POST':
              
       db_ref = request.form['db_ref']
       id_num = request.form['c_id']
       num = request.form['num']
       letter =request.form['letter']
       title = request.form['title']
       lyric = request.form['lyric']
       porjay = request.form['porjay']
       upo_porjay = request.form['upo_porjay']
       song_num = request.form['song_num']
       taal =  request.form['taal']
       raag = request.form['raag']
       bn_yr = request.form['bn']
       eng_yr = request.form['eng']
       age = request.form['age']
       write_palce = request.form['place']
       publish = request.form['date']
       not_info = request.form['not_info']
       writer = request.form['writer']
       foot_note = request.form['foot_note']
       lyric_change = request.form['lyrical_change']
       discussion = request.form['disc']
       not_file = request.form['not_file']
       url = request.form['url']

    #    db.reference(db_ref).child("2").set(None)

       
       # As an admin, the app has access to read and write all data, regradless of Security Rules
       ref = db.reference(db_ref)
       # print(ref.get())


       posts_ref = ref.child(id_num)



       posts_ref.set({
                     "number": num,
                     "letter": letter,
                     "title": title,
                     "lyric": lyric,
                     "porjay": porjay,
                     "upo_porjay": upo_porjay,
                     "song_no":song_num,
                     "raag": raag,
                     "taal": taal,
                     "write_bn": bn_yr,
                     "write_en": eng_yr,
                     "age": age,
                     "write_place": write_palce,
                     "pubish": publish,
                     "notation_info": not_info,
                     "notation_writer": writer,
                     "footnote": foot_note,
                     "lyric_change": lyric_change,
                     "discussion": discussion,
                     "notation_file":not_file,
                     "urlNotation":url
                      })

     
       return "Input done"

@app.route('/delete',methods = ['POST'])
def delete():
   if request.method == 'POST':
       db_ref = request.form['db_ref']
       id_num = request.form['c_id']
       
        # As an admin, the app has access to read and write all data, regradless of Security Rules
       ref = db.reference(db_ref)
       
       posts_ref = ref.child(id_num)

       posts_ref.delete()

       return "Deletion Done"

@app.route('/delete_page',methods = ['GET'])
def delete_page():
   if request.method == 'GET':
       return render_template('delete.html')

@app.route('/add_page',methods = ['GET'])
def add_page():
   if request.method == 'GET':
       return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)