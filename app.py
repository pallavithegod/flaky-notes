import os

from flask import Flask, jsonify

from storage import export_notes, list_notes

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/")
def index():
    items = "".join(f"<li>{note['title']}</li>" for note in list_notes())
    return f"""<!doctype html>
    <html><head><title>Flaky Notes</title></head>
    <body style="font-family: sans-serif; max-width: 40rem; margin: 3rem auto;">
      <h1>Flaky Notes</h1>
      <p>A demo notes service monitored by RecallOps.</p>
      <ul>{items}</ul>
      <form action="/notes/export" method="get">
        <button style="padding: 0.6rem 1.4rem; font-size: 1rem;">Export notes</button>
      </form>
    </body></html>"""


@app.get("/notes/export")
def notes_export():
    try:
        return jsonify(export_notes())
    except Exception:
        app.logger.exception("notes export failed")
        return jsonify(error="notes export failed"), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
