from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Display Disasters
@app.route("/disaster")
def disaster():

    conn = sqlite3.connect("disaster.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM disasters")
    disasters = cursor.fetchall()

    conn.close()

    return render_template("disaster.html", disasters=disasters)

# Add Disaster
@app.route("/add_disaster", methods=["POST"])
def add_disaster():

    dtype = request.form["type"]
    location = request.form["location"]
    severity = request.form["severity"]
    description = request.form["description"]

    conn = sqlite3.connect("disaster.db")
    cursor = conn.cursor()

    cursor.execute(
    "INSERT INTO disasters(disaster_type, location, severity, description) VALUES (?, ?, ?, ?)",
    (dtype, location, severity, description)
)

    conn.commit()
    conn.close()

    return redirect("/disaster")


# Edit Disaster
@app.route("/edit_disaster/<int:id>")
def edit_disaster(id):

    conn = sqlite3.connect("disaster.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM disasters WHERE id=?", (id,))
    disaster = cursor.fetchone()

    conn.close()

    return render_template("edit_disaster.html", disaster=disaster)


# Delete Disaster
@app.route("/delete_disaster/<int:id>")
def delete_disaster(id):

    conn = sqlite3.connect("disaster.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM disasters WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return redirect("/disaster")

@app.route("/update_disaster/<int:id>", methods=["POST"])
def update_disaster(id):

    dtype = request.form["type"]
    location = request.form["location"]
    severity = request.form["severity"]
    description = request.form["description"]

    conn = sqlite3.connect("disaster.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE disasters
        SET disaster_type=?, location=?, severity=?, description=?
        WHERE id=?
    """, (dtype, location, severity, description, id))

    conn.commit()
    conn.close()

    return redirect("/disaster")
@app.route("/delete_drone/<int:id>")
def delete_drone(id):

    conn = sqlite3.connect("disaster.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM drones WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return redirect("/view_drones")

@app.route("/dashboard")
def dashboard():

    conn = sqlite3.connect("disaster.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM disasters")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM disasters WHERE severity='High'")
    high = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM disasters WHERE severity='Medium'")
    medium = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM disasters WHERE severity='Low'")
    low = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "dashboard.html",
        total=total,
        high=high,
        medium=medium,
        low=low
    )

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("disaster.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users(fullname, email, password) VALUES (?, ?, ?)",
            (fullname, email, password)
        )

        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("register.html")
# Login
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("disaster.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )

        user = cursor.fetchone()

        conn.close()

        if user:
            return redirect("/disaster")
        else:
            return "Invalid Email or Password"

    return render_template("login.html")

@app.route("/drone")
def drone():

    conn = sqlite3.connect("disaster.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM drones")
    drones = cursor.fetchall()

    conn.close()

    return render_template("drone.html", drones=drones)

@app.route("/add_drone", methods=["POST"])
def add_drone():

    drone_name = request.form["drone_name"]
    model = request.form["model"]
    status = request.form["status"]
    battery = request.form["battery"]

    conn = sqlite3.connect("disaster.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO drones(drone_name, model, status, battery) VALUES(?,?,?,?)",
        (drone_name, model, status, battery)
    )

    conn.commit()
    conn.close()

    return redirect("/drone")
@app.route("/view_drones")
def view_drones():

    conn = sqlite3.connect("disaster.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM drones")
    drones = cursor.fetchall()

    conn.close()

    return render_template("view_drones.html", drones=drones)
@app.route("/edit_drone/<int:id>")
def edit_drone(id):

    conn = sqlite3.connect("disaster.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM drones WHERE id=?", (id,))
    drone = cursor.fetchone()

    conn.close()

    return render_template("edit_drone.html", drone=drone)

@app.route("/edit_rescue/<int:id>")
def edit_rescue(id):

    conn = sqlite3.connect("disaster.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM rescue_team WHERE id=?", (id,))
    team = cursor.fetchone()

    conn.close()

    return render_template("edit_rescue.html", team=team)

@app.route("/update_drone", methods=["POST"])
def update_drone():

    id = request.form["id"]
    drone_name = request.form["drone_name"]
    model = request.form["model"]
    status = request.form["status"]
    battery = request.form["battery"]

    conn = sqlite3.connect("disaster.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE drones
        SET drone_name=?, model=?, status=?, battery=?
        WHERE id=?
    """, (drone_name, model, status, battery, id))

    conn.commit()
    conn.close()
    return redirect("/view_drones")

@app.route("/update_rescue", methods=["POST"])
def update_rescue():

    id = request.form["id"]
    team_name = request.form["team_name"]
    leader = request.form["leader"]
    contact = request.form["contact"]
    location = request.form["location"]

    conn = sqlite3.connect("disaster.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE rescue_team
        SET team_name=?, leader=?, contact=?, location=?
        WHERE id=?
    """, (team_name, leader, contact, location, id))

    conn.commit()
    conn.close()

    return redirect("/rescue")

@app.route("/delete_rescue/<int:id>")
def delete_rescue(id):

    conn = sqlite3.connect("disaster.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM rescue_team WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return redirect("/rescue")

@app.route("/rescue")
def rescue():

    conn = sqlite3.connect("disaster.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM rescue_team")
    teams = cursor.fetchall()

    conn.close()

    return render_template("rescue.html", teams=teams)

@app.route("/add_rescue", methods=["POST"])
def add_rescue():

    team_name = request.form["team_name"]
    leader = request.form["leader"]
    contact = request.form["contact"]
    location = request.form["location"]

    conn = sqlite3.connect("disaster.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO rescue_team(team_name, leader, contact, location) VALUES(?,?,?,?)",
        (team_name, leader, contact, location)
    )

    conn.commit()
    conn.close()

    return redirect("/rescue")
@app.route("/assignment")
def assignment():

    conn = sqlite3.connect("disaster.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM drone_assignment")
    assignments = cursor.fetchall()

    conn.close()

    return render_template(
        "assignment.html",
        assignments=assignments
    )

@app.route("/add_assignment", methods=["POST"])
def add_assignment():

    drone_name = request.form["drone_name"]
    disaster_type = request.form["disaster_type"]
    location = request.form["location"]
    status = request.form["status"]

    conn = sqlite3.connect("disaster.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO drone_assignment
        (drone_name, disaster_type, location, status)
        VALUES (?, ?, ?, ?)
        """,
        (drone_name, disaster_type, location, status)
    )

    conn.commit()
    conn.close()

    return redirect("/assignment")


if __name__ == "__main__":
    app.run(debug=True)