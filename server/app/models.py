from typing import List, Optional
from pydantic import BaseModel, Field

class SourceData(BaseModel):
    source: str
    value: str
    confidence: float = Field(0.0, ge=0.0, le=1.0)

class CompanyProfile(BaseModel):
    name: str
    description: Optional[str]
    sources: List[SourceData]
    score: float = Field(0.0, ge=0.0, le=1.0)

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    results: List[CompanyProfile]
