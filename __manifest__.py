{
    'name': 'To-Do Application',
    'description': 'Manage your personal To-Do task.',
    'author': 'Santoni',
    'description': """
This module allows users to create their own notes inside Odoo
=================================================================

Use notes to write meeting minutes, organize ideas, organize personal todo
lists, etc. Each user manages his own personal Notes. Notes are available to
their authors only, but they can share notes to others users so that several
people can work on the same note in real time. It's very efficient to share
meeting minutes.

Notes can be found in the 'Home' menu.
""",
    'depends': ['base'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'security/todo_access_rules.xml',
        'views/todo_menu.xml',
        'views/todo_view.xml'
    ],
}
