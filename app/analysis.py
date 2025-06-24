from . import bigquery_utils
from .models import Recommendation

async def idle_vm_recommendations() -> list[Recommendation]:
    sql = f"""
        SELECT resource AS resource_name
        FROM `{bigquery_utils.full_table_name()}`
        WHERE service = 'Compute Engine'
          AND usage_amount = 0
          AND DATE(timestamp) < CURRENT_DATE() - 30
    """
    rows = await bigquery_utils.query(sql)
    recs = [Recommendation(resource_name=r["resource_name"],
                           reason="Idle VM >30 days")
            for r in rows]
    return recs
