from odoo import models, api, fields


class Appointment(models.Model):
    _name = "appointment"
    _inherit = ["mail.thread"]
    _description = "Appointment"
    _rec_name = "appointment_number"
    _rec_names_search = ["appointment_number", "patient_id", "state"]

    appointment_number = fields.Char(string="Appointment Reference", readonly=True, copy=False, index=True,
                                     default=lambda self: ('New'))
    patient_id = fields.Many2one('patient', string="Patient", required=True, onDelete='restrict')
    date = fields.Datetime(string="Date and Time", required=True, tracking=True)
    note = fields.Text(string="Note")
    appointment_line_ids = fields.One2many(
        'appointment.line',
        'appointment_number', string='Lines')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('canceled', 'Canceled')
    ], string="Status", required=True, readonly=True, copy=False, tracking=True, default='draft')
    total_quantity = fields.Float(compute="_compute_total_quantity" ,string='Total Quantity')

    @api.model
    def create(self, vals):
        if vals.get('appointment_number', 'New') == 'New':
            '''
                If the key is not present in the dictionary, 
                the get method returns a default value specified as the second argument.
            '''
            vals['appointment_number'] = self.env['ir.sequence'].next_by_code('appointment.sequence') or 'New'
        return super(Appointment, self).create(vals)

        # Action Method to Confirm the Appointment

    def action_confirm(self):
        for record in self:
            if record.state == 'draft':
                record.state = 'confirmed'

        # Action Method to Mark the Appointment as Done

    def action_done(self):
        for record in self:
            if record.state == 'confirmed':
                record.state = 'done'

        # Action Method to Reset the Appointment to Draft

    def action_draft(self):
        for record in self:
            if record.state in ['confirmed']:
                record.state = 'draft'

    def action_cancel(self):
        for record in self:
            if record.state in ['confirmed', 'draft']:
                record.state = 'canceled'

    def _compute_display_name(self):
        """Compute the value of the `display_name` field.

                The `display_name` field is a textual representation of the record.
                This method can be overridden to change the representation.  If needed,
                it can be made field-dependent using :attr:`~odoo.api.depends` and
                context-dependent using :attr:`~odoo.api.depends_context`.
                """
        for rec in self:
            rec.display_name = f"[{rec.appointment_number}] {rec.patient_id.name}"

    def _compute_total_quantity(self):
        for rec in self:
            rec.total_quantity = 0
            for line in rec.appointment_line_ids:
                rec.total_quantity += line.quantity

class AppointmentLine(models.Model):
    _name = 'appointment.line'
    _description = 'Appointment Lines'

    appointment_number = fields.Many2one('appointment', string='Appointment')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    quantity = fields.Float(string='Quantity')
