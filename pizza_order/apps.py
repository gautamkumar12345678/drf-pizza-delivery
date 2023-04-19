from django.apps import AppConfig


class PizzaOrderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pizza_order'

    def ready(self):
        import pizza_order.signals
