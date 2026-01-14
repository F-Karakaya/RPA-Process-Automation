import time
import logging
import random

# Setup Logging
logger = logging.getLogger("RetryHandler")
logger.setLevel(logging.INFO)
if not logger.handlers:
    ch = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - RETRY_HANDLER - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

class RetryHandler:
    """
    Manages retry logic for failed RPA processes with exponential backoff.
    """
    
    def __init__(self, max_retries=3, backoff_factor=2):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        
    def handle_retry(self, bot_name, job_id):
        """
        Attempts to retry a failed job.
        """
        logger.info(f"Received retry request for Job {job_id} ({bot_name}).")
        
        for attempt in range(1, self.max_retries + 1):
            wait_time = self.backoff_factor ** attempt
            logger.info(f"Attempt {attempt}/{self.max_retries}: Waiting {wait_time}s before retrying...")
            time.sleep(wait_time)
            
            # Simulate Retry Execution
            if random.random() > 0.3: # Increased success chance on retry
                logger.info(f"Job {job_id} ({bot_name}) Retry Successful on attempt {attempt}.")
                return True
            else:
                logger.warning(f"Job {job_id} ({bot_name}) Retry Failed on attempt {attempt}.")
        
        logger.critical(f"Job {job_id} ({bot_name}): All retry attempts failed. Raising Alert.")
        self.send_alert(bot_name, job_id)
        return False
        
    def send_alert(self, bot_name, job_id):
        """
        Simulate sending an alert to the support team.
        """
        logger.error(f"ALERT: Critical failure for {bot_name} (Job {job_id}). Support notified.")
