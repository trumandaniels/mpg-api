from flask import Flask, jsonify, request
from tensorflow import keras
import tensorflow as tf
from pathlib import Path

app = Flask(__name__)

load_path = Path.cwd().joinpath("mpg_model_saved") #change if the saved model folder isn't in this directory
model = keras.models.load_model(load_path)


#Only POST method is defined
@app.route("/", methods=["POST"])
def predict():
    data = request.json
    input_dict = {name: tf.convert_to_tensor([value]) for name, value in data.items()}
    predictions = model.predict(input_dict)    
    return jsonify({"mpg": str(predictions[0][0])})

if __name__ == "__main__":
    app.run(debug=True) #debug=False in production
