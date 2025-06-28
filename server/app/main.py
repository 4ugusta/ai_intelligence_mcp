from fastapi import FastAPI, Depends
from .orchestrator import orchestrate_query
from .models import QueryRequest, QueryResponse

app = FastAPI(title="MCP Server")

@app.post("/query", response_model=QueryResponse)
async def query_endpoint(request: QueryRequest):
    """Accept natural language query and return aggregated results."""
    return await orchestrate_query(request)
