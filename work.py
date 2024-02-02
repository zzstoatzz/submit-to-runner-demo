import time
from prefect import flow, task
from prefect.runner.submit import submit_to_runner

@task
def simulate_work(duration: int) -> None:
    time.sleep(duration)

@flow
def collection_of_tasks(x: int):
    simulate_work.map(range(x))


@flow
def my_flow():
    submit_to_runner(collection_of_tasks, [{"x": i} for i in range(10)])

if __name__ == "__main__":
    my_flow.serve("simulate-work", webserver=True, limit=10)