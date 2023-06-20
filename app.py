import pickle
from flask import Flask, render_template, request

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

# If someone opens the server the following code will be executed


@app.route('/')
def htmlPage():
    return render_template('index.html')


@app.route('/predict', methods=['post'])
def predict():
    # collect data from form

    von = float(request.form['von'])
    vop = float(request.form['vop'])
    vok = float(request.form['vok'])
    vot = float(request.form['vot'])
    voh = float(request.form['voh'])
    voph = float(request.form['voph'])
    vor = float(request.form['vor'])
    result = model.predict([[von, vop, vok, vot, voh, voph, vor]])
    
    input_data = "at Nitrogen = " + str(von) + ", Phosphorus = " + str(vop) + ", Potassium = " + str(vok) + ", Temperature = " + str(vot) + ", Humidity = " + str(voh) + ", pH = " + str(voph) + " and Rainfall = " + str(vor)
    
    crop = "The crop is:"
    return render_template('index.html', result=result[0],input_data=input_data,crop=crop)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
