FROM python:3.12-slim
WORKDIR /app
COPY chatbot/requirements.txt chatbot/requirements.txt
RUN pip install --no-cache-dir -r chatbot/requirements.txt
COPY chatbot chatbot
ENV PYTHONUNBUFFERED=1
CMD ["python", "-m", "chatbot.main"]
