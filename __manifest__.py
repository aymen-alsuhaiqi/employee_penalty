# -*- coding: utf-8 -*-
{
    'name': 'Employee_penalty',
    'version': '',
    'summary': """ Employee_penalty Summary """,
    'author': 'AMT',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/penalty_type_views.xml',
    ],
    
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
