from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)


MODEL_PATH = "sales_model.pkl"

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    model = None
    print(" Model not found!")


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            month = int(request.form.get("month"))
            day = int(request.form.get("day"))

            if month < 1 or month > 12:
                error = "Month must be between 1 and 12"
            elif day < 1 or day > 31:
                error = "Day must be between 1 and 31"
            elif model is None:
                error = "Model not loaded"
            else:
                pred = model.predict([[month, day]])
                prediction = round(pred[0], 2)

        except Exception as e:
            error = str(e)

    return render_template("index.html", prediction=prediction, error=error)


@app.route("/health")
def health():
    return {"status": "ok", "model_loaded": model is not None}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  
    app.run(host="0.0.0.0", port=port)
   
