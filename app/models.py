from pydantic import BaseModel

class UsageRecord(BaseModel):
    date: str | None = None
    service: str
    usage_amount: float | None = None

class Recommendation(BaseModel):
    resource_name: str
    reason: str
    projected_savings: float | None = None
