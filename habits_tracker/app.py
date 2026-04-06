from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

habits = [
    "Practice coding (30 min)",
    "Practice French",
    "Drink 1.5L water",
    "Sleep before 23:00",
    "Physical exercise"
]



@app.route("/")
def home():
    today = datetime.now().strftime("%Y-%m-%d")
    completed = []

    try:
        with open("progress.txt", "r") as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip()
                print("DEBUG:", line)  # 👈 temporary debug

                if today in line:
                    completed.append(line)

    except FileNotFoundError:
        print("No file found")

    print("COMPLETED:", completed)  

    return render_template(
    "index.html",
    habits=habits,
    completed=completed,
    total=len(habits)
)

@app.route("/done", methods=["POST"])
def done():
    habit = request.form["habit"]

    # If it's physical exercise → ask for minutes
    if habit == "Physical exercise":
        minutes = request.form.get("minutes")

        if minutes:
            habit = f"Physical exercise ({minutes} min)"
        else:
            return """
                <h2>Enter minutes:</h2>
                <form method="post">
                    <input type="hidden" name="habit" value="Physical exercise">
                    <input type="number" name="minutes" placeholder="Minutes">
                    <button type="submit">Submit</button>
                </form>
            """

    date = datetime.now().strftime("%Y-%m-%d")

    with open("progress.txt", "a") as file:
        file.write(f"{date} - {habit}\n")

    return f"<h2>✅ {habit} saved!</h2><a href='/'>Go back</a>"


if __name__ == "__main__":
    app.run(debug=True)
    


