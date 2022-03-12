from flask import Flask, jsonify, request
from Models import db, Consultes


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database\\salou.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Aquí comencen les rutes # 127.0.0.1_4000
@app.route("/")
def home():
    return "<h1>Welcome!</h1>"

# 127.0.0.1_4000/api/consultes
@app.route("/api/consultes", methods=["GET"])
def getConsultes():
    try:
        consultes = Consultes.query.all()
        toReturn = [consulta.serialize() for consulta in consultes]
        return jsonify(toReturn), 200 
        # for consulta in consultes:
        #     print(consulta)
    except Exception:
        exception("[SERVER]: Error")
        return jsonify({"msg: Ha ocurrido un error"}), 500


# 127.0.0.1_4000/api/consulta?numero=26
@app.route("/api/consulta", methods=["GET"])
def getNumeroConsulta():
    try:
        numeroConsulta = request.args["numero"]
        consulta = Consultes.query.filter_by(numero = numeroConsulta).first()
        if not consulta:
            return jsonify({"msg": "Aquesta consulta no te dades"}), 200
        else:
            return jsonify(consulta.serialize()), 200
    except Exception:
        exception("[SERVER]: Error")
        return jsonify({"msg: Ha ocurrido un error"}), 500

# 127.0.0.1_4000/api/buscaconsulta?
@app.route("/api/buscaconsulta", methods=["GET"])
def buscaConsulta():
    try:
        fields = {}
        if "numero" in request.args:
            fields["numero"] = request.args["numero"]
        
        if "doctor" in request.args:
            fields["doctor"] = request.args["doctor"]

        if "llista" in request.args:
            fields["llista"] = request.args["llista"]

        consulta = Consultes.query.filter_by(**fields).first()
        if not consulta:
            return jsonify({"msg": "Aquesta consulta no te dades"}), 200
        else:
            return jsonify(consulta.serialize()), 200
    
    except Exception:
        exception("[SERVER]: Error")
        return jsonify({"msg: Ha ocurrido un error"}), 500

if __name__ == "__main__":
    app.run(debug = True, port = 4000)
