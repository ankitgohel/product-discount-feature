{
    'name': 'Custom eCommerce',
    'version': '1.0',
    'summary': 'DIsplay product discounted price',
    'category': 'Sales/Sales',
    'author': 'Ankit Gohel',
    'depends': ['base', 'website_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template.xml',
        'views/website_sale_product_template.xml',
        'views/website_sale_cart.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
