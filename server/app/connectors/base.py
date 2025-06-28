from abc import ABC, abstractmethod
from typing import List

from ..models import CompanyProfile


class BaseConnector(ABC):
    @abstractmethod
    async def search_companies(self, query: str) -> List[CompanyProfile]:
        """Return a list of CompanyProfiles matching the query."""
        raise NotImplementedError
