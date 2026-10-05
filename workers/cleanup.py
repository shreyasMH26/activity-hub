def cleanup_worker_pool(workers):
    for worker in workers:
        worker.terminate()
        worker.join()
