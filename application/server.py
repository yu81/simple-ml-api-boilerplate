import responder

api = responder.API()


@api.route("/")
def hello(req, resp):
    resp.text = "Hello world!"


@api.route("/api/prediction/iris")
class PredictionIrisResource:
    def on_post(self, req, resp):
        resp.media = {"results": []}


if __name__ == "__main__":
    api.run()
