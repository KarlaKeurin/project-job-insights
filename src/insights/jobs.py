from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path, encoding="utf8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row:
                    self.jobs_list.append(row)
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        jobTypes = [job["job_type"] for job in self.jobs_list]
        seJobTypes = set(jobTypes)
        return list(seJobTypes)

    def filter_by_multiple_criteria(
        self, jobs: List[Dict], filter_criteria: Dict
    ):
        try:
            filteredJobs = []
            for job in jobs:
                if all(
                    job[key] == value for key, value in filter_criteria.items()
                ):
                    filteredJobs.append(job)
            return filteredJobs
        except (ValueError, AttributeError):
            raise TypeError("Filter criteria must be a dictionary")
