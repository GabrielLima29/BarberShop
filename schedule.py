from datetime import datetime, timedelta

class BarberAgenda:
    def __init__(self):
        self.agendamentos = []
        self.barbeiros = ["Felipe", "Matheus", "Guilherme"]
        self.horarios_disponiveis = self.gerar_horarios()

    def gerar_horarios(self):
        inicio = datetime.strptime("09:00", "%H:%M")
        fim = datetime.strptime("18:30", "%H:%M")
        intervalo = timedelta(minutes=30)
        horarios = []

        while inicio <= fim:
            horarios.append(inicio.strftime("%H:%M"))
            inicio += intervalo

        return horarios

    def verificar_horarios(self, barbeiro):
        return self.horarios_disponiveis

    def adicionar_agendamento(self, cliente, telefone, data, hora, barbeiro):
        self.agendamentos.append({
            'cliente': cliente,
            'telefone': telefone,
            'data': data,
            'hora': hora,
            'barbeiro': barbeiro
        })
        return True, "Agendamento realizado com sucesso!"

    def visualizar_agendamentos(self):
        return self.agendamentos

    def alterar_agendamento(self, telefone):
        for appt in self.agendamentos:
            if appt['telefone'] == telefone:
                print(f"Agendamento encontrado: {appt}")
                print("Deixe em branco para manter o valor atual.")
                
                new_client = input(f"Novo nome do cliente (atual: {appt['cliente']}): ").strip()
                new_phone = input(f"Novo telefone (atual: {appt['telefone']}): ").strip()
                new_date = input(f"Nova data (DD/MM) (atual: {appt['data']}): ").strip()
                new_time = input(f"Nova hora (HH:MM) (atual: {appt['hora']}): ").strip()
                print("Escolha o novo barbeiro (ou deixe em branco):")
                for i, b in enumerate(self.barbeiros, 1):
                    print(f"{i}. {b}")
                barber_idx = input("Número do barbeiro: ").strip()
                new_barber = self.barbeiros[int(barber_idx) - 1] if barber_idx.isdigit() and (1 <= int(barber_idx) <= len(self.barbeiros)) else appt['barbeiro']

                appt['cliente'] = new_client if new_client else appt['cliente']
                appt['telefone'] = new_phone if new_phone else appt['telefone']
                appt['data'] = new_date if new_date else appt['data']
                appt['hora'] = new_time if new_time else appt['hora']
                appt['barbeiro'] = new_barber

                return True, "Agendamento alterado com sucesso!"
        
        return False, "Agendamento não encontrado."

    def buscar_e_excluir_agendamento(self, telefone):
        for appt in self.agendamentos:
            if appt['telefone'] == telefone:
                print(f"Agendamento encontrado: {appt}")
                confirmacao = input("Você deseja excluir este agendamento? (sim/não): ").strip().lower()
                if confirmacao == 'sim':
                    self.agendamentos.remove(appt)
                    return True, "Agendamento excluído com sucesso!"
                else:
                    return False, "Exclusão cancelada."
        
        return False, "Não há agendamento encontrado para este telefone."
