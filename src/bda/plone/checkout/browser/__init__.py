#!/usr/bin/env python
# -*- coding: utf-8 -*
from Products.Five import BrowserView
from bda.plone.shop.utils import is_ticket as is_context_ticket
from plone.app.uuid.utils import uuidToCatalogBrain

class CheckoutView(BrowserView):

    def is_ticket(self):
        result = is_context_ticket(self.context)
        return result

    def get_tickets_header(self, ticket):
        if ticket:
            folder = self.context
            if folder.portal_type in ["Folder", "Event"]:
                if folder.portal_type == "Event":
                    uuid = folder.UID()
                    brain = uuidToCatalogBrain(uuid)
                    if brain:
                        leadmedia = getattr(brain, 'leadMedia', None)
                        if leadmedia:
                            image = uuidToCatalogBrain(leadmedia)
                            if hasattr(image, 'getURL'):
                                url = image.getURL()
                                scale_url = "%s/%s" %(url, "@@images/image/large")
                                return scale_url
                else:
                    contents = folder.getFolderContents({"portal_type": "Image", "Title":"tickets-header"})
                    if len(contents) > 0:
                        image = contents[0]
                        url = image.getURL()
                        scale_url = "%s/%s" %(url, "@@images/image/large")
                        return scale_url
        else:
            brains = self.context.portal_catalog(Title="webwinkel-header", portal_type="Image")
            if len(brains) > 0:
                brain = brains[0]
                if brain.portal_type == "Image":
                    url = brain.getURL()
                    scale_url = "%s/%s" %(url, "@@images/image/large")
                    return scale_url

            return ""