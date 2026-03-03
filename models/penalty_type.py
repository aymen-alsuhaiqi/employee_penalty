# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class PenaltyType(models.Model):
    _name = 'penalty.type'
    _description = 'PenaltyType'

    name = fields.Char('Name',required=True)
    amount = fields.Float('Amount of deduction',required=True)

    _unique_name = models.Constraint('unique (name)','the name of penalty type must be unique')
