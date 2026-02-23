# -*- coding: utf-8 -*-
{
    'name': 'Food Waste to Food Plate',
    'summary': 'Corporate leftover food redistribution',
    'version': '19.0.0.1',
    'category': 'Operations',
    'author': 'Workshop',
    'license': 'LGPL-3',
    'website': 'https://example.com',
    'depends': [
        'base',
        'mail',
        'sale',          # Sales (stats + SO flow)
        'product',
        'website_sale',  # e-commerce / website products @ step 1
        'stock',         # Inventory link @ step 2
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/menu.xml',
        'views/food_batch_views.xml',
        'views/receiver_views.xml',
        'views/pickup_views.xml',
        'views/impact_views.xml',
        'views/dashboards.xml',

        # --- NEW files (add these below) ---
        'views/product_template_views.xml',
        'views/website_product_views.xml',
        # optional: auto-confirm $0 orders (Sales stats update immediately)
        'data/cron_free_orders.xml',
    ],
    'application': True,
}
