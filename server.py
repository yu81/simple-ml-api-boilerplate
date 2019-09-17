import responder

from predictions import task as prediction_task

api = responder.API()


@api.route("/")
def hello(req, resp):
    resp.text = "Hello world!"


@api.route("/api/prediction/iris")
class PredictionIrisResource:
    async def on_post(self, req, resp):
        r = await req.media()
        prediction_task.score(r["data"])
        resp.media = {"results": [], "resuest": r}


if __name__ == "__main__":
    api.run(workers=2)
