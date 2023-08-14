# Newspapers
news = {
    "name": "Newspapers",
    "env": {
        "source": {"value": "YAMS_NEWSPAPER", "list": False},
        "since": {"value": "YAMS_NEWSPAPER_SINCE", "list": False},
        "to": {"value": "YAMS_NEWSPAPER_TO", "list": False},
        "keywords": {"value": "YAMS_NEWSPAPER_KEYWORDS", "list": True},
        "output": {"value": "YAMS_NEWSPAPER_OUTPUT", "list": False},
    },
    "spiders": ["diariocorreo", "elcomercio", "peru21"],
}
