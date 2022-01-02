from django.db import models

# Create your models here.

class Carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        txt = "{0} (Duración: {1} año(s))"
        return txt.format(self.nombre, self.duracion)

class Estudiante(models.Model):
    rut =models.CharField(max_length=8, primary_key=True)
    apelllido_paterno = models.CharField(max_length=35)
    apelllido_materno = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    fecha_nacimiento = models.DateField()
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)

    def nombre_completo(self):
        txt = "{0} {1} , {2}"
        return txt.format(self.apelllido_paterno, self.apelllido_materno, self.nombres)

    def __str__(self):
        txt= "{0} / Carrera: {1} / {2}"
        if self.vigencia:
            estado_estudiante = "VIGENTE"
        else:   
            estado_estudiante = "DE BAJA"
        return txt.format(self.nombre_completo(), self.carrera, estado_estudiante)
        
class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField() 
    docente = models.CharField(max_length=100) 

    def __str__(self):
        txt = "{0} ({1}) / Docente: {2}"
        return txt.format(self.nombre, self.codigo, self.docente)       
class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fecha_matricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        txt = "{0} matriculad{1} en el curso {2} / Fecha: {3}"
        if self.estudiante.sexo == "F":
            letra_sexo = "a"
        else:
            letra_sexo = "o"
        fec_mat = self.fecha_matricula.strftime("%A %d/%m/%Y %H:%M:%S")
        return txt.format(self.estudiante.nombre_completo(), letra_sexo, self.curso, fec_mat)
