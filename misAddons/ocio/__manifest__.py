# -*- coding: utf-8 -*-
{
    'name': "ocio",

    'summary': """
        Módulo de ejemplo para la introducción a creación de módulos
        en el SGE/ERP odoo14""",

    'description': """
        Módulo para la recogida de datos de las actividades de ocio que realizan los empleados.
    """,

    'author': "Pedro Soto",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
