from fastapi import FastAPI
from inference import load_model, predict as perform_prediction
from api.models.iris import PredictRequest, PredictResponse

app = FastAPI(title="ML API", description="API for serving ML models")

model = load_model()

app = FastAPI()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    input_data = [
        request.sepal_length,
        request.sepal_width,
        request.petal_length,
        request.petal_width,
    ]
    prediction_result = perform_prediction(model, input_data)
    return PredictResponse(prediction=prediction_result)
