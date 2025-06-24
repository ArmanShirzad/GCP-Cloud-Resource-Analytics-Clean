from fastapi import FastAPI
from . import bigquery_utils, analysis, models

app = FastAPI(title="Cloud Resource Analytics API")

@app.get("/usage", response_model=list[models.UsageRecord])
async def get_usage():
    query = """
        SELECT FORMAT_DATE('%F', DATE(timestamp)) as date, service, SUM(usage_amount) as usage_amount
        FROM `{dataset}`
        GROUP BY date, service
        ORDER BY date DESC
        LIMIT 100
    """.format(dataset=bigquery_utils.full_table_name())
    rows = await bigquery_utils.query(query)
    return [models.UsageRecord(**row) for row in rows]

@app.get("/costs")
async def get_costs():
    query = """
        SELECT service, SUM(cost_usd) as cost_usd
        FROM `{dataset}`
        GROUP BY service
    """.format(dataset=bigquery_utils.full_table_name())
    rows = await bigquery_utils.query(query)
    return rows

@app.get("/recommendations", response_model=list[models.Recommendation])
async def recommendations():
    recs = await analysis.idle_vm_recommendations()
    return recs
