from flask import Flask, request, jsonify
import smtplib
import os

app = Flask(__name__)

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "senses10k@gmail.com"
EMAIL_PASSWORD = "xaqc xxkr wulh lbro" 

@app.route("/signup", methods=["POST"])
def signup():
    data = request.json  # Expecting JSON input
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    # Email Content
    subject = "New Beta Sign-Up"
    body = f"Name: {name}\nEmail: {email}"
    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, "horizonautomationtools@gmail.com", message)
        
        return jsonify({"success": "Email sent"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
