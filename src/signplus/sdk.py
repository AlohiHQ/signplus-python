from .services.signplus import SignplusService
from .net.environment import Environment


class Signplus:
    def __init__(
        self,
        access_token: str = None,
        base_url: str = Environment.DEFAULT.value,
        timeout: int = 60000,
    ):
        """
        Initializes Signplus the SDK class.
        """
        self.signplus = SignplusService(base_url=base_url)
        self.set_access_token(access_token)
        self.set_timeout(timeout)

    def set_base_url(self, base_url):
        """
        Sets the base URL for the entire SDK.
        """
        self.signplus.set_base_url(base_url)

        return self

    def set_access_token(self, access_token: str):
        """
        Sets the access token for the entire SDK.
        """
        self.signplus.set_access_token(access_token)

        return self

    def set_timeout(self, timeout: int):
        """
        Sets the timeout for the entire SDK.

        :param int timeout: The timeout (ms) to be set.
        :return: The SDK instance.
        """
        self.signplus.set_timeout(timeout)

        return self


# c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c
