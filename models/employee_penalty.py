# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class EmployeePenalty(models.Model):
    _name = 'employee.penalty'
    _description = 'EmployeePenalty'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    penalty_type_id = fields.Many2one('penalty.type', string='Penalty Type', required=True,tracking=True)
    currency_id = fields.Many2one(related='penalty_type_id.currency_id')
    amount = fields.Monetary(related='penalty_type_id.amount', string='Amount of deduction', currency_field='currency_id')
    date = fields.Date('Date', required=True)
    note = fields.Html('Note')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled'),
        ('discounted', 'Discounted')
    ], string='State', default='draft',tracking=True)


    @api.constrains('date')
    def check_date(self):
        if self.date > fields.Date.today():
            raise ValidationError(_("You can not set penalty for date in feature"))

    def action_approve(self):
        if self.state != 'draft':
            raise UserError(_('You can only approve a draft record.'))
        self.write({'state': 'approved'})

    def action_reject(self):
        if self.state != 'draft':
            raise UserError(_('You can only reject a draft record.'))
        self.write({'state': 'rejected'})

    def action_cancel(self):
        if self.state != 'approved':
            raise UserError(_('You can only cancel an approved record.'))
        self.write({'state': 'cancelled'})

    def action_discount(self):
        if self.state != 'approved':
            raise UserError(_('You can only discount an approved record.'))
        self.write({'state': 'discounted'})
