# -*- coding: utf-8 -*-
##############################################################################
#
#    Kinesis Athletics
#    Copyright (C) 2014 Ingenieria Adhoc
#    No email
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


import re
from openerp import netsvc
from openerp.osv import osv, fields

class company_type(osv.osv):
    """"""
    
    _name = 'kinesis_athletics.company_type'
    _description = 'company_type'

    _columns = {
        'name': fields.char(string='name', required=True),
        'is_school': fields.boolean(string='Is school'),
        'company_id': fields.one2many('res.company', 'company_type_id', string='company_id'), 
    }

    _defaults = {
    }


    _constraints = [
    ]




company_type()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
