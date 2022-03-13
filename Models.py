from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Consultes(db.Model):
    rowid = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, unique = True, nullable = False)
    doctor = db.Column(db.String(100), unique = True, nullable = False)
    llista = db.Column(db.String(500), nullable = True)

    def __init__(self, numero, doctor, llista):
        super().__init__()
        self.numero = numero
        self.doctor = doctor
        self.llista = llista

    def __str__(self):
        return "Consulta: {}. Doctor: {}. Material: {}".format(
            self.numero, 
            self.doctor, 
            self.llista
            )
    
    # Ho passem a diccionari perqué sigui interpretable per JSON
    def serialize(self):
        return {
            "rowid": self.rowid,
            "numero": self.numero,
            "doctor": self.doctor,
            "llista": self.llista
        }
