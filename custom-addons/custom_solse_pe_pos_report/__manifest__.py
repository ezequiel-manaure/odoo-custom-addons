{
   'name':'Personalizacion para el Ticket',
   'version':'17.0.1.0.0',
   'author':'Ezequiel Manaure',
   'license': 'LGPL-3',
   'depends':['point_of_sale', 'solse_pe_pos_report', 'solse_pe_cpe', 'solse_pe_cpe_pos', 'solse_pe_cpe_pdf'],
   'assets': {
    'point_of_sale._assets_pos': [
        'custom_solse_pe_pos_report/static/src/xml/custom_ticket.xml',
        'custom_solse_pe_pos_report/static/src/js/custom_orderline.js',
    ],
   },
   'installable': True,
   'application': False,
}

