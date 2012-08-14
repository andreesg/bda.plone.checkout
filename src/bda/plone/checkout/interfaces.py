from zope.interface import (
    Interface,
    Attribute,
)


class ICheckoutExtensionLayer(Interface):
    """Browser layer for bda.plone.checkout
    """


class IFieldsProvider(Interface):
    """Form fields provider for checkout.
    """
    fields_name = Attribute(u"Name of this fields provider.")
    
    def extend(form):
        """Extend form with arbitrary fields.
        """


class ICheckoutAdapter(Interface):
    """Checkout persistence adapter.
    """
    
    vessel = Attribute(u"``zope.interface.mapping.IWriteMapping providing`` "
                       u"instance.")
    
    def save(providers, widget, data):
        """Save fields specific data.
        """