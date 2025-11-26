from app.core.celery_app import celery_app


@celery_app.task
def test_task():
    return {"message": "Test task completed"}


@celery_app.task
def send_email_task(email: str, subject: str, message: str):
    # Simulate sending email
    print(f"Sending email to {email}: {subject} - {message}")
    return {"message": f"Email sent to {email}"}


@celery_app.task
def process_data_task(data: dict):
    # Simulate data processing
    processed_data = {
        k: v.upper() if isinstance(v, str) else v for k, v in data.items()
    }
    return {"processed_data": processed_data}
