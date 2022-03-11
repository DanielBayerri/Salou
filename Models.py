from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Consultes(db.Model):
    rowid = db.Column(db.Integer, primary_key=True)
    numero_consulta = db.Column(db.Integer, nullable = False)
    nom_doctor = db.Column(db.String(100), unique = True, nullable = False)
    llista_productes = db.Column(db.String(500), nullable = True)


