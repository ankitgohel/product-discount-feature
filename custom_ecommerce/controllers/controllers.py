from odoo.addons.website_sale.controllers.main import WebsiteSale, Website
from odoo.http import request
from odoo import http

class WebsiteSaleExtended(WebsiteSale):

    def _get_shop_payment_values(self, order, **kwargs):
        """
        Override this method to ensure the discounted price is applied during checkout.
        """
        values = super(WebsiteSaleExtended, self)._get_shop_payment_values(order, **kwargs)
        for line in order.order_line:
            if line.product_id.discount_percentage > 0:
                line.price_unit = line.product_id.discounted_price
        return values

class WebsiteExtended(Website):

    @http.route(['/shop/cart/update_json'], type='json', auth="public", methods=['POST'], website=True, csrf=False)
    def cart_update_json(
            self, product_id, line_id=None, add_qty=None, set_qty=None, display=True):
        """
        Override the cart update route to apply custom logic (e.g., discount).
        This method updates the cart by applying the discounted price.
        """
        result = super(WebsiteExtended, self).cart_update_json(product_id, line_id, add_qty, set_qty, display)

        order = request.website.sale_get_order()
        if order:
            for line in order.order_line:
                # Apply discounted price if product has a discount percentage
                if line.product_id.discount_percentage > 0:
                    line.price_unit = line.product_id.discounted_price
                else:
                    line.price_unit = line.product_id.list_price

            # Recompute the order totals (subtotal, total, taxes)
            order._amount_all()

        return result