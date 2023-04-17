import db
from sqlalchemy import Column, Integer, String, Time, Boolean

# CLASE
# Creación de la clase que organiza la información y que luego importará en 
# tabla a la DB, gracias a los modulos de sqlalchemy

class Tarea(db.Base):
    # Tabla + columnas
    __tablename__ = "tarea"
    id_tarea = Column(Integer,primary_key=True)
    contenido_tarea = Column(String(300),nullable=False)
    categoria = Column(String(100),nullable=False)
    hora = Column(String(100),nullable=False)
    fecha_limite = Column(String(100),nullable=False)
    tarea_hecha = Column(Boolean)

    # Filas tabla
    def __init__(self,
                 contenido_tarea,
                 categoria,
                 hora,
                 fecha_limite,
                 tarea_hecha):
        self.contenido_tarea = contenido_tarea
        self.tarea_hecha = tarea_hecha
        self.hora = hora
        self.fecha_limite = fecha_limite
        self.categoria = categoria
    
    def __str__(self):
        return """
        --TAREA--
        id: {}
        contenido: {}
        categoria: {}
        hora: {}
        fecha_limite: {}
        hecha: {}""".format(self.id_tarea,
                            self.contenido_tarea,
                            self.categoria,
                            self.hora,
                            self.fecha_limite,
                            self.tarea_hecha)