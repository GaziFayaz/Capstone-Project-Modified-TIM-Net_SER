from google.cloud import speech
from google.oauth2 import service_account

client_file = "servcie_emotex.json"
credentials = service_account.Credentials.from_service_account_file(client_file)