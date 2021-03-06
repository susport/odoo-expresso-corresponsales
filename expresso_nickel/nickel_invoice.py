# -*- coding: utf-8 -*-

from openerp import models, fields


class nickel_invoice(models.Model):
    # Cliente obtenido desde la base de datos de Nickel
    _name = 'nickel_invoice'
    _description = 'Nickel Invoice'
    _order = 'expiration_date asc'

    remote_id = fields.Char(
        'Identificador Remoto',
        size=30,
        readonly=True)

    customer_code = fields.Char(
        'Client Code',
        size=50,
        readonly=True)
    partner_id = fields.Many2one(
        'res.partner',
        'Client')
    invoice_number = fields.Char(
        'Invoice Number',
        size=50,
        readonly=True)
    invoice_id = fields.Many2one(
        'account.invoice',
        'Invoice')
    serie = fields.Char(
        'Serie',
        size=50,
        readonly=True)
    invoice_date = fields.Date(
        'Invoice Date')
    expiration_date = fields.Date(
        'Expiration Date')
    amount = fields.Float(
        'Amount')
    code_currency = fields.Char(
        'Code Currency',
        size=10,
        readonly=True)

    paid = fields.Boolean(
        'Paid', default=False)

    def copy(self, cr, uid, id, default=None, context=None):
        if default is None:
            default = {}
        default['remote_id'] = None
        return super(nickel_invoice, self).copy(cr, uid, id, default, context)

    def get_invoice_asociados(self, cr, uid, ids, context=None):
        invoice_ids = []
        for nickel_invoice in self.browse(cr, uid, ids, context=context):
            if nickel_invoice.invoice_id:
                invoice_ids.append(nickel_invoice.invoice_id.id)
        return invoice_ids

    _sql_constraints = [
        ('remote_id_no_uniq', 'unique(remote_id)', 'The remote ID must be unique!')]
