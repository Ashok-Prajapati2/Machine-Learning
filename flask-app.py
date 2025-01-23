from flask import Flask, request, render_template
import pickle
from sklearn.preprocessing import StandardScaler


## Load the model
model = pickle.load(open('model.pkl', 'rb'))
sclar = pickle.load(open('scaler.pkl', 'rb'))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])

def predict():
    if request.method == 'POST':
        data = float(request.form.get('weight'))
        print(data)
        newdata = StandardScaler.transform([[data]])
        prediction = model.predict(newdata) 
        return render_template('re.html', result=prediction[0])
    else:
        return render_template('re.html')
    
if __name__ == '__main__':
    app.run()