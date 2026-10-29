"""Send a one-time code by email and store a file, with Google API clients imported lazily."""

import base64
from email.message import EmailMessage


def send_login_code(credentials, to_address: str, code: str) -> None:
    from googleapiclient.discovery import build

    message = EmailMessage()
    message["To"] = to_address
    message["Subject"] = "Your sign-in code"
    message.set_content(f"Your code is {code}")
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    gmail = build("gmail", "v1", credentials=credentials)
    gmail.users().messages().send(userId="me", body={"raw": raw}).execute()


def archive_transcript(credentials, folder_id: str, path: str) -> str:
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload

    drive = build("drive", "v3", credentials=credentials)
    created = drive.files().create(
        body={"name": path.rsplit("/", 1)[-1], "parents": [folder_id]},
        media_body=MediaFileUpload(path),
    ).execute()
    return created["id"]
