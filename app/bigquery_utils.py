from google.cloud import bigquery
import os
import traceback
from fastapi import HTTPException

_client = bigquery.Client()

DATASET = os.getenv("BQ_DATASET", "usage_data")
TABLE = os.getenv("BQ_TABLE", "resource_usage")
PROJECT = _client.project


def full_table_name():
    return f"{PROJECT}.{DATASET}.{TABLE}"

async def query(sql: str) -> list[dict]:
    try:
        client = bigquery.Client()
        job_config = bigquery.QueryJobConfig()
        print("🔎 DATASET:", os.getenv("BQ_DATASET"))
        print("🔎 TABLE  :", os.getenv("BQ_TABLE"))
        print("🔎 SQL    :", sql[:200])      # first 200 chars
        job = client.query(sql, job_config=job_config)
        rows = job.result()
        return [dict(row.items()) for row in rows]
    except Exception as exc:
        print("💥 BIGQUERY ERROR\n", traceback.format_exc())
        raise HTTPException(status_code=500, detail="BigQuery query failed")
