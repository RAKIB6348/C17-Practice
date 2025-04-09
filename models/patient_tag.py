from odoo import api, fields, models


class PatientTag(models.Model):
    _name = 'patient.tag'
    _description = 'Patient Tag'
    _order = 'sequence, id'

    name = fields.Char(string='Tag')
    color = fields.Integer(string='Color')
    sequence = fields.Integer(string='Sequence', default=1)
