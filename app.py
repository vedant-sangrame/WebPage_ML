from flask import Flask, request
import pickle
import os   # ✅ add this

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

def render_page(result=None):
    result_html = ""
    if result is not None:
        result_html = f"<p><strong>Prediction:</strong> {result}</p>"
    return f"""<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Prediction</title>
  </head>
  <body>
    <h1>Prediction App</h1>
    <form method="post" action="/predict">
      <label>Input:</label>
      <input type="number" name="input" step="any" required />
      <button type="submit">Predict</button>
    </form>
    {result_html}
  </body>
</html>"""

@app.route('/')
def home():
    return render_page()

@app.route('/predict', methods=['POST'])
def predict():
    input_value = float(request.form['input'])
    prediction = model.predict([[input_value]])
    return render_page(prediction[0])

# ✅ IMPORTANT CHANGE HERE
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
