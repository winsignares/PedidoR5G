'''
Se necesita realizar un módulo de altas y bajas de pacientes médicos, en
donde registremos la información completa del paciente: Nombre, n° de
identificación, tipo de identificación (cédula tarjeta de identidad, pasaporte,
etc), edad, género, temperatura corporal, malestar informado por el paciente,
fecha de ingreso y eps.

identificación, temperatura corporal, malestar informado por el paciente,
fecha de ingreso y eps, asignar un médico,  tratamiento, n° de cama, diagnóstico y gravedad de
malestar, Estado

Se debe crear un formulario para las creaciones de los médicos.
Una vez registrado el paciente, en una vista o página diferente se le debe
asignar un médico, tratamiento, n° de cama, diagnóstico y gravedad de
malestar.
Teniendo los datos anteriores ya podemos realizar el alta del paciente,
debe realizarse en otra vista o página de internet, registrando los datos tales
como: fecha de salida, tratamiento realizado, temperatura corporal,
acompañante y receta médica.
'''



from flask import Flask,render_template, redirect, url_for, flash, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
'''nos conectamos a la bd '''
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/2311'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

'''pasamos la key'''
app.secret_key = "William"

'''iniciamos trabajo con la bd'''
db = SQLAlchemy(app)
ma = Marshmallow(app)

'''Iniciamos trabajo con los modelos '''
'''Modelo Paciente
Nombre, n° de
identificación, tipo de identificación (cédula tarjeta de identidad, pasaporte,
etc), edad, género '''
class Paciente(db.Model):
    __tablename__ = "Paciente"
    id = db.Column(db.Integer, primary_key=True)
    Identificacion = db.Column(db.Integer, unique=True)
    tipo_id = db.Column(db.String(30))
    Nombre = db.Column(db.String(30))
    genero = db.Column(db.String(30))
    edad = db.Column(db.Integer)

    def __init__(self, Identificacion, tipo_id, Nombre, genero, edad):
        self.Identificacion = Identificacion
        self.tipo_id  = tipo_id
        self.Nombre = Nombre
        self.genero = genero
        self.edad = edad
db.create_all()

class PacienteSchema(ma.Schema):
    class Meta:
        fields = ('id','Identificacion', 'tipo_id', 'Nombre', 'genero', 'edad')

'''Modelo Medico
Nombre, n° de
identificación, tipo de identificación (cédula tarjeta de identidad, pasaporte,
etc), edad, género, especialidad '''

class Medico(db.Model):
    __tablename__ = "Medico"
    id = db.Column(db.Integer, primary_key=True)
    Identificacion = db.Column(db.Integer, unique=True)
    tipo_id = db.Column(db.String(30))
    Nombre = db.Column(db.String(30))
    especialidad = db.Column(db.String(30))
   
    def __init__(self,Identificacion,  tipo_id, Nombre, especialidad):
        self.Identificacion = Identificacion
        self.tipo_id  = tipo_id
        self.Nombre = Nombre
        self.especialidad = especialidad

db.create_all()

class MedicoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'Identificacion', 'tipo_id', 'Nombre', 'especialidad')

'''Concepto'''
class Concepto(db.Model):
    __tablename__ = "Concepto"
    id = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(30))
   
    def __init__(self,Nombre):
       self.Nombre = Nombre

db.create_all()

class ConceptoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'Nombre')


'''Modelo Tratamiento'''
'''
identificación, temperatura corporal, malestar informado por el paciente,
fecha de ingreso y eps, asignar un médico,  tratamiento, n° de cama, diagnóstico y gravedad de
malestar, Estado -> la relación de concepto
'''
class Tratamiento(db.Model):
    __tablename__ = "Tratamiento"
    id = db.Column(db.Integer, primary_key=True)
    Id_Paciente = db.Column(db.Integer, db.ForeignKey('Paciente.id') )
    Temperatura =  db.Column(db.Integer)
    Malestar = db.Column(db.String(70))
    FechaIngreso = db.Column(db.String(70))
    Id_Medico = db.Column(db.Integer, db.ForeignKey('Medico.id') )
    Procedimiento = db.Column(db.String(70))
    N_Cama =  db.Column(db.Integer)
    Diagnostico = db.Column(db.String(70))
    Gravedad_Malestar = db.Column(db.String(70))
    Id_Concepto = db.Column(db.Integer, db.ForeignKey('Concepto.id') )
    
    Paciente =  db.relationship('Paciente', backref=db.backref('Tratamiento', lazy=True))
    Medico = db.relationship('Medico', backref=db.backref('Tratamiento', lazy=True))
    Concepto = db.relationship('Concepto', backref=db.backref('Tratamiento', lazy=True))

    def __init__(self, Id_Paciente, Temperatura,Malestar, FechaIngreso, Id_Medico, Procedimiento,N_Cama, Diagnostico, Gravedad_Malestar,  Id_Concepto ):
        self.Id_Paciente = Id_Paciente
        self.Temperatura = Temperatura
        self.Malestar =Malestar 
        self.FechaIngreso = FechaIngreso
        self.Id_Medico = Id_Medico
        self.Procedimiento= Procedimiento
        self.N_Cama = N_Cama
        self.Diagnostico=Diagnostico
        self.Gravedad_Malestar = Gravedad_Malestar
        self.Id_Concepto = Id_Concepto
        
db.create_all()

class TratamientoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'Id_Paciente', 'Temperatura', 'Malestar', 'FechaIngreso', 'Id_Medico', 'Procedimiento', 'N_Cama', 'Diagnostico','Gravedad_Malestar','Id_Concepto')

conceto_schema = ConceptoSchema()
conceptos_schema = ConceptoSchema(many=True)
paciente_schema = PacienteSchema()
pacientes_schema = PacienteSchema(many=True)
medico_schema = MedicoSchema()
medicos_schema = MedicoSchema(many=True)
tratamiento_schema = TratamientoSchema()
tratamiento_schema = TratamientoSchema(many=True)

@app.route('/Concepto', methods=['GET'])
def concepto():
    all_conceptos = Concepto.query.all()
    resultConceptos = conceptos_schema.dump(all_conceptos)
    return render_template("concepto.html", conceptos = resultConceptos)


@app.route('/addConcepto', methods=['GET','POST'])
def addConcepto():
    if request.method == "POST":
        Nombre = request.form['Nombre']
        NewConcepto = Concepto(Nombre) 
        db.session.add(NewConcepto)
        db.session.commit()
        flash('Concepto Agregado con Exito')
        return redirect(url_for('index'))

@app.route('/Alta', methods=['GET'])
def alta():
    return "Este es el modulo de Alta"

@app.route('/Pacientes', methods=['GET'])
def pacientes():
    all_pacientes = Paciente.query.all()
    resultPacientes = pacientes_schema.dump(all_pacientes)
    return render_template("paciente.html", pacientes = resultPacientes)

@app.route('/addPaciente', methods=['GET','POST'])
def addPaciente():
    if request.method == "POST":
       
        Identificacion = request.form['Identificacion']
        tipo_id = request.form['tipo_id']
        Nombre = request.form['Nombre']
        genero = request.form['genero']
        edad = request.form['edad']
        NewPaciente = Paciente(Identificacion,tipo_id,Nombre,genero,edad) 
        db.session.add(NewPaciente)
        db.session.commit()
        flash('Paciente Agregado con Exito')
        return redirect(url_for('index'))

@app.route('/Medicos', methods=['GET'])
def medicos():
    all_medicos = Medico.query.all()
    resultMedicos= medicos_schema.dump(all_medicos)
    return render_template("medico.html", medicos = resultMedicos)

@app.route('/addMedico', methods=['GET','POST'])
def addMedico():
    if request.method == "POST":
       
        Identificacion = request.form['Identificacion']
        tipo_id = request.form['tipo_id']
        Nombre = request.form['Nombre']
        especialidad = request.form['especialidad']
        NewMedico = Medico(Identificacion,tipo_id,Nombre,especialidad) 
        db.session.add(NewMedico)
        db.session.commit()
        flash('Medico Agregado con Exito')
        return redirect(url_for('index'))

@app.route('/', methods=['GET'])
def index():
    all_pacientes = Paciente.query.all()
    resultPacientes = pacientes_schema.dump(all_pacientes)
    all_medicos = Medico.query.all()
    resultMedicos= medicos_schema.dump(all_medicos)
    all_concetos = Concepto.query.all()
    resultConcepto= conceptos_schema.dump(all_concetos)
    all_tratamientos = Tratamiento.query.all()
    resultTratamiento= tratamiento_schema.dump(all_tratamientos)
    #cruce=  db.session.query(Paciente,Medico, Concepto,Tratamiento).join(Tratamiento).join(Medico)
    #cruce= db.Session.query(Paciente,Medico, Concepto,Tratamiento ).filter( Tratamiento.Id_Medico == Medico.id).filter( Tratamiento.Id_Concepto == Concepto.id ).filter( Tratamiento.Id_Paciente == Paciente.id ).all()
    #cruce= db.session.query(Tratamiento, Paciente.Nombre, Medico.Nombre, Concepto.Nombre).join(Tratamiento).join(Paciente).join(Medico).join(Concepto).all()
    #print(cruce)
    #cruce= db.session.query(Paciente, Tratamiento,Medico, Concepto).join(Paciente, Tratamiento,Medico, Concepto).all()
    #CMeTra= db.session.query(Medico, Tratamiento).join(Tratamiento).all()
    #CCoTra= db.session.query(Concepto, Tratamiento).join(Tratamiento).all()
    
    return render_template("tratamiento.html",pacientes = resultPacientes, medicos = resultMedicos, conceptos = resultConcepto, tratamientos = resultTratamiento)

@app.route('/addTratamiento', methods=['GET','POST'])
def addTratamiento():
    if request.method == "POST":
        Id_Paciente = request.form['Id_Paciente']
        Temperatura = request.form['Temperatura']
        Malestar = request.form['Malestar']
        FechaIngreso = request.form['FechaIngreso']
        Id_Medico = request.form['Id_Medico']
        Procedimiento = request.form['Procedimiento']
        N_Cama = request.form['N_Cama']
        Diagnostico = request.form['Diagnostico']
        Gravedad_Malestar = request.form['Gravedad_Malestar']
        Id_Concepto = request.form['Id_Concepto']

        NewTratamiento = Tratamiento(Id_Paciente,Temperatura,Malestar,FechaIngreso,Id_Medico,Procedimiento,N_Cama, Diagnostico, Gravedad_Malestar, Id_Concepto) 
        db.session.add(NewTratamiento)
        db.session.commit()
        flash('Tratamiento Agregado con Exito')
        return redirect(url_for('index'))


@app.route('/cambioE/<id>', methods = ['POST', 'GET'])
def cambioE(id):
     if request.method == "GET": 
        DTratamiento = Tratamiento.query.get(id)
        Estado = Concepto.query.get(DTratamiento.Id_Concepto)
        NEstado = Concepto.query.get(DTratamiento.Id_Concepto +1)
        if NEstado:
            DTratamiento.Id_Concepto = Estado.id + 1
            db.session.commit()        
            flash('Actualizado con Exito')
            return redirect(url_for('index'))
        else:
            flash('No hay mas estado')
            return redirect(url_for('index'))  
            
if __name__ == "__main__":
    app.run(debug=True)