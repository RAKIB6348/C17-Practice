{
    'name': 'Hospital Management',
    'version': '17.0.1.1',
    'category': 'Healthcare',
    'summary': 'A comprehensive hospital management system.',
    'description': """
        A Hospital Management System to manage patient records, appointments, 
        doctor schedules, prescriptions, and more. The system enables hospitals 
        to efficiently handle their operations from a single platform.
    """,
    'author': 'Rakib Hasan',
    'depends': ['mail','product'],  # Example dependencies, add more as needed
    'data': [
        # security
        'security/ir.model.access.csv',
        'security/security.xml',


        # data
        'data/sequence.xml',
        'data/patient.tag.csv',


        # views
        'views/menu_views.xml',
        'views/hospital_patient_views.xml',
        'views/hospital_appointment_views.xml',
        'views/patient_tag_views.xml',
        'views/pharmacy_lines_views.xml',
    ],

    'application': True,  # Set to True if this is an application module
    'installable': True,  # Allows the module to be installed
    'auto_install': False,  # Set to True if you want it to install automatically based on dependencies
    'license': 'AGPL-3',  # You can choose a suitable license for your module
}
