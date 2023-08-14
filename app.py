from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save_data():
    input1 = request.form.get("input1")
    input2 = request.form.get("input2")
    input3 = request.form.get("input3")

    # Save the data to a file or database
    with open("data.txt", "a") as f:
        f.write(f"{input1}, {input2}, {input3}\n")

    return "Data saved successfully."

if __name__ == "__main__":
    app.run(debug=True)
