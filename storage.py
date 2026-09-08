NOTES = [
    {"id": 1, "title": "Ship the demo", "body": "Crash an app, watch the PR appear."},
    {"id": 2, "title": "Retro notes", "body": "Remember to rotate the API keys."},
    # Legacy record without a body; exports should tolerate missing content.
    {"id": 3, "title": "Migration leftovers"},
]


def list_notes():
    return [{"id": note["id"], "title": note["title"]} for note in NOTES]


def export_notes():
    return [
        {"id": note["id"], "title": note["title"], "body": note.get("body", "")}
        for note in NOTES
    ]
