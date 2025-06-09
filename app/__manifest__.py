# __manifest__.py

{
    "name": "Kateb Database Replication",
    "version": "1.0.0",
    "summary": "Module to manage database replication within Odoo instances.",
    "description": """
Database Replication Module
===========================

This module provides tools to configure and manage database replication setups across Odoo environments.
It is designed for advanced users and system administrators needing better control over their Odoo deployments.
    """,
    "author": "Fateh Lebbier",
    "website": "https://katebworks.com",
    "category": "Tools",
    "depends": ["base"],
    "data": [
        # "views/replication_settings_view.xml",
        # "security/ir.model.access.csv"
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
