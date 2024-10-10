from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    discount_percentage = fields.Float(string='Discount Percentage', default=0.0)
    discounted_price = fields.Float(string="Discounted Price", compute="get_discounted_price")

    def get_discounted_price(self):
        """
        Compute the discounted price based on the discount percentage.
        If discount_percentage is 0, return the original price.
        """
        for product in self:
            if product.discount_percentage > 0:
                product.discounted_price = product.list_price * (1 - product.discount_percentage / 100)
            else:
                product.discounted_price = product.list_price
