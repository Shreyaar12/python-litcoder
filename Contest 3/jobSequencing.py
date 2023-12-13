def job_sequencing(jobs, deadlines, profits):
    """
    Schedule jobs to maximize profit given deadlines and profits for each job.

    Parameters:
    jobs (list): List of job names.
    deadlines (list): Corresponding deadlines for each job.
    profits (list): Corresponding profits for each job.

    Returns:
    list: List of job names in the order they should be scheduled.
    """
    # Combine the job info into a single list and sort by profit in descending order
    job_info = sorted(zip(jobs, deadlines, profits), key=lambda x: x[2], reverse=True)

    # Initialize variables
    max_deadline = max(deadlines)
    scheduled_jobs = [None] * max_deadline
    total_profit = 0

    # Iterate over jobs and schedule them if possible
    for job, deadline, profit in job_info:
        for i in range(min(max_deadline, deadline) - 1, -1, -1):
            if scheduled_jobs[i] is None:
                scheduled_jobs[i] = job
                total_profit += profit
                break

    # Filter out None values and return the scheduled jobs
    return [job for job in scheduled_jobs if job]

# User input handling
if __name__ == "__main__":
    job_count = int(input("Enter the number of jobs: "))
    jobs = input("Enter the job names: ").split()
    deadlines = list(map(int, input("Enter the deadlines: ").split()))
    profits = list(map(int, input("Enter the profits: ").split()))

    result = job_sequencing(jobs, deadlines, profits)
    print("Scheduled jobs for maximum profit:", ' '.join(result))

