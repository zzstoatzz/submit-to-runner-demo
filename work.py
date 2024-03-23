import asyncio
from prefect import flow, task
from prefect.runner.submit import submit_to_runner, wait_for_submitted_runs

@task
async def fetch_data(url: str) -> dict:
    await asyncio.sleep(2)
    return {"url": url, "data": "Sample data"}

@task
async def process_data(data: dict) -> str:
    await asyncio.sleep(1)
    return f"Processed data from {data['url']}"

@flow
async def data_processing_pipeline(urls: list[str]):
    fetched_data = await fetch_data.map(urls)
    return await process_data.map(fetched_data)

@flow
async def sample_async_etl():
    urls = ["https://example.com", "https://example.org", "https://example.net"]
    await submit_to_runner(data_processing_pipeline, [{"urls": urls} for _ in range(5)])
    await wait_for_submitted_runs()

if __name__ == "__main__":
    sample_async_etl.serve("data-processing", webserver=True, limit=50)