import json
from typing import Optional
from requests import Response as RequestsResponse
from urllib.parse import parse_qs


class Response:
    """
    A simple HTTP response wrapper class using the requests library.

    :ivar int status: The status code of the HTTP response.
    :ivar dict headers: The headers of the HTTP response.
    :ivar str body: The body of the HTTP response.
    :var str chunk: The chunk of the HTTP response.
    """

    def __init__(self, response: RequestsResponse, chunk: Optional[str] = None):
        """
        Initializes a Response object.

        :param RequestsResponse response: The requests.Response object.
        """
        self.status = response.status_code
        self.headers = response.headers
        if chunk:
            self.body = json.loads(chunk)
        else:
            self.body = self._get_response_body(response)

    def __str__(self) -> str:
        """
        Return a string representation of the Response object.

        :return: A string representation of the Response object.
        :rtype: str
        """
        return (
            f"Response(status={self.status}, headers={self.headers}, body={self.body})"
        )

    def _get_response_body(self, response: RequestsResponse) -> str:
        """
        Extracts the response body from a given HTTP response.

        This method attempts to parse the response body based on its content type.
        If the content type is JSON, it tries to parse the body as JSON.
        If the content type is text or XML, it returns the raw text.
        If the content type is 'application/x-www-form-urlencoded', it parses the body as a query string.
        For all other content types, it returns the raw binary content.

        :param RequestsResponse response: The HTTP response received from a request.
        :return: The parsed response body.
        :rtype: str or dict or bytes
        """
        try:
            return response.json()
        except ValueError:
            content_type = response.headers.get("Content-Type", "").lower()
            if "text/" in content_type or content_type == "application/xml":
                return response.text
            elif content_type == "application/x-www-form-urlencoded":
                parsed_response = parse_qs(response.text)
                return {k: v[0] for k, v in parsed_response.items()}
            else:
                return response.content
