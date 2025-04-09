from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    image = fields.Binary(string='Image')
    name = fields.Char(string='Name', tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([
        ('male','Male'),
        ('female','female'),
    ], string='Gender', tracking=True)
    tag_ids = fields.Many2many('patient.tag', string='Tag')

    @api.constrains('age')
    def _check_age_value(self):
        for rec in self:
            if rec.age == 0:
                raise ValidationError(_('Age Must Be Greater Than Zero!!!!!'))