from pydantic import BaseModel, Field


class FinanceInput(BaseModel):
    query: str = Field(description="The user's query related to finance.")


class LegalInput(BaseModel):
    query: str = Field(
        description="The user's query related to legal or compliance.")


class MarketingInput(BaseModel):
    query: str = Field(
        description="The user's query related to marketing or launch strategies.")
