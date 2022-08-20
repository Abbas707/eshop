from django.db.models import QuerySet


class OrderManager(QuerySet):
    """ Order model object's manager  """

    def get_orders_by_customer(self, user_id):
      # Pull all the orders of a user
      return self.filter(user=user_id)

    def get_orders_by_store(self, store_id):
      # Pull all the orders of a store
      return self.filter(store=store_id)
