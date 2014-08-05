from django.db import models

RACES_LIST = (
        ('ALL', 'GENERAL' ),
        ('GC', 'GUERREROS DEL CAOS'),
        ('OG', 'ORCOS Y GOBLINS'),
        ('E', 'ENANOS'),
        ('AE', 'ALTOS ELFOS'),
        ('EO', 'ELFOS OSCUROS'),
        ('ES', 'ELFOS SILVANOS'),
        ('RO', 'REINOS OGROS'),
        ('CV', 'CONDES VAMPIRO'),
        ('RF', 'REYES FUNERARIOS'),
        ('HL', 'HOMBRES LAGARTO'),
        ('S', 'SKAVENS'),
        ('B', 'BRETONIA'),
        ('EI', 'EL IMPERIO'),
        ('HB', 'HOMBRES BESTIA'),
        ('DC', 'DEMONIOS DEL CAOS')
)

UNITY_TYPE = (
    ('CO', 'Comandante'),
    ('HE', 'heroe'),
    ('B', 'Básica'),
    ('NB', 'No básica'),
    ('E', 'Especial'),
    ('S', 'Singular')
)

TROOP_TYPE = (
    ('I', 'Infantería'),
    ('IP', 'Infantería (Personaje especial)'),
    ('IM', 'Infantería Monstruosa'),
    ('IMP', 'Infantería Monstruosa (Personaje especial)'),
    ('C', 'Caballería'),
    ('CP', 'Caballería (Personaje especial)'),
    ('CM', 'Caballería Monstruosa'),
    ('CMP', 'Caballería Monstruosa (Personaje especial)'),
)

MONTURA_TYPE = (
    ('BM', 'Bestia Monstruosa'),
)

SABERES = (
    ('F', 'Fuego'),
    ('B', 'Bestias')
)

class Equipment(models.Model):
    name = models.CharField('Nombre', max_length=200)
    description = models.TextField('Descripción', blank=True)
    short_description = models.TextField('Descripción corta', blank=True)
    race = models.CharField('Raza', max_length=3, choices=RACES_LIST)
    puntos = models.IntegerField('Puntos', blank=True, default=0)

    class Meta:
        verbose_name = 'Equipo'


class Regla(models.Model):
    name = models.CharField('Regla', max_length=100)
    description = models.TextField('Descripción', blank=True)
    short_description = models.TextField('Descripción corta', blank=True)
    race = models.CharField('Raza', max_length=3, choices=RACES_LIST)

    class Meta:
        verbose_name = 'Regla'
        verbose_name_plural = 'Reglas'

    def __unicode__(self):
        return u"%s" % self.name


class Arma(Equipment):

    class Meta:
        verbose_name = 'Arma'
        verbose_name_plural = 'Armas'

    def __unicode__(self):
        return u"%s" % self.name

    '''
    def reglas_arma(self):
        return ', '.join([a.name for a in self.reglas_especiales.all()])
    '''



class ArmaMagica(Equipment):
    class Meta:
        verbose_name = 'Arma Mágica'
        verbose_name_plural = 'Armas Mágicas'


class Armadura(Equipment):
    class Meta:
        verbose_name = 'Armadura'
        verbose_name_plural = 'Armaduras'


class ArmaduraMagicas(Equipment):
    class Meta:
        verbose_name = 'Armadura Mágica'
        verbose_name_plural = 'Armaduras Mágicas'


class Talisman(Equipment):
    class Meta:
        verbose_name = 'Talisman'
        verbose_name_plural = 'Talismanes'


class EstandarteMagico(Equipment):
    class Meta:
        verbose_name = 'Estandarte Mágico'
        verbose_name_plural = 'Estandartes Mágicos'


class ObjetoArcano(Equipment):
    class Meta:
        verbose_name = 'Objeto Arcano'
        verbose_name_plural = 'Objetos Arcanos'


class ObjetoHechizado(Equipment):
    class Meta:
        verbose_name = 'Objeto Hechizado'
        verbose_name_plural = 'Objetos Hechizados'

'''
class Tropa(models.Model):
    name = models.CharField('Nombre', max_length=200)
    puntos = models.IntegerField('Puntos', blank=True, default=0)
    num_tropa = models.IntegerField(blank=True)
    tipo_tropa = models.CharField('Tipo de tropa', max_length='3', choices=TROOP_TYPE)
    race = models.CharField('Raza', max_length=3, choices=RACES_LIST)
    reglas = models.ManyToManyField(Regla)

    class Meta:
        verbose_name = 'Tropa'
        verbose_name_plural = 'Tropas'


class Montura(models.Model):
    name = models.CharField('Nombre', max_length=200)
    puntos = models.IntegerField('Puntos', blank=True, default=0)
    tipo_montura = models.CharField('Tipo de montura', max_length='3', choices=MONTURA_TYPE)
    race = models.CharField('Raza', max_length=3, choices=RACES_LIST)
    reglas = models.ManyToManyField(Regla)

    class Meta:
        verbose_name = 'Montura'
        verbose_name_plural = 'Monturas'


class Hechizo(models.Model):
    name = models.CharField('Nombre', max_length=200)
    description = models.TextField('Descripción', blank=True)
    dificultad = models.CharField('Dificultad', max_length=200)
    race = models.CharField('Raza', max_length=3, choices=RACES_LIST)
    # tipo_saber = models.CharField('Saber', max_length=200, choices=SABERES)

    class Meta:
        verbose_name = 'Hechizo'
        verbose_name_plural = 'Hechizos'

    def __unicode__(self):
       return self.name

class Saber(models.Model):
    name = models.CharField('Nombre', max_length=200, choices=SABERES)
    regla_saber = models.TextField('Regla del saber', blank=True)
    hechizos = models.ManyToManyField(Hechizo)
    race = models.CharField('Raza', max_length=3, choices=RACES_LIST)

    class Meta:
        verbose_name = 'Saber'
        verbose_name_plural = 'Saberes'

    def get_hechizos(self):
        return ', '.join([a.name for a in self.hechizos.all()])


class Magia(models.Model):
    saber = models.ManyToManyField(Saber)
    nivel = models.IntegerField('Nivel', blank=True, default=0)
    puntos = models.IntegerField('Puntos', blank=True, default=0)

    class Meta:
        verbose_name = 'Magia'
        verbose_name_plural = 'Magias'


class Unidad(models.Model):
    name = models.CharField('Nombre', max_length=200)
    description = models.TextField('Descripción', blank=True)
    short_description = models.TextField('Descripción corta', blank=True)
    tipo = models.CharField('Tipo de unidad', max_length='2', choices=UNITY_TYPE)
    tropa = models.OneToOneField(Tropa)
    montura = models.OneToOneField(Montura)
    magia = models.OneToOneField(Magia)

    class Meta:
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'
'''