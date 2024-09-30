from datetime import date, datetime

from dateutil.relativedelta import relativedelta

from odoo import models, api, fields, _
from odoo.exceptions import UserError

class Patient(models.Model):
    _name = "patient"
    _inherit = ["mail.thread"]
    _description = "Patient.Master"

    name = fields.Char(string="Name", required=True, tracking=True)
    date_of_birth = fields.Date(string="DOB", tracking=True)
    gender = fields.Selection([("male", "Male"), ("female", "Female")], string="Gender", tracking=True)
    tag_ids = fields.Many2many("patient_tag", "patient_tag_rel", "tag_id", string="Tags")
    is_minor = fields.Boolean('Minor',compute="_compute_age", store=True)
    guardian = fields.Char(string="Guardian")

    @api.ondelete(at_uninstall=False)
    def _check_patient_appointment(self):
        for rec in self:
            domain = [('patient_id', '=', rec.id)]
            appointments = self.env['appointment'].search(domain)
            if appointments:
                raise UserError(_("You cannot delete a patient with existing appointments already linked with"))

    @api.depends('date_of_birth')
    def _compute_age(self):
        today = date.today()
        for record in self:
            if record.date_of_birth:
                age_difference = relativedelta(today, record.date_of_birth)
                print(int(age_difference.years))
                record.is_minor = int(age_difference.years) < 18
