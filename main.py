from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow import keras

app = Flask('app')

@app.route('/')
def main():
  return render_template('index.html')

@app.route('/submit', methods=['GET'])
def submit():
	if request.method == 'GET':
		hr = request.args.get('hr')
		iis = request.args.get('iis')
		avnn = request.args.get('avnn')
		rmssd = request.args.get('rmssd')
		pnn50 = request.args.get('pnn50')
		tp = request.args.get('tp')
		sdnn = request.args.get('sdnn')
		lf = request.args.get('lf')
		hf = request.args.get('hf')
		lf_hf = request.args.get('lf_hf')
		eda = request.args.get('eda')
		modelPath = '/Result3'
		loadModel = tf.keras.models.load_model(modelPath)
		loadModel.predict([hr, avnn, iis, sdnn, rmssd, pnn50, tp, lf, hf, lf_hf, eda], epochs=2)
		return render_template('result.html', result="a")

@app.route('/getHelp')
def getHelp():
	return render_template('getHelp.html')
	
app.run(host='0.0.0.0', port=8080)