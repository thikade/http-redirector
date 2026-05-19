FROM python:3.13-alpine
WORKDIR /app
COPY redirect.py .
EXPOSE 8080
CMD ["python", "redirect.py"]
