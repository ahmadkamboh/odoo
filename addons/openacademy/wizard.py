# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'openacademy.wizard'

    def _default_sessions(self):
        return self.env['openacademy.session'].browse(self._context.get('active_ids'))

    session_ids = fields.Many2many('openacademy.session',
                                   string="Sessions", required=True, default=_default_sessions)

    session_id = fields.Many2one('openacademy.session',
        string="Session", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    @api.multi
    def subscribe(self):
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids
       # self.session_id.attendee_ids |= self.attendee_ids
        return {}