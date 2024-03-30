<h3>pip install -r requirements.txt</h3>
<h3>uvicorn main:app --port 4444</h3>
OR <code>hypercorn main:app --worker-class trio --workers 4 --bind localhost:4444</code> for multiple workers
