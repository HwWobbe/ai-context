from flask import Flask, redirect
import requests
 
app = Flask(__name__)
 
@app.route("/jump/<path:key>")
def jump(key):
    r = requests.get(
        f"http://localhost:8080/recipes/default/tiddlers/jump%2F{key}",
        headers={"Accept": "application/json"}
    )
    if r.ok:
        data = r.json()
        target = data.get("target") or data.get("fields", {}).get("target") or data.get("text", "").strip()
        if target:
            return redirect(target)
    return f"No jump for: {key}", 404
 
if __name__ == "__main__":
    app.run(port=5099)
 