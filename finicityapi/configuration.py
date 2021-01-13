# -*- coding: utf-8 -*-

from finicityapi.api_helper import APIHelper


class Configuration(object):

    """A class used for configuring the SDK by a user.

    This class need not be instantiated and all properties and methods
    are accessible without instance creation.

    """

    # Set the array parameter serialization method
    # (allowed: indexed, unindexed, plain, csv, tsv, psv)
    array_serialization = "indexed"

    # An enum for SDK environments
    class Environment(object):
        # Production
        PRODUCTION = 0

    # An enum for API servers
    class Server(object):
        DEFAULT = 0

    # The environment in which the SDK is running
    environment = Environment.PRODUCTION

    # Finicity-App-Key from Developer Portal
    # TODO: Set an appropriate value
    finicity_app_key = None

    # Token returned from Partner Authentication
    # TODO: Set an appropriate value
    finicity_app_token = None


    # All the environments the SDK can run in
    environments = {
        Environment.PRODUCTION: {
            Server.DEFAULT: 'https://api.finicity.com',
        },
    }

    @classmethod
    def get_base_uri(cls, server=Server.DEFAULT):
        """Generates the appropriate base URI for the environment and the server.

        Args:
            server (Configuration.Server): The server enum for which the base URI is required.

        Returns:
            String: The base URI.

        """
        return cls.environments[cls.environment][server]
