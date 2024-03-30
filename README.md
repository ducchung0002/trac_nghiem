pip install -r requirements.txt
uvicorn main:app --port 4444
  OR 'hypercorn main:app --worker-class trio --workers 4 --bind localhost:4444' for multiple workers
