<h3><code>pip install -r requirements.txt</code></h3>
<h3><code>uvicorn main:app --port 4444</code></h3>
OR <code>hypercorn main:app --worker-class trio --workers 4 --bind localhost:4444</code> for multiple workers
