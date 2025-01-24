from flask import Flask, request, render_template
import pickle

## Load the model
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])

def predict():
    if request.method == 'POST':
        data = int(request.form.get('weight'))
        print(f"Received weight: {data}")
        prediction = model.predict(scaler.transform([[data]]))
        return render_template('re.html', result=prediction[0])
    else:
       if not data:
            return render_template('re.html', result="Please enter a valid weight.")

    
if __name__ == '__main__':
    app.run()