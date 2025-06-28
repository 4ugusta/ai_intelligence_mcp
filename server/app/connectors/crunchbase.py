from typing import List
from ..models import CompanyProfile, SourceData
from .base import BaseConnector


class CrunchbaseConnector(BaseConnector):
    async def search_companies(self, query: str) -> List[CompanyProfile]:
        # Stub implementation returning fake data
        return [
            CompanyProfile(
                name="AI Startup A",
                description="A sample AI company from Crunchbase",
                sources=[SourceData(source="Crunchbase", value="Sample data", confidence=0.8)],
            )
        ]
