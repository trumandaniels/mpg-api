#https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html
#https://curiousily.com/posts/deploy-keras-deep-learning-project-to-production-with-flask/

from flask import Flask, jsonify, request
from tensorflow import keras
import tensorflow as tf

app = Flask(__name__)

model = keras.models.load_model("/home/truman/Documents/DataAPI/mpg_model_saved/")

@app.route("/", methods=["POST"])
def predict():
    data = request.json
    input_dict = {name: tf.convert_to_tensor([value]) for name, value in data.items()}
    predictions = model.predict(input_dict)    
    return jsonify({"mpg": str(predictions[0][0])})

if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
        "please wait until server has fully started"))
    app.run(debug=True)
