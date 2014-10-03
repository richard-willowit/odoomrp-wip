
# -*- encoding: utf-8 -*-
##############################################################################
#
#    Daniel Campos (danielcampos@avanzosc.es) Date: 02/10/2014
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    "name": "MRP BOM component massive change",
    "version": "1.0",
    "description": """
    This module allows change massively one component for another on a list of
    BOMs.
    """,
    'author': 'OdooMRP team',
    'website': "http://www.odoomrp.com",
    "depends": ['mrp'],
    "category": "Manufacturing",
    "data": ['views/mrp_bom_change_view.xml',
             'security/ir.model.access.csv'
             ],
    "installable": True
}
