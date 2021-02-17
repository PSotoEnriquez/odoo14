# -*- coding: utf-8 -*-

from odoo import models, fields, api

tipos_playa = [
    ('1', 'Arena fina'),
    ('2', 'Arena gruesa'),
    ('3', 'Cantos rodados'),
    ('4', 'Arena negra (polvo)'),
]


class Municipio(models.Model):
    _name = 'ocio.municipio'
    _description = 'Este modelo almacenará informacion de las municipios de Cádiz'

    nombre = fields.Char(string='Nombre municipio', size=50, required=True)
    habitantes = fields.Integer(string='Nº Habitantes')
    cod_prov = fields.Integer(string='Codigo provincia')
    cod_mun = fields.Integer(string='Codigo municipio')
    cod_postal = fields.Integer(string='Codigo postal')
    playas = fields.One2many("ocio.playa", "poblacion", string="Playas")
    # campo calculado
    n_playas = fields.Integer(string='Nº total playas', compute="calculaplayas", store=True)

    @api.depends('playas')
    def calculaplayas(self):
        for municipio in self:
            municipio.n_playas = len(self.playas)


class Playa(models.Model):
    _name = 'ocio.playa'
    _description = 'Este modelo almacenará informacion de las playas de Cádiz'

    nombre = fields.Char(string='Nombre playa')
    composicion = fields.Selection(tipos_playa, string='Composición terreno')
    anchura = fields.Char(string='Anchura playa')
    interes = fields.Char(string='Interés')
    nudista = fields.Boolean(string='¿Es nudista?')
    poblacion = fields.Many2one('ocio.municipio', string='Poblacion', required=True, ondelete="cascade")
    # si borramos un pueblo se borran todas las playas.


class Convivencia(models.Model):
    _name = 'ocio.convivencia'
    _description = 'Este modelo almacenará informacion de las convivencias de los empleados.'

    nombre = fields.Char(string='Nombre convivencia')
    empleados = fields.Many2many('hr.employee', string='Employee', index=True)
    playa = fields.Many2one('ocio.playa', string="Playa")
    precio_persona = fields.Float(string='Precio')

