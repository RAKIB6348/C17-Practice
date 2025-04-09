from odoo import api, fields, models, _
from odoo.fields import date
from odoo.fields import datetime


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'patient_id'
    _rec_names_search = ['name', 'patient_id']

    patient_id = fields.Many2one('hospital.patient', string='Patient', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'female'),
    ], string='Gender', related='patient_id.gender')
    appointment_date = fields.Date(string='Appointment Date', default=date.today(), tracking=True)
    booking_datetime = fields.Datetime(string='Appointment Date', default=datetime.now(), tracking=True)
    state = fields.Selection([
            ('draft', 'Draft'),
            ('progress', 'In Porgress'),
            ('confirm', 'Confirmed'),
            ('cancel', 'Cancelled')
        ],
        string="Status",
        store=True, readonly=True,
        index=True,
        copy=False,
        default='draft',
        tracking=True
    )


    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_progress(self):
        for rec in self:
            rec.state = 'progress'

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'


    name = fields.Char(
        string="Appointment ID",
        required=True, copy=False, readonly=True,
        index='trigram',
        default=lambda self: _('New'))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _("New")) == _("New"):
                vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _("New")

        return super(HospitalAppointment, self).create(vals_list)

    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.name} - {rec.patient_id.name}"





class PharmacyLines(models.Model):
    _name = 'pharmacy.lines'
    _description = 'Pharmacy Lines'


    product = fields.Many2one('product.product', string='Product')
    qty = fields.Integer(string='Quantity')
    price = fields.Float(string='Price')
    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')
    total_price = fields.Float(string='Total Price', compute='compute_total_price')


    @api.depends('qty','price')
    def compute_total_price(self):
        for rec in self:
            rec.total_price = rec.qty * rec.price