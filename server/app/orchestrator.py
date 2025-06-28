import asyncio
from typing import Dict, List
from .models import QueryRequest, QueryResponse, CompanyProfile
from .connectors.base import BaseConnector
from .connectors.crunchbase import CrunchbaseConnector
from .connectors.cbinsights import CBInsightsConnector
from .connectors.pitchbook import PitchbookConnector
from .connectors.openweb import OpenWebConnector


async def orchestrate_query(request: QueryRequest) -> QueryResponse:
    """Run connectors in parallel, merge results and compute confidence."""
    connectors: List[BaseConnector] = [
        CrunchbaseConnector(),
        CBInsightsConnector(),
        PitchbookConnector(),
        OpenWebConnector(),
    ]

    # Fetch results concurrently
    results_lists = await asyncio.gather(
        *(c.search_companies(request.query) for c in connectors)
    )

    profiles: Dict[str, CompanyProfile] = {}
    for lst in results_lists:
        for item in lst:
            if item.name not in profiles:
                profiles[item.name] = item
            else:
                profiles[item.name].sources.extend(item.sources)

    # Simple confidence heuristic based on number of sources
    for profile in profiles.values():
        total = sum(s.confidence for s in profile.sources)
        profile.score = min(1.0, total / len(connectors))

    sorted_profiles = sorted(profiles.values(), key=lambda p: p.score, reverse=True)
    return QueryResponse(results=sorted_profiles)
