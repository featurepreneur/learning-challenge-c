from flask import Flask,render_template,request,url_for,redirect
import data




app = Flask(__name__ )

actname = [i['Actress Name'] for i in data.movieslist]

@app.route('/')
@app.route('/crowdengine/')
def crowdengine():
    return render_template('mainpage.html',movie_list = data.movieslist)

@app.route('/download/')
def download():
    return data.get_csv(a = app)
    
    

@app.route('/pyhackons/')
def pyhackons():
    return render_template('pyhackons.html')

@app.route('/crowdengine/<string:name>')
def movie_name(name):
    
    if name not in actname:
        return render_template('error.html',error="Name Not Found")
    return render_template('movies.html' ,name = name)


@app.route('/crowdengine/pre/')
def pre():
    name = request.args.get('page')
    index = actname.index(name)
    
    name = data.page('pre',index)
    return redirect(url_for('movie_name',name = name) )
    
   

@app.route('/crowdengine/next/')
def next():
    name = request.args.get('page')
    index = actname.index(name)
    
    name = data.page('next',index)
    
    return redirect(url_for('movie_name',name = name))

@app.route('/crowdengine/write/',methods=["POST"])   
def write_db():
    
    if request.method == 'POST':
        
        movie = request.form["moviescount"]
        actor = request.form["name"]
        dur = request.form["screenduration"]
        insta = request.form["instagramfollowers"]
        dress = request.form["dressmatchmeter"]
        criticscore = request.form["criticscore"]
        consistency = request.form["consistency"]
        
        data.write(movie=movie,actor=actor,duration=dur,insta=insta,dress=dress,consistency=consistency,criticscore=criticscore)
        
    return render_template('movies.html',p="ok" ,name=actor)

@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    
    return render_template('error.html',error=e )
    
@app.route('/table')
def table():
    data1 = data.table()
    return render_template('table.html',data=data1,view=True)







if __name__ == "__main__":
    app.run()

    
