#!/usr/bin/env python
# -*- coding: utf-8 -*
from Products.Five import BrowserView


class CheckoutView(BrowserView):
    def get_tickets_header(self, is_ticket):
        if is_ticket:
            folder = self.context
            if folder.portal_type == "Folder":
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