from gnewsclient import gnewsclient

_client = gnewsclient.NewsClient()


def fetch_news(params) -> list:

    _client.language = params.get("language")
    _client.location = params.get("geo-country")
    _client.topic = params.get("topic")

    return _client.get_news()[:3]
