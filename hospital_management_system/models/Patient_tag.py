from odoo import models, api, fields
class PatientTag(models.Model):
    _name = "patient_tag"
    _description = "Patient Tag"
    _order = "sequence,id"

    name = fields.Char(string="Name", required=True, tracking=True)
    sequence = fields.Integer(default=10)