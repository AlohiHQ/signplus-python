from typing import Union
from .net.environment import Environment
from .sdk import SignplusDeveloperApiV2SpecSdk
from .services.async_.signplus import SignplusServiceAsync


class SignplusDeveloperApiV2SpecSdkAsync(SignplusDeveloperApiV2SpecSdk):
    """
    SignplusDeveloperApiV2SpecSdkAsync is the asynchronous version of the SignplusDeveloperApiV2SpecSdk SDK Client.
    """

    def __init__(
        self,
        access_token: str = None,
        base_url: Union[Environment, str, None] = None,
        timeout: int = 60000,
    ):
        super().__init__(access_token=access_token, base_url=base_url, timeout=timeout)

        self.signplus = SignplusServiceAsync(base_url=self._base_url)
