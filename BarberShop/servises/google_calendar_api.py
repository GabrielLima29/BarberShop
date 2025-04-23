import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']
CALENDAR_IDS = {
    "felipe": "felipe.agenda@gmail.com",
    "matheus": "matheus.agenda@gmail.com",
    "guilherme": "guilherme.agenda@gmail.com",
}

def criar_servico_google():
    creds = service_account.Credentials.from_service_account_file(
        'credentials.json', scopes=SCOPES
    )
    return build('calendar', 'v3', credentials=creds)

def verificar_disponibilidade(servico, calendar_id, data_str, hora_str):
    data = datetime.datetime.strptime(f"{data_str} {hora_str}", "%d/%m %H:%M")
    inicio = data.isoformat() + "-03:00"
    fim = (data + datetime.timedelta(minutes=30)).isoformat() + "-03:00"

    eventos = servico.events().list(
        calendarId=calendar_id,
        timeMin=inicio,
        timeMax=fim,
        singleEvents=True,
        orderBy="startTime"
    ).execute()

    return len(eventos.get('items', [])) == 0

def agendar_evento(servico, calendar_id, nome, telefone, data_str, hora_str):
    data = datetime.datetime.strptime(f"{data_str} {hora_str}", "%d/%m %H:%M")
    inicio = data.isoformat() + "-03:00"
    fim = (data + datetime.timedelta(minutes=30)).isoformat() + "-03:00"

    evento = {
        "summary": f"Agendamento - {nome}",
        "description": f"Cliente: {nome}\nTelefone: {telefone}",
        "start": {"dateTime": inicio, "timeZone": "America/Sao_Paulo"},
        "end": {"dateTime": fim, "timeZone": "America/Sao_Paulo"},
    }
    evento_criado = servico.events().insert(calendarId=calendar_id, body=evento).execute()
    return evento_criado.get("htmlLink")

def buscar_evento_cliente(servico, calendar_id, nome, telefone):
    agora = datetime.datetime.utcnow().isoformat() + 'Z'
    eventos = servico.events().list(
        calendarId=calendar_id,
        timeMin=agora,
        maxResults=10,
        singleEvents=True,
        orderBy="startTime"
    ).execute()

    for evento in eventos.get('items', []):
        descricao = evento.get('description', '')
        if nome.lower() in descricao.lower() and telefone in descricao:
            return {
                "id": evento["id"],
                "summary": evento.get("summary"),
                "start": evento["start"].get("dateTime"),
                "link": evento.get("htmlLink")
            }
    
def excluir_evento(servico, calendar_id, evento_id):
    try:
        servico.events().delete(calendarId=calendar_id, eventId=evento_id).execute()
        return True
    except Exception as e:
        print(f"Erro ao excluir evento: {e}")
        return False    
    