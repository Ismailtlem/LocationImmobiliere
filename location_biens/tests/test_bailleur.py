# -*- coding: utf-8 -*-
from odoo.tests import common

class TestModelA(common.TransactionCase):

    def test_country(self):
            record = self.env['lb.bailleur'].create({'nom': 'Ismail', 'email':'ismail.tlemcani@gmail.com', 'telephone':'0670272931'})
            self.assertEqual(
                record.pays_id.code,
                'MA')
