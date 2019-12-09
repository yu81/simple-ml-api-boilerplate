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
        scores = prediction_task.predict_proba(r["data"])
        results = prediction_task.predict(r["data"])
        resp.media = {
            "scores": scores.tolist(),
            "result": results.tolist(),
            "request": r,
        }


if __name__ == "__main__":
    api.run(workers=2)
