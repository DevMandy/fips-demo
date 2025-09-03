FROM cgr.dev/chainguard-private/python-fips:latest

WORKDIR /app

COPY main.py /app

ENTRYPOINT ["python3"]
CMD ["main.py"]
