from flask import Flask , render_template ,request

app = Flask(__name__) # object of flask the main file
# Entire code will be between this and app.run(debug=True)

@app.route('/')
def base():
    return render_template('home.html')

@app.route('/gallary')
def gallary():
    return render_template("gallary.html")

@app.route('/cart')
def cart():
    return "welcome to cart page"

@app.route('/contact')
def contact():
    return "welcome to contact page"

@app.route('/predict', methods=['post'])
def predict():

    # Load the model
    import pickle
    model = pickle.load(open('diabetic_79.pkl','rb'))

    Pregnancies = request.form.get('Pregnancies')
    Glucose = request.form.get('Glucose')
    BP = request.form.get('BP')
    SkinThickness= request.form.get('SkinThickness')
    Insulin = request.form.get('Insulin')
    BMI = request.form.get('BMI')
    Diabetes = request.form.get('Diabetes')
    Age = request.form.get('Age')


   

    print(Pregnancies,Glucose,BP,SkinThickness,Insulin,BMI,Diabetes,Age)
    Output = model.predict([[Pregnancies,Glucose,BP,SkinThickness,Insulin,BMI,Diabetes,Age]])

    if  Output[0]==0:

        data  = 'person is not diabetic'
    else:
        data  = 'person is diabetic'
    

    return render_template('predict.html',data = data)

if __name__ == "__main__":
    app.run(debug=True)




 









# @app.route('') - it will default always
# /anyword = if we put any word after slash and define function for it , it will give the return from function
# @app.route('/gallary') 
#  http://127.0.0.1:5000/gallary : will return "welcome to gallary"

# http://127.0.0.1:5000/ 
# http : protocols
# Ip address : 127.0.0.1 - localhost
# 5000 - port number (gateway)   
# / - route
# here we have write a function for "/" and return hello world , so we will again run the server by ctrl+c and then it will work.
# debug = True , we don't have to refresh the server everytime we make changes.
# creating a templates folder is mandatory with this name only in same path and then we create different html file inside it .

