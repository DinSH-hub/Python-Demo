{
    'name': 'Simple Sales Demo',
    'version': '18.0.1.0.0',
    'summary': 'Save items and automatically calculate their total',
    'category': 'Productivity',
    'author': 'Learning Project',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/simple_sale_views.xml',
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
