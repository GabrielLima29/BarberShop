from schedule import BarberAgenda

def main():
    agenda = BarberAgenda()

    def print_menu():
        print("\n=== Barbearia Batista's - Sistema de Agendamento ===")
        print("1. Agendar corte")
        print("2. Verificar horários disponíveis")
        print("3. Alterar agendamento")
        print("4. Excluir agendamento")
        print("5. Sair")

    def is_blocked_time(time_str):
        blocked = {'07:00','07:30','08:00', '08:30', '19:00', '19:30', '20:00', '20:30', '21:00'}
        return time_str in blocked

    barbeiros = agenda.barbeiros

    while True:
        print_menu()
        option = input("Escolha uma opção: ").strip()

        if option == '1':
            print("\n-- Agendar corte --")  
            print("\nPrimeiro preencha os dados requisitados:")
            client_name = input("Seu nome: ").strip()
            phone = input("Seu telefone (com DDD): ").strip()
            print("Escolha o barbeiro:")
            for i, b in enumerate(barbeiros, 1):
                print(f"{i}. {b}")
            idx = input("Número do barbeiro: ").strip()
            if not idx.isdigit() or not (1 <= int(idx) <= len(barbeiros)):
                print("Barbeiro inválido.")
                continue
            barber = barbeiros[int(idx) - 1]

            while True:
                date = input("Data (DD/MM): ").strip()
                time = input("Hora (HH:MM): ").strip()
                if is_blocked_time(time):
                    print("Horário não permitido. Por favor, escolha um horário entre 09:00 e 18:30.")
                    continue
                success, message = agenda.adicionar_agendamento(client_name, phone, date, time, barber)
                print(message)
                if success:
                    print(f"\nObrigado, {client_name}! Seu corte foi agendado para {date} às {time} com o barbeiro {barber}."
                          "\n Favor comparecer no endereço: R. Mascarenhas Camelo, 517 - Vila Santana, Sorocaba - SP,")
                    break
                else:
                    print("Horário ou data não permitidos. Tente novamente.")

        elif option == '2':
            print("\n-- Verificar horários disponíveis dos barbeiros --")
            print("Escolha um barbeiro:")
            for i, b in enumerate(barbeiros, 1):
                print(f"{i}. {b}")
            idx = input("Número do barbeiro: ").strip()
            if not idx.isdigit() or not (1 <= int(idx) <= len(barbeiros)):
                print("Barbeiro inválido.")
                continue
            barber = barbeiros[int(idx) - 1]
            horarios = agenda.verificar_horarios(barber)
            print(f"\nHorários disponíveis para {barber}:")
            for horario in horarios:
                print(horario)

            agendar = input("Você gostaria de agendar um corte? (sim/não): ").strip().lower()
            if agendar == 'sim':
                client_name = input("Seu nome: ").strip()
                phone = input("Número de telefone: ").strip()
                date = input("Data (DD/MM): ").strip()
                time = input("Escolha o horário (HH:MM): ").strip()
                success, message = agenda.adicionar_agendamento(client_name, phone, date, time, barber)
                print(message)
                if success:
                    print(f"\nObrigado, {client_name}! Seu corte foi agendado para {date} às {time} com o barbeiro {barber}."
                          "\n Favor comparecer no endereço: R. Mascarenhas Camelo, 517 - Vila Santana, Sorocaba - SP,")
                    break

        elif option == '3':
            print("\n-- Alterar agendamento --")
            phone = input("Digite seu telefone (com DDD): ").strip()
            success, message = agenda.alterar_agendamento(phone)
            print("Agendamento alterado com sucesso!")
            break


        elif option == '4':
            print("\n-- Excluir agendamento --")
            phone = input("Digite seu telefone (com DDD): ").strip()
            success, message = agenda.buscar_e_excluir_agendamento(phone)
            print("Agendamento excluido com sucesso!")
            break

        elif option == '5':
            print("Volte sempre!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == '__main__':
    main()
