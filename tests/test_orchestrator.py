import asyncio
from server.app.models import QueryRequest
from server.app.orchestrator import orchestrate_query


def test_orchestrator_returns_scored_results():
    request = QueryRequest(query="AI startups")
    response = asyncio.run(orchestrate_query(request))
    assert len(response.results) >= 3
    for profile in response.results:
        assert 0.0 <= profile.score <= 1.0
        assert len(profile.sources) >= 1
