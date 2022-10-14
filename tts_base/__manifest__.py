{
    'name': 'TTS - Trust Transport Services',
    'category': 'TTS/Base',
    'sequence': 1,
    'author': 'Mai Thành Duy An',
    'summary': 'Trust Transport Services',
    'version': '1.0',
    'description': 'TTS - Trust Transport Services',
    'installable': True,
    'application': True,
    'auto_install': False,
    'depends': ['base', 'contacts'],
    'data': [
        'views/tts_base_view.xml',
        'views/tts_base_menu.xml',
        'security/ir.model.access.csv',
    ],
    'license': 'LGPL-3',
}
