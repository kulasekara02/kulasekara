from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            num1 = float(request.form.get("num1", 0))
            num2 = float(request.form.get("num2", 0))
            operation = request.form.get("operation")

            if operation == "add":
                result = num1 + num2
            elif operation == "sub":
                result = num1 - num2
            elif operation == "mul":
                result = num1 * num2
            elif operation == "div":
                if num2 == 0:
                    error = "Cannot divide by zero."
                else:
                    result = num1 / num2
            else:
                error = "Unknown operation."

        except ValueError:
            error = "Please enter valid numbers."

    return render_template("index.html", result=result, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
