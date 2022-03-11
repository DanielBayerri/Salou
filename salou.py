from flask import Flask
from Models import db, Consultes


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database\\salou.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Aquí comencen les rutes
@app.route("/")
def home():
    return "<h1>Welcome!</h1>"

@app.route("/api/consultes")
def getConsultes():
    consultes = Consultes.query.all()
    print(consultes)
    return "<h1>Success!</h1>"





if __name__ == "__main__":
    app.run(debug = True, port = 4000)
