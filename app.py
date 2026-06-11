from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
<<<<<<< HEAD
    return "Hello Raj SINGH this is CI/CD Pipeline Project Version 2"
=======
    return "Hello Raj Singh This is CI/CD Pipeline Project Version 2"
>>>>>>> 707eebe (Update GitHub actions versions)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
