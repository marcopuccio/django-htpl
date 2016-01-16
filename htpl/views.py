# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView

class IndexTemplateView(TemplateView):
    """
    This view will render the index template that must be called index.html 
    """
    template_name = 'htpl/index.html'


class GenericTemplateNameView(TemplateView):
    """
    This view will search a template using the slug passed via URL
    """    
    def get_template_names(self):
        return [
                "htpl/{0}.html".format(self.kwargs.get('tpl_name')),
                ]
