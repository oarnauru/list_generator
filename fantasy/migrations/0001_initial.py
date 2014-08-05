# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Equipment'
        db.create_table('fantasy_equipment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('short_description', self.gf('django.db.models.fields.TextField')()),
            ('race', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('puntos', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('fantasy', ['Equipment'])

        # Adding model 'Regla'
        db.create_table('fantasy_regla', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('short_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('race', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('fantasy', ['Regla'])

        # Adding model 'Arma'
        db.create_table('fantasy_arma', (
            ('equipment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fantasy.Equipment'], primary_key=True, unique=True)),
            ('alcance', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('fuerza', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('fantasy', ['Arma'])

        # Adding M2M table for field reglas_especiales on 'Arma'
        m2m_table_name = db.shorten_name('fantasy_arma_reglas_especiales')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('arma', models.ForeignKey(orm['fantasy.arma'], null=False)),
            ('regla', models.ForeignKey(orm['fantasy.regla'], null=False))
        ))
        db.create_unique(m2m_table_name, ['arma_id', 'regla_id'])

        # Adding model 'ArmaMagica'
        db.create_table('fantasy_armamagica', (
            ('equipment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fantasy.Equipment'], primary_key=True, unique=True)),
        ))
        db.send_create_signal('fantasy', ['ArmaMagica'])

        # Adding model 'Armadura'
        db.create_table('fantasy_armadura', (
            ('equipment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fantasy.Equipment'], primary_key=True, unique=True)),
        ))
        db.send_create_signal('fantasy', ['Armadura'])

        # Adding model 'ArmaduraMagicas'
        db.create_table('fantasy_armaduramagicas', (
            ('equipment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fantasy.Equipment'], primary_key=True, unique=True)),
        ))
        db.send_create_signal('fantasy', ['ArmaduraMagicas'])

        # Adding model 'Talisman'
        db.create_table('fantasy_talisman', (
            ('equipment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fantasy.Equipment'], primary_key=True, unique=True)),
        ))
        db.send_create_signal('fantasy', ['Talisman'])

        # Adding model 'EstandarteMagico'
        db.create_table('fantasy_estandartemagico', (
            ('equipment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fantasy.Equipment'], primary_key=True, unique=True)),
        ))
        db.send_create_signal('fantasy', ['EstandarteMagico'])

        # Adding model 'ObjetoArcano'
        db.create_table('fantasy_objetoarcano', (
            ('equipment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fantasy.Equipment'], primary_key=True, unique=True)),
        ))
        db.send_create_signal('fantasy', ['ObjetoArcano'])

        # Adding model 'ObjetoHechizado'
        db.create_table('fantasy_objetohechizado', (
            ('equipment_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['fantasy.Equipment'], primary_key=True, unique=True)),
        ))
        db.send_create_signal('fantasy', ['ObjetoHechizado'])


    def backwards(self, orm):
        # Deleting model 'Equipment'
        db.delete_table('fantasy_equipment')

        # Deleting model 'Regla'
        db.delete_table('fantasy_regla')

        # Deleting model 'Arma'
        db.delete_table('fantasy_arma')

        # Removing M2M table for field reglas_especiales on 'Arma'
        db.delete_table(db.shorten_name('fantasy_arma_reglas_especiales'))

        # Deleting model 'ArmaMagica'
        db.delete_table('fantasy_armamagica')

        # Deleting model 'Armadura'
        db.delete_table('fantasy_armadura')

        # Deleting model 'ArmaduraMagicas'
        db.delete_table('fantasy_armaduramagicas')

        # Deleting model 'Talisman'
        db.delete_table('fantasy_talisman')

        # Deleting model 'EstandarteMagico'
        db.delete_table('fantasy_estandartemagico')

        # Deleting model 'ObjetoArcano'
        db.delete_table('fantasy_objetoarcano')

        # Deleting model 'ObjetoHechizado'
        db.delete_table('fantasy_objetohechizado')


    models = {
        'fantasy.arma': {
            'Meta': {'object_name': 'Arma', '_ormbases': ['fantasy.Equipment']},
            'alcance': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'equipment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fantasy.Equipment']", 'primary_key': 'True', 'unique': 'True'}),
            'fuerza': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'reglas_especiales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['fantasy.Regla']", 'symmetrical': 'False'})
        },
        'fantasy.armadura': {
            'Meta': {'object_name': 'Armadura', '_ormbases': ['fantasy.Equipment']},
            'equipment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fantasy.Equipment']", 'primary_key': 'True', 'unique': 'True'})
        },
        'fantasy.armaduramagicas': {
            'Meta': {'object_name': 'ArmaduraMagicas', '_ormbases': ['fantasy.Equipment']},
            'equipment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fantasy.Equipment']", 'primary_key': 'True', 'unique': 'True'})
        },
        'fantasy.armamagica': {
            'Meta': {'object_name': 'ArmaMagica', '_ormbases': ['fantasy.Equipment']},
            'equipment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fantasy.Equipment']", 'primary_key': 'True', 'unique': 'True'})
        },
        'fantasy.equipment': {
            'Meta': {'object_name': 'Equipment'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'puntos': ('django.db.models.fields.IntegerField', [], {}),
            'race': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'short_description': ('django.db.models.fields.TextField', [], {})
        },
        'fantasy.estandartemagico': {
            'Meta': {'object_name': 'EstandarteMagico', '_ormbases': ['fantasy.Equipment']},
            'equipment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fantasy.Equipment']", 'primary_key': 'True', 'unique': 'True'})
        },
        'fantasy.objetoarcano': {
            'Meta': {'object_name': 'ObjetoArcano', '_ormbases': ['fantasy.Equipment']},
            'equipment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fantasy.Equipment']", 'primary_key': 'True', 'unique': 'True'})
        },
        'fantasy.objetohechizado': {
            'Meta': {'object_name': 'ObjetoHechizado', '_ormbases': ['fantasy.Equipment']},
            'equipment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fantasy.Equipment']", 'primary_key': 'True', 'unique': 'True'})
        },
        'fantasy.regla': {
            'Meta': {'object_name': 'Regla'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'race': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'short_description': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'fantasy.talisman': {
            'Meta': {'object_name': 'Talisman', '_ormbases': ['fantasy.Equipment']},
            'equipment_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['fantasy.Equipment']", 'primary_key': 'True', 'unique': 'True'})
        }
    }

    complete_apps = ['fantasy']