# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Display Followers who are customer',
    'version': '12.0.1.0.0',
    'Author': 'SAM VISITH',
    'website': '',
    'category': 'Project',
    'summary': 'Display those followers, on project_portal_template, who are not internal users.',
    'depends': ['project'],
    'description': """
This module provides the following features:
1. to show the followers who are the customers in the task page.
2. hide internal user in the follower list. 
""",
    'data': [
        'views/project_task_view.xml',
    ],
    'installable': True,
    'application': True,
}
