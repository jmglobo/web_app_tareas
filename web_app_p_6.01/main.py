# SERVIDOR WEB FLASK
from flask import Flask, render_template, redirect, url_for, request
from models import Tarea
from datetime import datetime, date, time
import db

# Creación del servidor web
app = Flask(__name__)


# Ruta raiz del servidor web
@ app.route("/")
def home():
    todas_las_tareas = db.session.query(Tarea).all()
    return render_template("index.html",
                           lista_tareas = todas_las_tareas)


# Ruta para creación de la tarea
@app.route("/crear-tarea", methods=["POST"])
def crear():
    date = datetime.now()
    tarea = Tarea(contenido_tarea=request.form["contenido_tarea"], 
                  categoria = request.form["categoria"],
                  fecha_limite=request.form["fecha_limite"],
                  hora= ("{:02d}:{:02d}:{:02d} - {:02d}/{:02d}/{} ".format(date.hour,
                                                                            date.minute,
                                                                            date.second,
                                                                            date.day,
                                                                            date.month,
                                                                            date.year)),
                    tarea_hecha=False)
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for("home"))


# Ruta para edición de la tarea
@app.route("/editar-tarea/<id>", methods=["POST"])
def editar(id):
    date = datetime.now()
    tarea = db.session.query(Tarea).filter_by(id_tarea=id).first()
    tarea.contenido_tarea=request.form["nuevo_contenido_tarea"] 
    tarea.categoria = request.form["nueva_categoria"]
    tarea.fecha_limite=request.form["nueva_fecha_limite"]
    tarea.hora= ("{}:{}:{} - {}/{}/{} ".format(date.hour,
                                                date.minute,
                                                date.second,
                                                date.day,
                                                date.month,
                                                date.year))
    tarea.tarea_hecha=False
    db.session.commit()
    return redirect(url_for("home"))


# Ruta para dar la tarea hecha
@app.route("/tarea-hecha/<id>")
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id_tarea=id).first()
    tarea.tarea_hecha = not(tarea.tarea_hecha)
    db.session.commit()
    return redirect(url_for("home"))


# Ruta para eliminación de la tarea
@app.route("/eliminar-tarea/<id>")
def eliminar(id):
    tarea = db.session.query(Tarea).filter_by(id_tarea=id).delete()
    db.session.commit()
    return redirect(url_for("home"))








# Puesta en servicio del servidor web + conexión a la DB
if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)

