import pytest
from src.insights.salaries import ProcessSalaries

TOTAL_JOBS_WITH_SPECIFIED_SALARY = 2232
MAX_SALARY = 383416
MIN_SALARY = 19857


import pytest
from src.insights.salaries import ProcessSalaries

TOTAL_JOBS_WITH_SPECIFIED_SALARY = 2232
MAX_SALARY = 383416
MIN_SALARY = 19857


def test_get_max_salary():
    process_salaries = ProcessSalaries()
    process_salaries.read("data/jobs.csv")
    assert process_salaries.get_max_salary() == MAX_SALARY

    process_salaries.jobs_list = (
        []
    )  # Assuming jobs_list is public or has a setter method
    process_salaries.read("tests/mocks/jobs_with_salaries.csv")
    assert process_salaries.get_max_salary() == 8000


def test_get_min_salary():
    process_salaries = ProcessSalaries()
    process_salaries.read("data/jobs.csv")
    assert process_salaries.get_min_salary() == MIN_SALARY

    process_salaries.jobs_list = (
        []
    )  # Assuming jobs_list is public or has a setter method
    process_salaries.read("tests/mocks/jobs_with_salaries.csv")
    assert process_salaries.get_min_salary() == 1000


def test_matches_salary_range():
    invalid_jobs = [
        {"max_salary": 0, "min_salary": 10},
        {"max_salary": 10, "min_salary": 100},
        {"max_salary": -1, "min_salary": 10},
    ]
    jobs = [
        {"max_salary": 10000, "min_salary": 200},
        {"max_salary": 1500, "min_salary": 0},
    ]
    salaries = [0, 1, 5, 1000, 2000, -1, -2]
    expected = [
        [False, False, False, True, True, False, False],
        [True, True, True, True, False, False, False],
    ]

    for job in invalid_jobs:
        for salary in salaries:
            with pytest.raises(ValueError):
                ProcessSalaries().matches_salary_range(job, salary)

    for job_index in range(len(jobs)):
        for salary_index in range(len(salaries)):
            result = ProcessSalaries().matches_salary_range(
                jobs[job_index], salaries[salary_index]
            )
            assert result == expected[job_index][salary_index]

    # ? Valida que pode ser passada uma string numérica
    assert ProcessSalaries().matches_salary_range(jobs[1], "5") is True
    assert ProcessSalaries().matches_salary_range(jobs[1], "1800") is False

    invalid_types = [None, "", "aloha", [], {}, lambda: 1]
    for invalid in invalid_types:
        with pytest.raises(ValueError):
            ProcessSalaries().matches_salary_range(
                {"max_salary": "1000", "min_salary": invalid}, 20
            )
        with pytest.raises(ValueError):
            ProcessSalaries().matches_salary_range(
                {"min_salary": "1000", "max_salary": invalid}, 20
            )
        with pytest.raises(ValueError):
            ProcessSalaries().matches_salary_range(
                {"min_salary": "100", "max_salary": "1000"}, invalid
            )
    with pytest.raises(ValueError):
        ProcessSalaries().matches_salary_range({"max_salary": "1000"}, 10)
    with pytest.raises(ValueError):
        ProcessSalaries().matches_salary_range({"min_salary": "1000"}, 10)
