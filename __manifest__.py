# -*- coding: utf-8 -*-
{
    'name': 'Pos Loyalty Fields',
    'version': '14.0.1',
    'author': 'silvau',
    'summary': 'Pos Loyalty Fields',
    'description': "Pos Loyalty Fields",
    'category': 'Point Of Sale',
    'website': 'http://zeval.com.mx',
    'depends': ['point_of_sale',
                  'pos_loyalty',
               ],
    'data': [
        'security/groups.xml',
        'views/pos_loyalty_views.xml',
    ],
    'qweb': [
        'static/src/xml/pos_loyalty_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
