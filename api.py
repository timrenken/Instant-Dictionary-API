import justpy as jp
import definition
import json

class Api:

    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        term = req.query_params.get("term")

        defined = definition.Definition(term).get()

        response = {
            "term": term,
            "definition": defined
        }
        wp.html = json.dumps(response)
        return wp

jp.Route("/api", Api.serve)
jp.justpy(port=8008)
