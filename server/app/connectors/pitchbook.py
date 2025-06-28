from typing import List
from ..models import CompanyProfile, SourceData
from .base import BaseConnector


class PitchbookConnector(BaseConnector):
    async def search_companies(self, query: str) -> List[CompanyProfile]:
        # Stub implementation returning fake data
        return [
            CompanyProfile(
                name="AI Startup C",
                description="A sample AI company from PitchBook",
                sources=[SourceData(source="PitchBook", value="Sample data", confidence=0.7)],
            )
        ]
