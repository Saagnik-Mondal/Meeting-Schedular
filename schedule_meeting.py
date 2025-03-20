import datetime
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Google Calendar API scope
SCOPES = ["https://www.googleapis.com/auth/calendar"]

# Authenticate user and save credentials
def authenticate_google():
    creds = None
    try:
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    except FileNotFoundError:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        creds = flow.run_local_server(port=0)
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return creds

# Build service
credentials = authenticate_google()
service = build("calendar", "v3", credentials=credentials)

# Meeting details
event = {
    "summary": "Project Meeting",
    "location": "Google Meet",
    "description": "Discussing project updates.",
    "start": {
        "dateTime": (datetime.datetime.utcnow() + datetime.timedelta(days=1)).isoformat() + "Z",
        "timeZone": "Asia/Kolkata",
    },
    "end": {
        "dateTime": (datetime.datetime.utcnow() + datetime.timedelta(days=1, hours=1)).isoformat() + "Z",
        "timeZone": "Asia/Kolkata",
    },
    "attendees": [
        {"email": "attendee1@example.com"},
        {"email": "attendee2@example.com"}
    ],
    "conferenceData": {
        "createRequest": {
            "requestId": "random-string",
            "conferenceSolutionKey": {"type": "hangoutsMeet"},
        }
    },
}

# Insert event into Google Calendar
event = service.events().insert(calendarId="primary", body=event, conferenceDataVersion=1).execute()
print(f"Meeting Scheduled: {event.get('htmlLink')}")
