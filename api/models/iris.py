from pydantic import BaseModel, Field


class PredictRequest(BaseModel):
    sepal_length: float = Field(..., example=5.1, description="Sepal length in cm")
    sepal_width: float = Field(..., example=3.5, description="Sepal width in cm")
    petal_length: float = Field(..., example=1.4, description="Petal length in cm")
    petal_width: float = Field(..., example=0.2, description="Petal width in cm")


class PredictResponse(BaseModel):
    prediction: str = Field(..., example="setosa", description="Predicted Iris species")
