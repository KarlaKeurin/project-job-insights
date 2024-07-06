from typing import Union, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        maxSalaries = 0
        for job in self.jobs_list:
            if "max_salary" in job and job["max_salary"].isdigit():
                maxSalaries = max(maxSalaries, int(job["max_salary"]))
        return maxSalaries

    def get_min_salary(self) -> int:
        minSalaries = float("inf")
        for job in self.jobs_list:
            if "min_salary" in job and job["min_salary"].isdigit():
                minSalaries = min(minSalaries, int(job["min_salary"]))
        return minSalaries

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        try:
            if "min_salary" not in job or "max_salary" not in job:
                raise ValueError(
                    "Missing min_salary or max_salary in job dictionary"
                )

            min_salary = int(job["min_salary"])
            max_salary = int(job["max_salary"])
            salary = int(salary)

            if min_salary > max_salary:
                raise ValueError("min_salary is greater than max_salary")

            return min_salary <= salary <= max_salary

        except (ValueError, TypeError):
            raise ValueError("Invalid salary or salary range values")
