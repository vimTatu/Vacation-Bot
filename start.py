from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build


# http = httplib2.Http()

def send_message(chat):
    resp = chat.spaces().messages().create(
        parent = 'spaces/AAAAOCm3BHc',
        body = {'text' : 'Hello world'}).execute()
    print(resp)


def auth():
    scopes = 'https://www.googleapis.com/auth/chat.bot'
    credentials = ServiceAccountCredentials.from_json_keyfile_name('Vacation-Bot-9e57beb0a8be.json', scopes)
    bot = build('chat', 'v1', http=credentials.authorize(Http()))
    return bot


if __name__ == '__main__':
    bot = auth()
    send_message(bot)