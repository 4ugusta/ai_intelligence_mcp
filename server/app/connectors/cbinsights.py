from typing import List
from ..models import CompanyProfile, SourceData
from .base import BaseConnector


class CBInsightsConnector(BaseConnector):
    async def search_companies(self, query: str) -> List[CompanyProfile]:
        # Stub implementation returning fake data
        return [
            CompanyProfile(
                name="AI Startup B",
                description="A sample AI company from CB Insights",
                sources=[SourceData(source="CB Insights", value="Sample data", confidence=0.75)],
            )
        ]
