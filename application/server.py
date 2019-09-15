import responder

api = responder.API()


@api.route("/")
def hello(req, resp):
    resp.text = "Hello world!"


@api.route("/api/prediction/iris")
class PredictionIrisResource:
    async def on_post(self, req, resp):
        r = await req.media()
        resp.media = {"results": [], "resuest": r}


if __name__ == "__main__":
    api.run()
