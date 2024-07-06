from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        industries = [
            job["industry"] for job in self.jobs_list if job.get("industry")
        ]
        seIndustries = set(industries)
        return list(seIndustries)
