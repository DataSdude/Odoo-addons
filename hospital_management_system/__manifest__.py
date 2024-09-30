{
    'name': "Hospital Management System",
    'version': '1.0',
    'depends': ['base', 'mail', 'product', 'account'],
    'author': "Ayoub Jbili",
    'category': 'Category',
    'data': [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/patients_view.xml",
        "views/patients_tag_view.xml",
        "views/appointments_view.xml",
        "views/appointments_lines_view.xml",
        "views/account_move_view.xml",
        'data/appointment_sequence.xml',  # Sequence XML file
        "views/menu.xml",
    ]
}
