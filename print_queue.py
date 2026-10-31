# print_queue.py
# Application exercise 6b: simulate a print queue (FIFO).
# Each job has an ID and a page count.

from linked_queue import LinkedQueue


def run_print_queue(jobs):
    q = LinkedQueue()
    for job_id, pages in jobs:
        q.enqueue((job_id, pages))
        print("Submitted job", job_id, "(" + str(pages) + " pages)")

    print("\n--- Printing in FIFO order ---")
    order = 1
    pages_before = 0
    while not q.is_empty():
        job_id, pages = q.dequeue()
        print("#" + str(order), "Printing job", job_id, "-", pages, "pages",
              "| waited for", pages_before, "pages before it")
        pages_before = pages_before + pages
        order = order + 1
    print("\nAll jobs done. Total pages printed:", pages_before)


if __name__ == "__main__":
    sample_jobs = [("J101", 5), ("J102", 12), ("J103", 3), ("J104", 8)]
    run_print_queue(sample_jobs)
