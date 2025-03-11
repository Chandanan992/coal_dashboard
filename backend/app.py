from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_bcrypt import Bcrypt
import mysql.connector

app = Flask(__name__)
CORS(app)  # Allow frontend to access API
bcrypt = Bcrypt(app)

app.config["JWT_SECRET_KEY"] = "super_secret_key"  # Change this for security
jwt = JWTManager(app)

# Database Connection
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="coal_db"
)
cursor = db.cursor()

# ✅ Home Route (To Test If Flask Is Running)
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Backend is running!"})

# ✅ User Signup
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        db.commit()
        return jsonify({"message": "User registered successfully!"}), 201
    except mysql.connector.IntegrityError:
        return jsonify({"error": "Username already exists"}), 400

# ✅ User Login
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()

    if user and bcrypt.check_password_hash(user[0], password):
        access_token = create_access_token(identity=username)
        return jsonify({"message": "Login successful", "token": access_token}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401

# ✅ Fetch Coal Data (Only Logged-In Users)
@app.route("/coal-data", methods=["GET"])
@jwt_required()
def get_coal_data():
    cursor.execute("SELECT * FROM coal_data")
    rows = cursor.fetchall()

    data = []
    for row in rows:
        data.append({
            "id": row[0],
            "name": row[1],
            "quantity": row[2],
            "location": row[3]
        })

    return jsonify(data)

# ✅ Add New Coal Data (Only Logged-In Users)
@app.route("/add-coal", methods=["POST"])
@jwt_required()
def add_coal():
    data = request.json
    name = data.get("name")
    quantity = data.get("quantity")
    location = data.get("location")

    if not name or not quantity or not location:
        return jsonify({"error": "All fields are required"}), 400

    cursor.execute("INSERT INTO coal_data (name, quantity, location) VALUES (%s, %s, %s)", (name, quantity, location))
    db.commit()
    
    return jsonify({"message": "Coal data added successfully!"}), 201

# ✅ Run Flask
if __name__ == "__main__":
    app.run(debug=True)
