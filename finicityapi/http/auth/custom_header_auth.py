# -*- coding: utf-8 -*-

from finicityapi.configuration import Configuration


class CustomHeaderAuth:

    @staticmethod
    def apply(http_request):
        """ Add custom authentication to the request.

        Args:
            http_request (HttpRequest): The HttpRequest object to which 
                authentication will be added.

        """                
        http_request.add_header("Finicity-App-Token", Configuration.finicity_app_token)
