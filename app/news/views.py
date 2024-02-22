import json
import subprocess

from django.shortcuts import render


def index(request):
    return render(request, "news/index.html", {})


def search(request):
    query = request.GET.get("query", "")
    output = subprocess.run(
        ["yams", "start", "newspaper", "elcomercio", "-k", query],
        stdout=subprocess.PIPE,
        universal_newlines=True
    )
    posts = [json.loads(post) for post in output.stdout.splitlines()]
    return render(request, "news/result.html", {"query": query, "posts": posts})
