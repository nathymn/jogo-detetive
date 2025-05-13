from typing import List, Optional
import random
import ttg

while True:
    gamer = input("Olá investigador! Qual seu nome? ")
    if gamer == "":
        print("Por favor, diga seu nome para registro \n")
        continue
    elif not gamer.isalpha():
        print("Números não são aceitos em seu nome! \n")
        continue
    else:
        break

# definição das informações
def infos():
    time = ["manhã", "tarde", "noite", "madrugada"]
    suspects = {
        "Micah": "Assassino lendário.",
        "Abigail": "Ex-meretriz no bordel de Imbituva, que posteriormente virou dona do estabelecimento. ",
        "Lenny": "Vendedor de armas em Imbituva. ",
        "Javier": "Responsável pelo estábulo de Imbituva.",
        "Bill": "Banqueiro no banco de Imbituva.",
        "Pearson": "Cozinheiro do acampamento e açougueiro da cidade de Imbituva.",
        "Sadie": "Caçadora de Recompensas. ",
        "Leopold": "Recepcionista e dono do Hotel em Imbituva. ",
        "Doutor": "Médico e dono da farmácia de Imbituva.",
        "Sally": "Bartender do Saloon da cidade. "
    }
    places = ["Consutório médico", "Banco", "Loja de Armas", "Departamento do Xerife", "Acampamento", "Teatro",
              "Bordel", "Saloon", "Hotel", "Estábulo"]
    arm = ["Faca", "Veneno", "Revólver", "Corda", "Pá", "Arco e flecha", "Garrafa de vidro"]

    time_of_death = random.choice(time)
    arm_use = random.choice(arm)
    return suspects, time_of_death, arm_use

suspects, time_of_death, arm_use = infos()

# função inicial, contexto do jogo
# função inicial, contexto do jogo
def start():
    global gamer
    print("\nEm meados de 1899, perto do fim das épocas de ouro do histórico velho-oeste...")
    print(
        f"\nXerife Arthur: Olá {gamer}. A polícia local está lutando para o fim das grandes gangues do faroeste na cidade de Imbituva – PR, "
        f"\nmas enfrenta uma das maiores do estado: a gangue Vanderlinde. Dutch é o líder da gangue, ele estava lutando para manter a paz entre os integrantes da gangue, "
        f"\nque estavam receosos pela ameaça. ")
    print(f"\nXerife Arthur: Em meio a este clima tenso entre os integrantes do grupo, enquanto o tempo passava na cidade na {time_of_death} de ontem, "
          f"\n,todos se preparavam para retomar suas atividades, {witness} encontrou o corpo sem vida de Dutch no acampamento.")
    print("\nXerife Arthur: Vou precisar da sua ajuda para encontrar o culpado!")
    print(f"\n\nAssim um novo mistério ataca a gangue Vanderlinde: ")
    print(f"--------------- Quem matou Dutch? ----------------")
    print("\nXerife Arthur: Os principais suspeitos são os integrantes da gangue: ")
    for name, description in suspects.items():
        print(f"{name}: {description}")

    print(
        f"\nEles suspeitam entre si, temos que encontrar o culpado antes que outra pessoa se machuque."
        f"\nXerife Arthur: Não sabemos nada sobre o assassinato, podemos começar o interrogatório com {witness}, que foi quem encontrou o corpo.\n"
    )

#ficha do caso para ser consultada durante o jogo
def case_sheet():
    global collection_clues
    global deductions_collection

    if 'time_of_death' not in globals() or 'arm_use' not in globals() or 'witness' not in globals():
        print("Erro: Variáveis do caso não estão definidas.")
        return

    victim = "Dutch, líder da gangue Vanderlinde"
    time_of_death_sheet = f"Hora da morte: {time_of_death}"
    death_cause = f"Causa da morte: {arm_use}"
    witness_sheet = f"Testemunha que encontrou o corpo: {witness}"

    print("\nO mistério de Imbituva: Quem matou Dutch?")
    print(f"Vítima: {victim}")
    print(time_of_death_sheet)
    print(death_cause)
    print(witness_sheet)

    if collection_clues:
        print("Pistas coletadas:")
        for chave, valor in collection_clues.items():
            print(f"{chave.capitalize()}: {valor}")

    else:
        print("Nenhuma pista coletada.")

    if deductions_collection:
        print("Deduções:")
        print("\n".join(deductions_collection))
    else:
        print("Nenhuma dedução disponível.")

    print("\nO que deseja fazer agora? ")
    print("1 - Fazer acusação")
    print("2 - Fechar ficha do caso")
    print("3 - Ver verificações de tabela verdade")

    ans = input("Digite uma opção: ")

    try:
        ans = int(ans)

        if ans == 1:
            make_acc()
        elif ans == 2:
            menu2()
        elif ans == 3:
            get_table_truth()
            final_valid()
        else:
            print("Xerife Arthur: Está louco?! Me ajude!")
            case_sheet()

    except ValueError:
        print("Xerife Arthur: Está louco?! Me ajude!")
        case_sheet()


# primeiro menu, após introdução
def menu1():
    global gamer
    print("\nO que deseja fazer?")
    print("1 - Interrogar testemunha")
    print("2 - Ver ficha do crime ")
    sus = list(suspects.keys())

    ans = input("Digite o número da opção escolhida: ")

    try:
        ans = int(ans)

        print("\n ")

        # caso seja interrogar testemunha, definição para casa caso de testemunha
        if ans == 1:
            if witness == "Micah":
                print(sus[0], ": Olá", gamer, pista_micah)
                menu2()

            elif witness == "Abigail":
                print(sus[1], ": Olá", gamer, pista_abigail)
                menu2()

            elif witness == "Lenny":
                print(sus[2], ": Olá", gamer, pista_lenny)
                menu2()

            elif witness == "Javier":
                print(sus[3], ": Olá", gamer, pista_javier)
                menu2()

            elif witness == "Bill":
                print(sus[4], ": Olá", gamer, pista_bill)
                menu2()

            elif witness == "Pearson":
                print(sus[5], ": Olá", gamer, pista_pearson)
                menu2()

            elif witness == "Sadie":
                print(sus[6], ": Olá", gamer, pista_sadie)
                menu2()

            elif witness == "Leopold":
                print(sus[7], ": Olá", gamer, pista_leopold)
                menu2()

            elif witness == "Doutor":
                print(sus[8], ": Olá", gamer, pista_doutor)
                menu2()

            elif witness == "Sally":
                print(sus[9], ": Olá", gamer, pista_sally)
                menu2()

        elif ans == 2:
            print(case_sheet())

        else:
            print(f"Opção inválida, escolha outra {gamer}")
            menu1()

    except ValueError:
        print("Entrada inválida, tente novamente.")
        menu1()


#menu do jogo
def menu2():
    global gamer
    pistas = {
        'micah': pista_micah,
        'abigail': pista_abigail,
        'lenny': pista_lenny,
        'javier': pista_javier,
        'bill': pista_bill,
        'pearson': pista_pearson,
        'sadie': pista_sadie,
        'leopold': pista_leopold,
        'doutor': pista_doutor,
        'sally': pista_sally,
    }

    print("\nXerife Arthur: Lembre-se que você pode fazer uma acusação a qualquer momento ao abrir a ficha do caso!")
    print("\nXerife Arthur: O que fazemos agora?")

    for i, suspect in enumerate(suspects.keys()):
        print(f"{i + 1} - Interrogar {suspect}")

    print("0 - Ver ficha do caso")

    ans = input("Digite o número da opção escolhida: ")

    try:
        ans = int(ans)

        if 1 <= ans <= len(suspects):
            suspect_name = list(suspects.keys())[ans - 1].lower()  # Converter para minúsculas
            pista = pistas.get(suspect_name)  # Buscar a pista

            if pista:
                print(f"\n{suspect_name.capitalize()}: Olá {gamer}. {pista}\n")
                process_clue(pista, suspect_name)  # Passar o nome em minúsculas
                menu2()
            else:
                print("Pista não encontrada.")
                menu2()

        elif ans == 0:
            case_sheet()

        else:
            print(f"Opção inválida, escolha outra {gamer}...")
            menu2()

    except ValueError:
        print("Entrada inválida, tente novamente.")
        menu2()


# definição do assassino de acordo com o período do assassinato
def get_murder_and_witness():
    suspects_list = list(suspects.keys())
    witness = random.choice(suspects_list)
    # ['Micah', 'Abigail', 'Lenny', 'Javier', 'Bill', 'Pearson', 'Sadie', 'Leopold', 'Doutor', 'Sally']
    #    0          1          2      3        4         5        6          7          8        9

    # manhã
    if time_of_death == "manhã":
        m = [suspects_list[0], suspects_list[1], suspects_list[3], suspects_list[6], suspects_list[5], suspects_list[9]]
        murder = random.choice(m)

    # tarde
    elif time_of_death == "tarde":
        m = [suspects_list[0], suspects_list[1], suspects_list[5], suspects_list[6]]
        murder = random.choice(m)

    # noite
    elif time_of_death == "noite":
        m = [suspects_list[0], suspects_list[2], suspects_list[3], suspects_list[4], suspects_list[5], suspects_list[6],
             suspects_list[7], suspects_list[8]]
        murder = random.choice(m)

    # madrugada
    elif time_of_death == "madrugada":
        m = [suspects_list[0], suspects_list[2], suspects_list[3], suspects_list[4], suspects_list[5], suspects_list[6],
             suspects_list[7], suspects_list[8]]
        murder = random.choice(m)

    return murder, witness


murder, witness = get_murder_and_witness()


# processamento das pistas em caso de assassino, alibi ou alibi sendo assassino
def clues(person, p2: str, peoples: List[str], p1: Optional[str] = None, p3: Optional[str] = None):
    if person == murder:
        if p1 is not None:
            pista = p1
        else:
            "Erro"

    elif murder in peoples:
        if p3 is not None:
            pista = p3
        else:
            "Erro"

    else:
        pista = p2
    return pista


# Definição de todas as dicas ods interrogatórios
def imp_clues():
    sus = list(suspects.keys())
    # clues(index do personagem,
    #       pista de alibi,
    #       pessoas citadas,
    #       pista se for assassino,
    #       pista se o alibi for o assassino, )

    # ['Micah', 'Abigail', 'Lenny', 'Javier', 'Bill', 'Pearson', 'Sadie', 'Leopold', 'Doutor', 'Sally']
    #    0          1          2      3        4         5        6          7          8        9

    # assassinato no período da manhã
    if time_of_death == "manhã":
        got_ded = []
        # 0 - micah
        pista_micah = clues(sus[0],
                            "Micah: Eu estava no acampamento tomando café com o Pearson e com o Leopold ",
                            # pista sendo alibi
                            ["Pearson", "Leopold"],  # pessoas citadas
                            "Micah: Eu não sei de nada",  # pista sendo assassino
                            "Micah: Eu tinha acabado de acordar e estava tomando café sozinho no hotel.",
                            # pista se o alibi for assassino
                            )

        # 1 - abigail
        pista_abigail = clues(sus[1],
                              "Não sei nada sobre isso, eu estava na fila do consultório esperando para ser atendida junto com Javier e Sally.",
                              # pista sendo alibi
                              ["Javier", "Sally"],  # pessoas citadas
                              "Não sei nada sobre isso, eu vi o Bill indo para o acampamento um pouco antes de encontrarem o corpo",
                              # pista sendo assassino
                              "Não sei nada sobre isso, eu estava sendo atendida pelo doutor no consultório no horário do assassinato."
                              # pista se o alibi for assassino
                              )

        # 2 - lenny
        pista_lenny = clues(sus[2],
                            "Não sei nada sobre o assassinato, eu estava com a Sadie na loja de armas ajudando-a a ajustar a mira de seu revólver",
                            # pista sendo alibi
                            ["Sadie", ],  # pessoas citadas
                            None,
                            "Não sei nada sobre o assassinato, eu estava trabalhando na loja de armas esse horário.",
                            # pista  do álibi sendo assassino
                            )

        # 3 - javier
        pista_javier = clues(sus[3],
                             "Não sei nada sobre isso, eu estava na fila do consultório esperando para ser atendida junto com Abigail e Sally",
                             # pista sendo alibi
                             ["Abigail", "Sally"],  # pessoas citadas
                             "Eu estava no estábulo esse horário... Lembro de ter visto Sadie com um comportamento estranho indo em direção ao acampamento.",
                             # pista sendo assassino
                             "Não sei nada sobre isso, estava no estábulo verificando os cavalos na hora do assassinato."
                             # pista do alibi sendo assassino
                             )

        # 4 - bill
        pista_bill = clues(sus[4],
                           "Eu estava trabalhando no banco esse horário, estava quase saindo para almoçar.",
                           # pista sendo alibi
                           ["  ", ],  # pessoas citadas
                           None,  # pista sendo assassino
                           None  # pista do alibi sendo assassino
                           )

        # 5 - Pearson
        pista_pearson = clues(sus[5],
                              "Eu estava com Micah e Leopold tomando café esse horário no acampamento. ",
                              # pista sendo alibi
                              ["Micah", "Leopold"],  # pessoas citadas
                              "Eu estava preparando, porém lembro de ter visto o Lenny caminhando. ",
                              # pista sendo assassino
                              "Eu estava tomando café da manhã sozinho no acampamento. "
                              # pista do alibi sendo assassino
                              )

        # 6 -  Sadie
        pista_sadie = clues(sus[6],
                            "Não sei nada sobre o assassinato, eu estava com o Lenny na loja de armas, ele estava me ajudando a ajustar a mira do revólver.",
                            # pista sendo alibi
                            ["Lenny", ],  # pessoas citadas
                            "Eu estava no teatro esse horário. Vi o doutor ir para o acampamento perto da hora da morte de Dutch. ",
                            # pista sendo assassino
                            None  # pista do alibi sendo assassino
                            )

        # 7 - Leopold
        pista_leopold = clues(sus[7],
                              "Eu estava tomando café com Pearson e Micah no acampamento. ",  # pista sendo alibi
                              ["Pearson", "Micah"],  # pessoas citadas
                              None,  # pista sendo assassino
                              "Eu estava trabalhando no hotel esse horário."  # pista do alibi sendo assassino
                              )

        # 8 - doutor
        pista_doutor = clues(sus[8],
                             " Eu estava atendendo esse horário, tinham muitas pessoas na fila de espera. Lembro de ter ouvido na rádio que o teatro estava interditado para reforma. ",
                             # pista sendo alibi
                             ["", ""],  # pessoas citadas
                             None,  # pista sendo assassino
                             None  # pista do alibi sendo assassino
                             )

        # 9 - Sally
        pista_sally = clues(sus[9],
                            "Não sei nada sobre isso, eu estava na fila do consultório esperando para ser atendida junto com Abigail e Javier",
                            # pista sendo alibi
                            ["Abigail", "Javier"],  # pessoas citadas
                            "Eu não sei nada sobre o assassinato, porém vi o Leopold em direção ao acampamento um pouco antes de encontrarem o corpo. ",
                            # pista sendo assassino
                            " Eu estava indo para o consultório esse horário."  # pista do alibi sendo assassino
                            )

    # assassinato no período da tarde
    elif time_of_death == "tarde":

        # 0 - micah
        pista_micah = clues(sus[0],
                            "Eu estava na loja de armas junto com o Lenny",  # pista sendo alibi
                            ["Lenny", ],  # pessoas citadas
                            "Eu estava saindo do banco esse horário, vi Abigail saindo do acampamento esse horário. ",
                            # pista sendo assassino
                            None,  # pista se o alibi for assassino
                            )

        # 1 - abigail
        pista_abigail = clues(sus[1],
                              "No horário da morte eu estava no banco tentando fazer um depósito para a conta da minha avó. Bill estava me ajudando, não acho que poderia ser ele.",
                              # pista sendo alibi
                              ["Javier", "Sally"],  # pessoas citadas
                              "No horário da morte eu estava no estábulo cuidando do meu cavalo que estava doente ",
                              # pista sendo assassino
                              None  # pista se o alibi for assassino
                              )

        # 2 - lenny
        pista_lenny = clues(sus[2],
                            "Eu estava trabalhando esse horário, não sei nada sobre o assassinato.",
                            # pista sendo alibi
                            ["", ],  # pessoas citadas
                            None,
                            None,  # pista  do álibi sendo assassino
                            )

        # 3 - javier
        pista_javier = clues(sus[3],
                             "Eu estava no estábulo trabalhando, foi um dia bem tranquilo, não vi ninguém por lá.",
                             # pista sendo alibi
                             ["", ""],  # pessoas citadas
                             None,  # pista sendo assassino
                             None  # pista do alibi sendo assassino
                             )

        # 4 - bill
        pista_bill = clues(sus[4],
                           "Esse horário eu estava ajudando a Abigail a fazer um depósito no banco, não vi mais ninguém durante esse horário.",
                           # pista sendo alibi
                           ["Abigail", ],  # pessoas citadas
                           None,  # pista sendo assassino
                           "Esse horário eu estava no banco, tinham algumas pessoas precisando da minha ajuda. "
                           # pista do alibi sendo assassino
                           )

        # 5 - Pearson
        pista_pearson = clues(sus[5],
                              "Eu tive que sair rapidamente para me consultar com o Doutor, pois estava com dor de cabeça.",
                              # pista sendo alibi
                              ["", ""],  # pessoas citadas
                              "Eu estava preparando a salada de frutas para o café da tarde. ",  # pista sendo assassino
                              None  # pista do alibi sendo assassino
                              )

        # 6 -  Sadie
        pista_sadie = clues(sus[6],
                            "Eu fui até o hotel fazer uma reserva para minha mãe que vem me visitar, falei com Leopold na recepção. ",
                            # pista sendo alibi
                            ["Leopold", ],  # pessoas citadas
                            "Lembro de ter visto o doutor indo ao acampamento esse horário, estava apressado. ",
                            # pista sendo assassino
                            None  # pista do alibi sendo assassino
                            )

        # 7 - Leopold
        pista_leopold = clues(sus[7],
                              "Encontrei com Sadie no hotel perto da hora da morte de Dutch, ela precisava conversar comigo para hospedar sua mãe que vinha visitar a cidade. ",
                              # pista sendo alibi
                              ["Sadie", ],  # pessoas citadas
                              None,  # pista sendo assassino
                              "Eu estava trabalhando no hotel esse horário, não posso deixar a recepção sozinha, estamos recebendo muitos turistas."
                              # pista do alibi sendo assassino
                              )

        # 8 - doutor
        pista_doutor = clues(sus[8],
                             " Encontrei com Pearson esse horário, ele veio se consultar porque estava com dor de cabeça.",
                             # pista sendo alibi
                             ["Pearson", ],  # pessoas citadas
                             None,  # pista sendo assassino
                             "Esse horário eu fui tomar café da tarde no acampamento, estava muito bom, porém não tinha nenhuma salada... Senti falta disso. "
                             # pista do alibi sendo assassino
                             )

        # 9 - Sally
        pista_sally = clues(sus[9],
                            "Não sei nada sobre isso, estava trabalhando e servindo bebidas na hora do assassinato. ",
                            # pista sendo alibi
                            ["", ],  # pessoas citadas
                            None,  # pista sendo assassino
                            None  # pista do alibi sendo assassino
                            )

    # assassinato sendo a noite
    elif time_of_death == "noite":

        # 0 - micah
        pista_micah = clues(sus[0],
                            "Eu estava com Leopold no bordel. ",  # pista sendo alibi
                            ["Leopold", ],  # pessoas citadas
                            "Não sei nada sobre isso, apenas lembro de ter visto Abigail caminhando perto do local da morte.",
                            # pista sendo assassino
                            "Eu estava no bordel assistindo a apresentação das bailarinas."
                            # pista se o alibi for assassino
                            )

        # 1 - abigail
        pista_abigail = clues(sus[1],
                              "Eu estava com Bill na hora do assassinato, no bordel.",  # pista sendo alibi
                              ["Bill", ],  # pessoas citadas
                              None,  # pista sendo assassino
                              "Eu estava dançando no bordel na hora do assassinato. Não vi Bill lá. "
                              # pista se o alibi for assassino
                              )

        # 2 - lenny
        pista_lenny = clues(sus[2],
                            "Fui ao Saloon quando escureceu esse dia, Sally pode confirmar, estava numa disputa de quem bebia mais. ",
                            # pista sendo alibi
                            ["", ],  # pessoas citadas
                            "Eu fui assistir uma peça de teatro essa noite, eu vi o Pearson no acampamento pouco antes do assassinato e ele parecia estressado. ",
                            # pista sendo assassino
                            None,  # pista  do álibi sendo assassino
                            )

        # 3 - javier
        pista_javier = clues(sus[3],
                             "Eu estava me preparando para ir ao teatro assistir uma peça, mas ela foi cancelada e eu tive que avisar o Doutor, que ia comigo. ",
                             # pista sendo alibi
                             ["Doutor", ],  # pessoas citadas
                             "Estava no teatro para assistir uma peça. ",  # pista sendo assassino
                             "Eu estava me preparando para ir ao teatro assistir uma peça, mas ela foi cancelada."
                             # pista do alibi sendo assassino
                             )

        # 4 - bill
        pista_bill = clues(sus[4],
                           "Eu estava com Abigail no bordel na hora do assassinato. ",  # pista sendo alibi
                           ["Abigail", ],  # pessoas citadas
                           "Estava com Abigail no bordel na hora do assassinato.",  # pista sendo assassino
                           None  # pista do alibi sendo assassino
                           )

        # 5 - Pearson
        pista_pearson = clues(sus[5],
                              "Eu estava conversando com Sadie sobre o jantar no acampamento, eu estava com muita raiva com todos perguntando sobre o cardápio do jantar. ",
                              # pista sendo alibi
                              ["Sadie", ],  # pessoas citadas
                              "Eu estava no teatro, assistindo uma peça ",  # pista sendo assassino
                              "Eu estava dormindo, não sei o que aconteceu. "  # pista do alibi sendo assassino
                              )

        # 6 -  Sadie
        pista_sadie = clues(sus[6],
                            "Estava no acampamento conversando com Pearson sobre o jantar, ele me disse que estava estressado porque estava com muita gente perguntando sobre o cardápio.  ",
                            # pista sendo alibi
                            ["Pearson", ],  # pessoas citadas
                            "Eu estava com o Leopold no hotel.",  # pista sendo assassino
                            "Estava no acampamento, fui falar com Pearson mas não encontrei ele."
                            # pista do alibi sendo assassino
                            )

        # 7 - Leopold
        pista_leopold = clues(sus[7],
                              "Eu estava com Micah no bordel na hora do assassinato.",  # pista sendo alibi
                              ["Micah", ],  # pessoas citadas
                              "Eu estava indo ao teatro para assistir a uma peça, não vi nada estranho.",
                              # pista sendo assassino
                              "Eu estava no bordel assistindo a apresentação das dançarinas."
                              # pista do alibi sendo assassino
                              )

        # 8 - doutor
        pista_doutor = clues(sus[8],
                             "Eu estava me preparando para ir ao teatro assistir uma peça, mas ela foi cancelada e eu tive que avisar o Javier, que ia comigo.",
                             # pista sendo alibi
                             ["Javier", ],  # pessoas citadas
                             "Eu vi a Abigail caminhando em direção ao acampamento esse horário, estava com um comportamento suspeito, mas não consegui falar com ela. ",
                             # pista sendo assassino
                             "Eu estava me preparando para ir ao teatro assistir uma peça, mas ela foi cancelada."
                             # pista do alibi sendo assassino
                             )

        # 9 - Sally
        pista_sally = clues(sus[9],
                            "Não sei nada sobre, estava trabalhando e servindo bebidas no Saloon.  ",
                            # pista sendo alibi
                            ["", ],  # pessoas citadas
                            None,  # pista sendo assassino
                            None  # pista do alibi sendo assassino
                            )


    # se o assassinato for de madrugada
    elif time_of_death == "madrugada":

        # 0 - micah
        pista_micah = clues(sus[0],
                            "Eu estava no hotel dormindo esse horário. ",  # pista sendo alibi
                            ["", ],  # pessoas citadas
                            "Estava no Saloon bebendo com Doutor.",  # pista sendo assassino
                            None  # pista se o alibi for assassino
                            )

        # 1 - abigail
        pista_abigail = clues(sus[1],
                              "Eu estava com Javier na hora do assassinato, no bordel.",  # pista sendo alibi
                              ["Javier", ],  # pessoas citadas
                              None,  # pista sendo assassino
                              "Eu estava com Pearson no bordel na hora do assassinato. Não vi Javier por lá. "
                              # pista se o alibi for assassino
                              )

        # 2 - lenny
        pista_lenny = clues(sus[2],
                            "Eu estava no hotel dormindo essa madrugada, encontrei com Leopold no meio da noite, quando me levantei para beber água. ",
                            # pista sendo alibi
                            ["Leopold", ],  # pessoas citadas
                            "Não fiquei sabendo de nada sobre isso, eu estava no hotel, pouco antes da hora da morte do Dutch eu vi o Pearson indo em direção ao acampamento. ",
                            # pista sendo assassino
                            "Eu estava no hotel dormindo essa madrugada, encontrei com Leopold no meio da noite perto do corredor de entrada do hotel",
                            # pista  do álibi sendo assassino
                            )

        # 3 - javier
        pista_javier = clues(sus[3],
                             "Eu estava com Abigail no bordel na hora do assassinato. ",  # pista sendo alibi
                             ["Abigail", ],  # pessoas citadas
                             "Eu estava no bordel essa noite.",  # pista sendo assassino
                             None  # pista do alibi sendo assassino
                             )

        # 4 - bill
        pista_bill = clues(sus[4],
                           "Dei um ‘boa noite’ para o Leopold e fui dormir. ",  # pista sendo alibi
                           ["Leopold", ],  # pessoas citadas
                           "Não sei nada sobre o assassinato, estava com o Leopold no hotel.",  # pista sendo assassino
                           "Não sei de nada, estava dormindo tranquilamente. "  # pista do alibi sendo assassino
                           )

        # 5 - Pearson
        pista_pearson = clues(sus[5],
                              "Eu estava no Bordel na hora do assassinato.",  # pista sendo alibi
                              ["", ],  # pessoas citadas
                              "Eu estava me preparando para dormir, porém vi o Doutor caminhando de uma forma estranha.",
                              # pista sendo assassino
                              None  # pista do alibi sendo assassino
                              )

        # 6 -  Sadie
        pista_sadie = clues(sus[6],
                            "Estava no Saloon disputando quem bebia mais com o Doutor. ",  # pista sendo alibi
                            ["Doutor", ],  # pessoas citadas
                            "Eu estava no Saloon, vi Pearson indo em direção ao acampamento pouco antes da morte de Dutch.",
                            # pista sendo assassino
                            "Eu estava no Saloon bebendo. Não vi o doutor por lá. "  # pista do alibi sendo assassino
                            )

        # 7 - Leopold
        pista_leopold = clues(sus[7],
                              "Eu estava no hotel essa noite, preciso dar suporte aos hóspedes que precisam. Encontrei com Lenny em um momento, enquanto verificava os corredores do hotel. Também lembro de ter dado boa noite ao Bill. ",
                              # pista sendo alibi
                              ["Lenny", "Bill"],  # pessoas citadas
                              "Eu estava no hotel dormindo essa noite, dormi como um anjo. ",  # pista sendo assassino
                              "Eu estava no hotel essa noite, não sei nada sobre isso."
                              # pista do alibi sendo assassino
                              )

        # 8 - doutor
        pista_doutor = clues(sus[8],
                             "Estava no Saloon disputando quem bebia mais com a Sadie, não vi mais ninguém. ",
                             # pista sendo alibi
                             ["Javier", ],  # pessoas citadas
                             "Antes de encontrarem o corpo, vi a Sally indo para o acampamento esse horário, achei suspeito. ",
                             # pista sendo assassino
                             "Estava no Saloon esse horário, não vi nada de errado por lá."
                             # pista do alibi sendo assassino
                             )

        # 9 - Sally
        pista_sally = clues(sus[9],
                            "Estava trabalhando, servindo bebidas somente para o Doutor e para a Sadie.",
                            # pista sendo alibi
                            ["Doutor", "Sadie"],  # pessoas citadas
                            None,  # pista sendo assassino
                            "Estava trabalhando e servindo bebidas para pessoas no Saloom"
                            # pista do alibi sendo assassino
                            )

    return pista_micah, pista_abigail, pista_lenny, pista_javier, pista_bill, pista_pearson, pista_sadie, pista_leopold, pista_doutor, pista_sally


pista_micah, pista_abigail, pista_lenny, pista_javier, pista_bill, pista_pearson, pista_sadie, pista_leopold, pista_doutor, pista_sally = imp_clues()



def deductions():
    abigail_validation = None
    bill_validation = None
    doutor_validation = None
    javier_validation = None
    lenny_validation = None
    leopold_validation = None
    micah_validation = None
    pearson_validation  = None
    sadie_validation = None
    sally_validation = None

# se for de manhã - OK
    if time_of_death == "manhã":
        # se a abigail for assassina
        if murder == "Abigail":
            # B  ~A	(F)
            abigail_validation = ttg.Truths(["Abigail viu o Bill indo para o acampamento antes de encontraram o corpo",
                                                   "Bill estava trabalhando"],
                                            ["Bill estava trabalhando => not  Abigail viu o Bill indo para o acampamento antes de encontraram o corpo"],
                                                    ints=False)

            bill_validation =  ttg.Truths(["Possui álibi"], ["Possui Álibi"], ints=False)
            doutor_validation = ttg.Truths(["Possui álibi"], ["Possui Álibi"], ints=False)
            sally_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            javier_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

            # o	Lenny sendo álibi
            # C = "Lenny estava com Sadie na loja de arma"
            # D = "Sadie estava na loja de armas com Lenny"
            #C  D		(V)
            lenny_validation = ttg.Truths(["Lenny estava com Sadie na loja de arma",
                                                 "Sadie estava na loja de armas com Lenny"],
                                          ["Lenny estava com Sadie na loja de arma => Sadie estava na loja de armas com Lenny"], ints=False)

            # o	Pearson sendo álibi
            # G = "Pearson estava com Micah e Leopold no hotel"
            # H = "Micah estava com Pearson e Leopold no hotel"
            # I = "Leopold estava com Pearson e Micah no hotel"
            # G ^ H ^ I		(V)
            pearson_validation = ttg.Truths(["Pearson estava com Micah e Leopold no hotel",
                                             "Micah estava com Pearson e Leopold no hotel",
                                             "Leopold estava com Pearson e Micah no hotel"],
                                            ["Pearson estava com Micah e Leopold no hotel and Micah estava com Pearson e Leopold no hotel and Leopold estava com Pearson e Micah no hotel"],
                                            ints=False
                                        )

            micah_validation = ttg.Truths(
                                    ["Pearson estava com Micah e Leopold no hotel",
                                         "Micah estava com Pearson e Leopold no hotel",
                                         "Leopold estava com Pearson e Micah no hotel"],
                                 ["Pearson estava com Micah e Leopold no hotel and Micah estava com Pearson e Leopold no hotel and Leopold estava com Pearson e Micah no hotel"],
                                        ints=False
                                            )

            leopold_validation = ttg.Truths( ["Pearson estava com Micah e Leopold no hotel",
                                             "Micah estava com Pearson e Leopold no hotel",
                                             "Leopold estava com Pearson e Micah no hotel"],
                                      ["Pearson estava com Micah e Leopold no hotel and Micah estava com Pearson e Leopold no hotel and Leopold estava com Pearson e Micah no hotel"],
                                            ints=False                                        )

            # o	Sadie sendo álibi
            # J = "Sadie estava na loja de armas com Lenny"
            # K = "Lenny estava com Sadie na loja de arma"
            #K  J		(V)
            sadie_validation = ttg.Truths(["Sadie estava na loja de armas com Lenny", "Lenny estava com Sadie na loja de arma"],
                                           ["Lenny estava com Sadie na loja de arma => Sadie estava na loja de armas com Lenny"],
                                           ints=False)

        # Javier sendo assassino
        elif murder == "Javier":
            # A = "Javier estava no estábulo"
            # B = "Javier viu Sadie ir para o acampamento"
            # C = "Sadie estava com Lenny na loja de armas"
            # D = "Lenny estava trabalhando na loja de armas ajudando Sadie"
            # E = "Javier não trabalha de manhã (informação oculta)"
            # (C ^ D) ^ E  ¬A ^ ¬B    (F)
            javier_validation = ttg.Truths(["Javier estava no estábulo",
                                                  "Javier viu Sadie ir para o acampamento",
                                                   "Sadie estava com Lenny na loja de armas",
                                                    "Lenny estava trabalhando na loja de armas ajudando Sadie",
                                                    "Javier não trabalha de manhã (informação oculta)"],
                                           ["Sadie estava com Lenny na loja de armas and Lenny estava trabalhando na loja de armas ajudando Sadie and Javier não trabalha de manhã (informação oculta) => not Javier estava no estábul and not Javier vLenny estava trabalhando na loja de armas ajudando Sadieu Sadie ir para o acampamento"], ints=False)

            bill_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            doutor_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            sally_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

            # Abigail sendo álibi
            # F = "Abigail estava no consultório com o doutor"
            # G = "Doutor estava atendendo esse horário (informação oculta)"
            #G  F(V)
            abigail_validation = ttg.Truths(["Abigail estava no consultório com o doutor",
                                             "Doutor estava atendendo esse horário (informação oculta)"], [
                "Doutor estava atendendo esse horário (informação oculta) => Abigail estava no consultório com o doutor "], ints=False)

            # Lenny sendo álibi
            # D = "Lenny estava trabalhando na loja de armas ajudando Sadie"
            # C = "Sadie estava na loja de armas com Lenny"
            #C  D(V)
            lenny_validation = ttg.Truths(["Sadie estava na loja de armas com Lenny",
                                           "Lenny estava trabalhando na loja de armas ajudando Sadie"], ["Sadie estava na loja de armas com Lenny=>Lenny estava trabalhando na loja de armas ajudando Sadie"], ints=False)
            sadie_validation = ttg.Truths(["Lenny estava trabalhando na loja de armas ajudando Sadie", "Sadie estava na loja de armas com Lenny"], ["Lenny estava trabalhando na loja de armas ajudando SadieD=>C"], ints=False)

            # Pearson sendo álibi
            # I = "Pearson estava com Micah e Leopold no hotel"
            # J = "Micah estava com Pearson e Leopold no hotel"
            # K = "Leopold estava com Pearson e Micah no hotel"
            #I ^ J  K(V)
            pearson_validation =  ttg.Truths(["Pearson estava com Micah e Leopold no hotel",
                                              "Micah estava com Pearson e Leopold no hotel",
                                              "Leopold estava com Pearson e Micah no ho"],
                                             ["Pearson estava com Micah e Leopold no hotel and Micah estava com Pearson e Leopold no hote => Micah estava com Pearson e Leopold no hote"], ints=False)
            micah_validation = ttg.Truths(["Pearson estava com Micah e Leopold no hotel",
                                           "Micah estava com Pearson e Leopold no hotel",
                                           "Leopold estava com Pearson e Micah no ho"],
                                          ["Pearson estava com Micah e Leopold no hotel and Micah estava com Pearson e Leopold no hotel => Micah estava com Pearson e Leopold no hotel"], ints=False)
            leopold_validation = ttg.Truths(["Pearson estava com Micah e Leopold no hotel",
                                             "Micah estava com Pearson e Leopold no hotel",
                                             "Leopold estava com Pearson e Micah no ho"],
                                            ["Pearson estava com Micah e Leopold no hotel and Micah estava com Pearson e Leopold no hotel => Micah estava com Pearson e Leopold no hotel"], ints=False)

        # Pearson sendo assassino
        elif murder == "Pearson":
            #A = "Pearson estava cozinhando e viu Lenny no acampamento"
            #B = "Lenny estava na loja de armas com Sadie"
            #C = "Sadie estava na loja de armas com Lenny"
            # C ^ B  ¬A		(F)
            pearson_validation = ttg.Truths(["Pearson estava cozinhando e viu Lenny no acampamento",
                                             "Lenny estava na loja de armas com Sadie",
                                             "Sadie estava na loja de armas com Lenny"],
                                            ["Sadie estava na loja de armas com Lenny and Lenny estava na loja de armas com Sadie => not Pearson estava cozinhando e viu Lenny no acampamento"], ints=False)

            bill_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            doutor_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

            # Abigail sendo álibi
            #D = "Javier estava no consultório junto de Abigail e Sally"
            #E = "Abigail estava no consultório junto de Javier e Sally"
            #F = "Sally estava no consultório junto de Javier e Abigail"
            # D ^ F  E		(V)
            abigail_validation = ttg.Truths(["Javier estava no consultório junto de Abigail e Sally",
                                             "Abigail estava no consultório junto de Javier e Sally",
                                             "Sally estava no consultório junto de Javier e Abigail"],
                                            ["Javier estava no consultório junto de Abigail e Sally and Sally estava no consultório junto de Javier e Abigail => Abigail estava no consultório junto de Javier e Sally"], ints=False)
            javier_validation = ttg.Truths(["Javier estava no consultório junto de Abigail e Sally",
                                            "Abigail estava no consultório junto de Javier e Sally",
                                            "Sally estava no consultório junto de Javier e Abigail"], ["Javier estava no consultório junto de Abigail e Sally and Sally estava no consultório junto de Javier e Abigail => Abigail estava no consultório junto de Javier e Sally"], ints=False)
            sally_validation = ttg.Truths(["Javier estava no consultório junto de Abigail e Sally",
                                           "Abigail estava no consultório junto de Javier e Sally",
                                           "Sally estava no consultório junto de Javier e Abigail"], ["Javier estava no consultório junto de Abigail e Sally and Sally estava no consultório junto de Javier e Abigail => Abigail estava no consultório junto de Javier e Sally"], ints=False)

            # Lenny sendo álibi
            # B = "Lenny estava na loja de armas com Sadie"
            # C = "Sadie estava na loja de armas com Lenny"
            # C  B		(V)
            lenny_validation = ttg.Truths(["Lenny estava na loja de armas com Sadie",
                                           "Sadie estava na loja de armas com Lenny"], ["Sadie estava na loja de armas com Lenny => Lenny estava na loja de armas com Sadie"], ints=False)
            sadie_validation = ttg.Truths(["Lenny estava na loja de armas com Sadie",
                                           "Sadie estava na loja de armas com Lenny"], ["Sadie estava na loja de armas com Lenny => Lenny estava na loja de armas com Sadie"], ints=False)

            # Leopold sendo álibi
            # H = "Leopold estava com Micah no hotel"
            # I = "Micah estava com Leopold no hotel"
            # I  H		(V)
            leopold_validation = ttg.Truths(["Leopold estava com Micah no hotel",
                                             "Micah estava com Leopold no hotel"],
                                            ["Micah estava com Leopold no hotel => Leopold estava com Micah no hotel"], ints=False)
            micah_validation = ttg.Truths(["Leopold estava com Micah no hotel",
                                           "Micah estava com Leopold no hotel"],
                                          ["Micah estava com Leopold no hotel => Leopold estava com Micah no hotel"], ints=False)

        # Sadie sendo assassina
        elif murder == "Sadie":
            # A = "Sadie estava no teatro e viu o doutor indo para o acampamento"
            # B = "Doutor estava trabalhando nesse horário, e viu no jornal que o teatro estava interditado para reforma"
            # # B  ¬A		(F)
            sadie_validation = ttg.Truths(["Sadie estava no teatro e viu o doutor indo para o acampamento",
                                           "Doutor estava trabalhando nesse horário, e viu no jornal que o teatro estava interditado para reforma"],
                                          ["Doutor estava trabalhando nesse horário, e viu no jornal que o teatro estava interditado para reforma => not Sadie estava no teatro e viu o doutor indo para o acampamento"], ints=False)

            bill_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            doutor_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            lenny_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

            # Abigail sendo álibi
            # C = "Abigail estava no consultório junto com Javier e Sally"
            # D = "Javier estava no consultório junto com Abigail e Sally"
            # E = "Sally estava no consultório junto com Abigail e Javier"
            # D ^ E  C		(V)
            abigail_validation = ttg.Truths(["Abigail estava no consultório junto com Javier e Sally",
                                             "Javier estava no consultório junto com Abigail e Sally",
                                             "Sally estava no consultório junto com Abigail e Javier"],
                                            ["Javier estava no consultório junto com Abigail e Sally and Sally estava no consultório junto com Abigail e Javier => Abigail estava no consultório junto com Javier e Sally"], ints=False)
            javier_validation = ttg.Truths(["Abigail estava no consultório junto com Javier e Sally",
                                            "Javier estava no consultório junto com Abigail e Sally",
                                            "Sally estava no consultório junto com Abigail e Javier"],
                                            ["Javier estava no consultório junto com Abigail e Sally and Sally estava no consultório junto com Abigail e Javier => Abigail estava no consultório junto com Javier e Sally"], ints=False)
            sally_validation = ttg.Truths(["Abigail estava no consultório junto com Javier e Sally",
                                           "Javier estava no consultório junto com Abigail e Sally",
                                           "Sally estava no consultório junto com Abigail e Javier"],
                                           ["Javier estava no consultório junto com Abigail e Sally and Sally estava no consultório junto com Abigail e Javier => Abigail estava no consultório junto com Javier e Sally"], ints=False)


            # Pearson sendo álibi
            # H = "Pearson estava com Leopold e Micah no acampamento."
            # I = "Leopold estava com Pearson e Micah no acampamento."
            # J = "Micah estava com Pearson e Leopold no acampamento."
            # J ^ I  H		(V)
            pearson_validation = ttg.Truths(["Pearson estava com Leopold e Micah no acampamento.",
                                             "Leopold estava com Pearson e Micah no acampamento.",
                                             "Micah estava com Pearson e Leopold no acampamento."],
                                            ["Micah estava com Pearson e Leopold no acampamento. and Leopold estava com Pearson e Micah no acampamento. => Pearson estava com Leopold e Micah no acampamento."], ints=False)
            leopold_validation = ttg.Truths(["Pearson estava com Leopold e Micah no acampamento.",
                                             "Leopold estava com Pearson e Micah no acampamento.",
                                             "Micah estava com Pearson e Leopold no acampamento."],
                                            ["Micah estava com Pearson e Leopold no acampamento. and Leopold estava com Pearson e Micah no acampamento. => Pearson estava com Leopold e Micah no acampamento."], ints=False)
            micah_validation = ttg.Truths(["Pearson estava com Leopold e Micah no acampamento.",
                                           "Leopold estava com Pearson e Micah no acampamento.",
                                           "Micah estava com Pearson e Leopold no acampamento."],
                                          ["Micah estava com Pearson e Leopold no acampamento. and Leopold estava com Pearson e Micah no acampamento. => Pearson estava com Leopold e Micah no acampamento."], ints=False)

        # Sally sendo assassina
        elif murder == "Sally":
            # A = "Sally viu o Leopold em direção ao acampamento"
            # B = "Leopold estava com Pearson e Micah no acampamento"
            # C = "Pearson estava com Micah e Leopold no acampamento"
            # D = "Micah estava com Leopold e Pearson no acampamento"
            # B ^ C ^ D  ¬A		(F)
            sally_validation = ttg.Truths(["Sally viu o Leopold em direção ao acampamento",
                                           "Leopold estava com Pearson e Micah no acampamento",
                                           "Pearson estava com Micah e Leopold no acampamento",
                                           "Micah estava com Leopold e Pearson no acampamento"],
                                          ["Leopold estava com Pearson e Micah no acampamento and Pearson estava com Micah e Leopold no acampamento and Micah estava com Leopold e Pearson no acampamento => not Sally viu o Leopold em direção ao acampamento"], ints=False)

            bill_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            doutor_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            javier_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

            # Abigail sendo álibi
            # E = "Abigail estava sendo atendida pelo doutor"
            # F = "Doutor estava atendendo esse horário"
            # F  E		(V)
            abigail_validation = ttg.Truths(["Abigail estava sendo atendida pelo doutor", "Doutor estava atendendo esse horário"],
                                            ["Doutor estava atendendo esse horário => Abigail estava sendo atendida pelo doutor"], ints=False)

            # Lenny sendo álibi
            # G = "Lenny estava com Sadie na loja de arma"
            # H = "Sadie estava com o Lenny na loja de armas"
            # H  G		(V)
            lenny_validation = ttg.Truths(["Lenny estava com Sadie na loja de armas",
                                           "Sadie estava com o Lenny na loja de armas"],
                                          ["Sadie estava com o Lenny na loja de armas => Lenny estava com Sadie na loja de armas"], ints=False)
            sadie_validation = ttg.Truths(["Lenny estava com Sadie na loja de armas",
                                           "Sadie estava com o Lenny na loja de armas"],
                                          ["Sadie estava com o Lenny na loja de armas => Lenny estava com Sadie na loja de armas"], ints=False)

            # Pearson sendo álibi
            # C = "Pearson estava com Micah e Leopold no acampamento"
            # B = "Leopold estava com Pearson e Micah no acampamento"
            # D = "Micah estava com Leopold e Pearson no acampamento"
            # B ^ D  C		(V)
            pearson_validation = ttg.Truths(["Pearson estava com Micah e Leopold no acampamento",
                                             "Pearson estava com Micah e Leopold no acampamento",
                                             "Micah estava com Leopold e Pearson no acampamento"], ["Pearson estava com Micah e Leopold no acampamento and Micah estava com Leopold e Pearson no acampamento => Pearson estava com Micah e Leopold no acampamento"], ints=False)
            leopold_validation = ttg.Truths(["Pearson estava com Micah e Leopold no acampamento",
                                             "Pearson estava com Micah e Leopold no acampamento",
                                             "Micah estava com Leopold e Pearson no acampamento"], ["Pearson estava com Micah e Leopold no acampamento and Micah estava com Leopold e Pearson no acampamento => Pearson estava com Micah e Leopold no acampamento"], ints=False)
            micah_validation = ttg.Truths(["Pearson estava com Micah e Leopold no acampamento",
                                           "Pearson estava com Micah e Leopold no acampamento",
                                           "Micah estava com Leopold e Pearson no acampamento"], ["Pearson estava com Micah e Leopold no acampamento and Micah estava com Leopold e Pearson no acampamento => Pearson estava com Micah e Leopold no acampamento"], ints=False)

        # Micah sendo assassino
        elif murder == "Micah":
            # A = "Micah tinha acabado de acordar e avistou Javier pela janela."
            # B = "Javier estava na fila do consultório junto com Abigail e Sally"
            # C = "Abigail estava na fila do consultório junto com Javier e Sally"
            # D = "Sally estava na fila do consultório junto com Abigail e Javier"
            # B ^ C ^ D  ¬A		(F)
            micah_validation = ttg.Truths(["Micah tinha acabado de acordar e avistou Javier pela janela.",
                                           "avier estava na fila do consultório junto com Abigail e Sally",
                                           "Abigail estava na fila do consultório junto com Javier e Sally",
                                           "Sally estava na fila do consultório junto com Abigail e Javier"],
                                          ["avier estava na fila do consultório junto com Abigail e Sally and Abigail estava na fila do consultório junto com Javier e Sally and Sally estava na fila do consultório junto com Abigail e Javier => not Micah tinha acabado de acordar e avistou Javier pela janela."], ints=False)

            bill_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            doutor_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            pearson_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            leopold_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

            # Abigail sendo álibi
            # C = "Abigail estava na fila do consultório junto com Javier e Sally"
            # B = "Javier estava na fila do consultório junto com Abigail e Sally"
            # D = "Sally estava na fila do consultório junto com Abigail e Javier"
            # D ^ B  C		(V)
            abigail_validation = ttg.Truths(["Abigail estava na fila do consultório junto com Javier e Sally",
                                             "Abigail estava na fila do consultório junto com Javier e Sally",
                                             "Sally estava na fila do consultório junto com Abigail e Javier"], ["Sally estava na fila do consultório junto com Abigail e Javier and Javier estava na fila do consultório junto com Abigail e Sally => Abigail estava na fila do consultório junto com Javier e Sally"], ints=False)
            javier_validation = ttg.Truths(["Abigail estava na fila do consultório junto com Javier e Sally",
                                            "Javier estava na fila do consultório junto com Abigail e Sally",
                                            "Sally estava na fila do consultório junto com Abigail e Javier"], ["Sally estava na fila do consultório junto com Abigail e Javier and Javier estava na fila do consultório junto com Abigail e Sally => Abigail estava na fila do consultório junto com Javier e Sally"], ints=False)
            sally_validation = ttg.Truths(["Abigail estava na fila do consultório junto com Javier e Sally",
                                           "Javier estava na fila do consultório junto com Abigail e Sally",
                                           "Sally estava na fila do consultório junto com Abigail e Javier"], ["Sally estava na fila do consultório junto com Abigail e Javier and Javier estava na fila do consultório junto com Abigail e Sally => Abigail estava na fila do consultório junto com Javier e Sally"], ints=False)

            # Lenny sendo álibi
            # E = "Lenny estava com Sadie na loja de armas"
            # F = "Sadie estava com Lenny na loja de armas"
            # F  E		(V)
            lenny_validation = ttg.Truths(["Lenny estava com Sadie na loja de armas", "adie estava com Lenny na loja de armas"], ["adie estava com Lenny na loja de armas => Lenny estava com Sadie na loja de armas"], ints=False)
            sadie_validation = ttg.Truths(["Lenny estava com Sadie na loja de armas", "adie estava com Lenny na loja de armas"], ["Lenny estava com Sadie na loja de armas => adie estava com Lenny na loja de armas"], ints=False)

# se for de tarde - OK
    elif time_of_death == "tarde":

        #abigail sendo assassina
        if murder == "Abigail":
            # A = "Abigail estava no estábulo"
            # B = "Javier estava trabalhando e não viu ninguém"
            # B  ¬A		(F)
            abigail_validation = ttg.Truths(["Abigail estava no estábulo", "Abigail estava no estábulo"],
                                            ["Abigail estava no estábulo => not Abigail estava no estábulo"], ints=False)

            bill_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            doutor_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            javier_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            lenny_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            sally_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            pearson_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

            # Sadie sendo álibi
            # G = "Sadie estava com Leopold no hotel"
            # H = "Leopold estava com Sadie no hotel"
            # H  G		(V)
            sadie_validation = ttg.Truths(["Sadie estava com Leopold no hotel"
                                           "Leopold estava com Sadie no hotel"], ["Leopold estava com Sadie no hotel => Sadie estava com Leopold no hotel"], ints=False)
            leopold_validation = ttg.Truths(["Sadie estava com Leopold no hotel",
                                             "Leopold estava com Sadie no hotel"], ["Sadie estava com Leopold no hotel => Leopold estava com Sadie no hotel"], ints=False)

            # Micah sendo álibi
            # K = "Micah estava na loja de armas"
            # L = "Lenny viu Micah na loja de armas"
            # L  K		(V)
            micah_validation = ttg.Truths(["Micah estava na loja de armas",
                                           "Lenny viu Micah na loja de armas"],
                                           ["Lenny viu Micah na loja de armas => Micah estava na loja de armas"], ints=False)

        # Pearson sendo assassino
        elif murder == "Pearson":
            # A = "Pearson estava no acampamento fazendo salada de frutas"
            # B = "Doutor estava no acampamento e não tinha salada de frutas"
            # B  ¬A		(F)
            pearson_validation = ttg.Truths(["Pearson estava no acampamento fazendo salada de frutas",
                                             "Doutor estava no acampamento e não tinha salada de frutas"], ["Doutor estava no acampamento e não tinha salada de frutas => not Pearson estava no acampamento fazendo salada de frutas"], ints=False)

            javier_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            lenny_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            sally_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            doutor_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

            # Abigail sendo álibi
            # C = "Abigail estava com Bill no banco"
            # D = "Bill estava no banco com Abigail"
            # D  C		(V)
            abigail_validation = ttg.Truths(["Abigail estava com Bill no banco", "Bill estava no banco com Abigail"],
                                            ["Bill estava no banco com Abigail => Abigail estava com Bill no banco"], ints=False)
            bill_validation = ttg.Truths(["Abigail estava com Bill no banco", "Bill estava no banco com Abigail"],
                                         ["Abigail estava com Bill no banco => Bill estava no banco com Abigail"], ints=False)

            # Sadie sendo álibi
            # G = "Sadie estava com Leopold no hotel"
            # H = "Leopold estava com Sadie no hotel"
            # H  G		(V)
            sadie_validation = ttg.Truths(["Sadie estava com Leopold no hotel",
                                           "Leopold estava com Sadie no hotel"], ["Leopold estava com Sadie no hotel => Sadie estava com Leopold no hotel"], ints=False)
            leopold_validation = ttg.Truths(["Sadie estava com Leopold no hotel",
                                             "Leopold estava com Sadie no hotel"], ["Sadie estava com Leopold no hotel => Leopold estava com Sadie no hotel"], ints=False)

            # Micah sendo álibi
            # K = "Micah estava na loja de armas com Lenny"
            # L = "Lenny viu Micah na loja de armas"
            # L  K		(V)
            micah_validation = ttg.Truths(["Micah estava na loja de armas com Lenny",
                                           "Lenny viu Micah na loja de armas"], ["Lenny viu Micah na loja de armas => Micah estava na loja de armas com Lenny"], ints=False)

        # Sadie sendo assassina
        elif murder == "Sadie":
            # A = "Sadie viu o Doutor no acampamento"
            # B = "Doutor estava trabalhando no consultório"
            # B  ¬A		(F)
            sadie_validation = ttg.Truths(["Sadie viu o Doutor no acampamento", "Doutor estava trabalhando no consultório"], ["Doutor estava trabalhando no consultório => not Sadie viu o Doutor no acampamento"], ints=False)

            javier_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            lenny_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            leopold_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            sally_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

            # Abigail sendo álibi
            # C = "Abigail estava com Bill no banco"
            # D = "Bill estava no banco com Abigail"
            # D  C		(V)
            abigail_validation = ttg.Truths(["Abigail estava com Bill no banco",
                                             "Bill estava no banco com Abigail"],
                                            ["Bill estava no banco com Abigail => Abigail estava com Bill no banco"], ints=False)
            bill_validation = ttg.Truths(["Abigail estava com Bill no banco",
                                          "Bill estava no banco com Abigail"],
                                         ["Abigail estava com Bill no banco => Bill estava no banco com Abigail"], ints=False)

            # Pearson sendo álibi
            # G = "Pearson estava no consultório médico"
            # H = "Doutor estava com Pearson no consultório"
            # H  G		(V)
            pearson_validation = ttg.Truths(["Pearson estava no consultório médico",
                                             "Doutor estava com Pearson no consultório"],
                                            ["Doutor estava com Pearson no consultório => Pearson estava no consultório médico"], ints=False)
            doutor_validation = ttg.Truths(["Pearson estava no consultório médico",
                                            "Doutor estava com Pearson no consultório"],
                                           ["Pearson estava no consultório médicPearson estava no consultório médico => Doutor estava com Pearson no consultório"], ints=False)

            # Micah sendo álibi
            # K = "Micah estava na loja de armas com Lenny"
            # L = "Lenny viu Micah na loja de armas"
            # L  K		(V)
            micah_validation = ttg.Truths(["Micah estava na loja de armas com Lenny",
                                           "Lenny viu Micah na loja de armas"],
                                          ["Lenny viu Micah na loja de armas => Micah estava na loja de armas com Lenny"], ints=False)

        # Micah sendo assassino
        elif murder == "Micah":
            # A = "Micah viu Abigail indo para o acampamento"
            # B = "Abigail estava no banco com Bill"
            # C = "Bill estava com Abigail no banco"
            # C ^ B  ¬A		(F)
            micah_validation = ttg.Truths(["Micah viu Abigail indo para o acampamento",
                                           "Abigail estava no banco com Bill",
                                           "Bill estava com Abigail no banco"],
                                          ["Bill estava com Abigail no banco and Abigail estava no banco com Bill => not Micah viu Abigail indo para o acampamento"], ints=False)

            javier_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            lenny_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            sally_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

            # Abigail sendo álibi
            # B = "Abigail estava no banco com Bill"
            # C = "Bill estava com Abigail no banco"
            # C  B		(V)
            abigail_validation = ttg.Truths(["Abigail estava no banco com Bill",
                                             "Abigail estava no banco com Bill"],
                                            ["Bill estava com Abigail no banco => Abigail estava no banco com Bill"], ints=False)
            bill_validation = ttg.Truths(["Abigail estava no banco com Bill",
                                          "Abigail estava no banco com Bill"],
                                         ["Abigail estava no banco com Bill => Bill estava com Abigail no banco"], ints=False)

            # Pearson sendo álibi
            # F = "Pearson estava com o Doutor no consultório médico"
            # G = "Doutor estava trabalhando e encontrou Pearson no consultório médico"
            # G  F		(V)
            pearson_validation = ttg.Truths(["Pearson estava com o Doutor no consultório médico",
                                             "Pearson estava com o Doutor no consultório médico"],
                                            ["Pearson estava com o Doutor no consultório médico => Pearson estava com o Doutor no consultório médico"], ints=False)
            doutor_validation = ttg.Truths(["Pearson estava com o Doutor no consultório médico",
                                            "Pearson estava com o Doutor no consultório médico",
                                           "Pearson estava com o Doutor no consultório médico => Doutor estava trabalhando e encontrou Pearson no consultório médico"], ints=False)

            # Sadie sendo álibi
            # H = "Sadie estava no hotel com Leopold"
            # I = "Leopold estava com Sadie no hotel"
            # I  H		(V)
            sadie_validation = ttg.Truths(["Sadie estava no hotel com Leopold",
                                           "Leopold estava com Sadie no hotel"
                                          "Leopold estava com Sadie no hote => Sadie estava no hotel com Leopold"], ints=False)
            leopold_validation = ttg.Truths(["Sadie estava no hotel com Leopold",
                                             "Leopold estava com Sadie no hotel"],
                                            ["Sadie estava no hotel com Leopold => Leopold estava com Sadie no hotel"], ints=False)


#se for de noite - OK
    elif time_of_death == "noite":

        # Lenny sendo assassino
        if murder == "Lenny":
            # A = "Lenny estava no teatro e viu Pearson no acampamento"
            # B = "Doutor disse que a peça foi cancelada"
            # C = "Javier disse que a peça foi cancelada"
            # C ^ B  ¬A		(F)
            lenny_validation = ttg.Truths(["Lenny estava no teatro e viu Pearson no acampamento",
                "Doutor disse que a peça foi cancelada", "Javier disse que a peça foi cancelada"], ["Javier disse que a peça foi cancelada and Doutor disse que a peça foi cancelada => not Lenny estava no teatro e viu Pearson no acampamento"], ints=False)

            # Abigail
            # Abigail
            abigail_validation = ttg.Truths(
                ["Abigail estava trabalhando no bordel com Bill", "Bill estava com Abigail no bordel"],
                ["Bill estava com Abigail no bordel => Abigail estava trabalhando no bordel com Bill"],
                ints=False
            )
            bill_validation = ttg.Truths(
                ["Abigail estava trabalhando no bordel com Bill", "Bill estava com Abigail no bordel"],
                ["Abigail estava trabalhando no bordel com Bill => Bill estava com Abigail no bordel"],
                ints=False
            )

            # Javier
            javier_validation = ttg.Truths(
                ["Javier iria para o teatro com Doutor, mas não foi",
                 "Bill iria para o teatro com Doutor, mas não foi"],
                [
                    "Bill iria para o teatro com Doutor, mas não foi => Javier iria para o teatro com Doutor, mas não foi"],
                ints=False
            )
            doutor_validation = ttg.Truths(
                ["Javier iria para o teatro com Doutor, mas não foi",
                 "Bill iria para o teatro com Doutor, mas não foi"],
                [
                    "Bill iria para o teatro com Doutor, mas não foi => Javier iria para o teatro com Doutor, mas não foi"],
                ints=False
            )

            # Pearson
            # H = "Pearson estava com Sadie no acampamento"
            # I = "Sadie estava com Pearson no acampamento"
            # I  H		(V)
            # Pearson
            pearson_validation = ttg.Truths(
                ["Pearson estava com Sadie no acampamento", "Sadie estava com Pearson no acampamento"],
                ["Sadie estava com Pearson no acampamento => Pearson estava com Sadie no acampamento"],
                ints=False
            )
            sadie_validation = ttg.Truths(
                ["Pearson estava com Sadie no acampamento", "Sadie estava com Pearson no acampamento"],
                ["Pearson estava com Sadie no acampamento => Sadie estava com Pearson no acampamento"],
                ints=False
            )

            # Leopold
            leopold_validation = ttg.Truths(
                ["Leopold estava com Micah no bordel", "Micah estava com Leopold no bordel"],
                ["Micah estava com Leopold no bordel => Leopold estava com Micah no bordel"],
                ints=False
            )
            micah_validation = ttg.Truths(
                ["Leopold estava com Micah no bordel", "Micah estava com Leopold no bordel"],
                ["Leopold estava com Micah no bordel => Micah estava com Leopold no bordel"],
                ints=False
            )


            sally_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

        # Javier sendo assassino
        if murder == "Javier":
            # Javier
            A = "Javier estava no teatro"
            B = "Doutor iria para o teatro, mas a peça foi cancelada"
            # B -> ¬A (F)
            javier_validation = ttg.Truths(
                ["Javier estava no teatro", "Doutor iria para o teatro, mas a peça foi cancelada"],
                ["Doutor iria para o teatro, mas a peça foi cancelada => not Javier estava no teatro"],
                ints=False
            )
            doutor_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

            # Abigail
            C = "Abigail estava trabalhando no bordel com Bill"
            D = "Bill estava com Abigail no bordel"
            # D -> C (V)
            abigail_validation = ttg.Truths(
                ["Abigail estava trabalhando no bordel com Bill", "Bill estava com Abigail no bordel"],
                ["Bill estava com Abigail no bordel => Abigail estava trabalhando no bordel com Bill"],
                ints=False
            )
            bill_validation = ttg.Truths(
                ["Abigail estava trabalhando no bordel com Bill", "Bill estava com Abigail no bordel"],
                ["Abigail estava trabalhando no bordel com Bill => Bill estava com Abigail no bordel"],
                ints=False
            )

            # Lenny
            E = "Lenny estava no saloon com Sally"
            F = "Sally viu Lenny no saloon"
            # F -> E (V)
            lenny_validation = ttg.Truths(
                ["Lenny estava no saloon com Sally", "Sally viu Lenny no saloon"],
                ["Sally viu Lenny no saloon => Lenny estava no saloon com Sally"],
                ints=False
            )
            sally_validation = ttg.Truths(
                ["Lenny estava no saloon com Sally", "Sally viu Lenny no saloon"],
                ["Lenny estava no saloon com Sally => Sally viu Lenny no saloon"],
                ints=False
            )

            # Pearson
            G = "Pearson estava com Sadie no acampamento"
            H = "Sadie estava com Pearson no acampamento"
            # H -> G (V)
            pearson_validation = ttg.Truths(
                ["Pearson estava com Sadie no acampamento", "Sadie estava com Pearson no acampamento"],
                ["Sadie estava com Pearson no acampamento => Pearson estava com Sadie no acampamento"],
                ints=False
            )
            sadie_validation = ttg.Truths(
                ["Pearson estava com Sadie no acampamento", "Sadie estava com Pearson no acampamento"],
                ["Pearson estava com Sadie no acampamento => Sadie estava com Pearson no acampamento"],
                ints=False
            )

            # Leopold
            I = "Leopold estava com Micah no bordel"
            J = "Micah estava com Leopold no bordel"
            # J -> I (V)
            leopold_validation = ttg.Truths(
                ["Leopold estava com Micah no bordel", "Micah estava com Leopold no bordel"],
                ["Micah estava com Leopold no bordel => Leopold estava com Micah no bordel"],
                ints=False
            )
            micah_validation = ttg.Truths(
                ["Leopold estava com Micah no bordel", "Micah estava com Leopold no bordel"],
                ["Leopold estava com Micah no bordel => Micah estava com Leopold no bordel"],
                ints=False
            )

            # Bill sendo assassino
            if murder == "Bill":
                A = "Bill estava com Abigail no bordel"
                B = "Abigail estava sozinha no bordel"
                # B -> ¬A (F)
                bill_validation = ttg.Truths(
                    ["Bill estava com Abigail no bordel", "Abigail estava sozinha no bordel"],
                    ["Abigail estava sozinha no bordel => not Bill estava com Abigail no bordel"],
                    ints=False
                )

            abigail_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

            sally_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

            # Lenny
            C = "Lenny estava no saloon com Sally"
            D = "Sally viu Lenny no saloon"
            # D  C		(V)
            lenny_validation = ttg.Truths(["Lenny estava no saloon com Sally", "Sally viu Lenny no saloon"], ["Sally viu Lenny no saloon => Lenny estava no saloon com Sally"], ints=False)

            ## Javier
            javier_validation = ttg.Truths(
                ["Javier iria para o teatro com Doutor, mas não foi", 
                 "Bill iria para o teatro com Doutor, mas não foi"],
                ["Bill iria para o teatro com Doutor, mas não foi => Javier iria para o teatro com Doutor, mas não foi"],
                ints=False
            )
            
            # Pearson
            pearson_validation = ttg.Truths(
                ["Pearson estava com Sadie no acampamento", 
                 "Sadie estava com Pearson no acampamento"],
                ["Sadie estava com Pearson no acampamento => Pearson estava com Sadie no acampamento"],
                ints=False
            )
            
            # Sadie (incluindo a validação de Sadie)
            sadie_validation = ttg.Truths(
                ["Pearson estava com Sadie no acampamento", 
                 "Sadie estava com Pearson no acampamento"],
                ["Pearson estava com Sadie no acampamento => Sadie estava com Pearson no acampamento"],
                ints=False
            )
            
            # Leopold
            leopold_validation = ttg.Truths(
                ["Leopold estava com Micah no bordel", 
                 "Micah estava com Leopold no bordel"],
                ["Micah estava com Leopold no bordel => Leopold estava com Micah no bordel"],
                ints=False
            )
            
            # Doutor
            doutor_validation = ttg.Truths(
                ["Javier iria para o teatro com Doutor, mas não foi", 
                 "Bill iria para o teatro com Doutor, mas não foi"],
                ["Bill iria para o teatro com Doutor, mas não foi => Javier iria para o teatro com Doutor, mas não foi"],
                ints=False
            )


        # Pearson sendo assassino
        if murder == "Pearson":
            # Pearson
            pearson_validation = ttg.Truths(
                ["Pearson estava no teatro",
                 "Doutor iria para o teatro, mas a peça foi cancelada",
                 "Javier iria para o teatro, mas a peça foi cancelada"],
                ["Javier iria para o teatro, mas a peça foi cancelada and Doutor iria para o teatro, mas a peça foi cancelada => not Pearson estava no teatro"],
                ints=False
            )

            # Abigail
            abigail_validation = ttg.Truths(
                ["Abigail estava trabalhando no bordel com Bill",
                 "Bill estava com Abigail no bordel"],
                ["Bill estava com Abigail no bordel => Abigail estava trabalhando no bordel com Bill"],
                ints=False
            )


            # Lenny
            # F = "Lenny estava no saloon com Sally e Sadie"
            # G = "Sally viu Lenny e Sadie no saloon"
            # H = "Sadie estava no saloon com Sally e Lenny"
            # G ^ H  F		(V)
            lenny_validation = ttg.Truths(["Lenny estava no saloon com Sally e Sadie", "Sally viu Lenny e Sadie no saloon", "Sadie estava no saloon com Sally e Lenny"], ["Sally viu Lenny e Sadie no saloon and  => Lenny estava no saloon com Sally e Sadie"], ints=False)

            # Bill
            # J = "Abigail estava trabalhando no bordel com Bill"
            # K = "Bill estava com Abigail no bordel"
            # K  J		(V)
            bill_validation = ttg.Truths(["Abigail estava trabalhando no bordel com Bill", "Bill estava com Abigail no bordel"], ["Bill estava com Abigail no bordel => Abigail estava trabalhando no bordel com Bill"], ints=False)

            javier_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            doutor_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

            # Sadie
            # F = "Lenny estava no saloon com Sally e Sadie"
            # G = "Sally viu Lenny e Sadie no saloon"
            # H = "Sadie estava no saloon com Sally e Lenny"
            # G ^ F  H		(V)
            sadie_validation = ttg.Truths(["Lenny estava no saloon com Sally e Sadie",
                                           "Sally viu Lenny e Sadie no saloon",
                                           "Sadie estava no saloon com Sally e Lenny"],["Sally viu Lenny e Sadie no saloon and Lenny estava no saloon com Sally e Sadie => H"], ints=False)

            # Leopold
            # L = "Leopold estava com Micah no bordel"
            # M = "Micah estava com Leopold no bordel"
            # M  L		(V)
            leopold_validation = ttg.Truths(["Leopold estava com Micah no bordel",
                                             "Micah estava com Leopold no bordel"], ["Micah estava com Leopold no bordel => Leopold estava com Micah no bordel"], ints=False)

            # Sally
            # F = "Lenny estava no saloon com Sally e Sadie"
            # G = "Sally viu Lenny e Sadie no saloon"
            # H = "Sadie estava no saloon com Sally e Lenny"
            # F ^ H  G		(V)
            sally_validation = ttg.Truths(["Lenny estava no saloon com Sally e Sadie",
                                           "Sally viu Lenny e Sadie no saloon",
                                           "Sadie estava no saloon com Sally e Lenny"], ["Lenny estava no saloon com Sally e Sadie and Sadie estava no saloon com Sally e Lenny => Sally viu Lenny e Sadie no saloon"], ints=False)

            # Micah
            # L = "Leopold estava com Micah no bordel"
            # M = "Micah estava com Leopold no bordel"
            # J = "Abigail estava trabalhando no bordel com Bill"
            # J  M		(V)
            micah_validation = ttg.Truths(["Leopold estava com Micah no bordel",
                                           "Micah estava com Leopold no bordel",
                                           "Abigail estava trabalhando no bordel com Bill"], ["Abigail estava trabalhando no bordel com Bill => Micah estava com Leopold no bordel"], ints=False)

        # Sadie sendo assassina
        if murder == "Sadie":
            # A = "Sadie estava com Leopold no hotel"
            # B = "Leopold estava com Micah no bordel"
            # C = "Micah estava com Leopold no bordel"
            # B ^ C  ¬A		(F)
            sadie_validation = ttg.Truths(["Sadie estava com Leopold no hotel",
                                           "Leopold estava com Micah no bordel",
                                           "Micah estava com Leopold no bordel"], ["Leopold estava com Micah no bordel and Micah estava com Leopold no bordel => not Sadie estava com Leopold no hotel"], ints=False)

            # Abigail
            # D = "Abigail estava trabalhando no bordel com Bill"
            # E = "Bill estava com Abigail no bordel"
            # E  D		(V)
            abigail_validation = ttg.Truths(["Abigail estava trabalhando no bordel com Bill",
                                             "Bill estava com Abigail no bordel"], ["Bill estava com Abigail no bordel => Abigail estava trabalhando no bordel com Bill"], ints=False)

            # Lenny
            # F = "Lenny estava no saloon com Sally"
            # G = "Sally viu Lenny no saloon"
            # G  F		(V)
            lenny_validation = ttg.Truths(["Lenny estava no saloon com Sally",
                                            "Sally viu Lenny no saloon"], ["G => Lenny estava no saloon com Sally"], ints=False)

            # Bill
            # D = "Abigail estava trabalhando no bordel com Bill"
            # E = "Bill estava com Abigail no bordel"
            # D  E		(V)
            bill_validation = ttg.Truths(["Abigail estava trabalhando no bordel com Bill",
                                          "Bill estava com Abigail no bordel"], ["Abigail estava trabalhando no bordel com Bill => Bill estava com Abigail no bordel"], ints=False)

            # Leopold
            # J = "Leopold estava com Micah no bordel"
            # K = "Micah estava com Leopold no bordel"
            # K  J		(V)
            leopold_validation = ttg.Truths(["Leopold estava com Micah no bordel",
                                             "Micah estava com Leopold no bordel"], ["Micah estava com Leopold no bordel => Leopold estava com Micah no bordel"], ints=False)

            # Sally
            # F = "Lenny estava no saloon com Sally"
            # G = "Sally viu Lenny no saloon"
            # F  G		(V)
            sally_validation = ttg.Truths(["Lenny estava no saloon com Sally",
                                           "Sally viu Lenny no saloon"], ["Lenny estava no saloon com Sally => Sally viu Lenny no saloon"], ints=False)

            # Micah
            # J = "Leopold estava com Micah no bordel"
            # K = "Micah estava com Leopold no bordel"
            # J  K		(V)
            micah_validation = ttg.Truths(["Leopold estava com Micah no bordel",
                                           "Leopold estava com Micah no bordel"], ["Leopold estava com Micah no bordel => Micah estava com Leopold no bordel"], ints=False)

            javier_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            doutor_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            pearson_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

        # Leopold sendo assassino
        if murder == "Leopold":
            # A = "Leopold estava indo para o teatro"
            # B = "Javier iria para o teatro, mas a peça foi cancelada"
            # C = "Doutor iria para o teatro, mas a peça foi cancelada"
            # C ^ B = ¬A		(F)
            leopold_validation = ttg.Truths(["Leopold estava indo para o teatro",
                                             "Javier iria para o teatro, mas a peça foi cancelada",
                                             "Doutor iria para o teatro, mas a peça foi cancelada"], ["Javier iria para o teatro, mas a peça foi cancelada and Doutor iria para o teatro, mas a peça foi cancelada => not Leopold estava indo para o teatro"], ints=False)

            # Abigail
            # D = "Abigail estava trabalhando no bordel com Bill"
            # E = "Bill estava com Abigail no bordel"
            # E  D		(V)
            abigail_validation = ttg.Truths(["Abigail estava trabalhando no bordel com Bill",
                                             "Bill estava com Abigail no bordel"], ["Bill estava com Abigail no bordel => Abigail estava trabalhando no bordel com Bill"], ints=False)

            # Lenny
            # F = "Lenny estava no saloon com Sally"
            # G = "Sally viu Lenny no saloon"
            # G  F		(V)
            lenny_validation = ttg.Truths(["Lenny estava no saloon com Sally", "Sally viu Lenny no saloon"],
            ["Sally viu Lenny no saloon => Lenny estava no saloon com Sally"], ints=False)

            # Bill
            # D = "Abigail estava trabalhando no bordel com Bill"
            # E = "Bill estava com Abigail no bordel"
            # D  E		(V)
            bill_validation = ttg.Truths(["Pearson estava com Sadie no acampamento", "Bill estava com Abigail no bordel"], 
                                         ["Abigail estava trabalhando no bordel com Bill => Bill estava com Abigail no bordel"], ints=False)

            # Pearson
            # H = "Pearson estava com Sadie no acampamento"
            # I = "Sadie estava com Pearson no acampamento"
            # I  H		(V)
            pearson_validation = ttg.Truths(["Pearson estava com Sadie no acampamento", "Sadie estava com Pearson no acampamento"],
                                            ["Sadie estava com Pearson no acampamento => Pearson estava com Sadie no acampamento"], ints=False)

            # Sadie
            # H = "Pearson estava com Sadie no acampamento"
            # I = "Sadie estava com Pearson no acampamento"
            # H  I		(V)
            sadie_validation = ttg.Truths(["Pearson estava com Sadie no acampamento", "Sadie estava com Pearson no acampamento"],
                                          ["Pearson estava com Sadie no acampamento => Sadie estava com Pearson no acampamento"], ints=False)

            # Sally
            sally_validation = ttg.Truths(
                ["Lenny estava no saloon com Sally",
                 "Sally viu Lenny no saloon"],
                ["Lenny estava no saloon com Sally => Sally viu Lenny no saloon"],
                ints=False
            )

            javier_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            doutor_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            micah_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

        # Doutor sendo assassino
        if murder == "Doutor":
            # Doutor viu Abigail no acampamento
            doutor_validation = ttg.Truths(
                ["Doutor viu Abigail no acampamento",
                 "Abigail estava trabalhando no bordel com Bill",
                 "Bill estava com Abigail no bordel"],
                ["Abigail estava trabalhando no bordel com Bill and Bill estava com Abigail no bordel => not Doutor viu Abigail no acampamento"],
                ints=False
            )

            # Abigail
            abigail_validation = ttg.Truths(
                ["Abigail estava trabalhando no bordel com Bill",
                 "Bill estava com Abigail no bordel"],
                ["Bill estava com Abigail no bordel => Abigail estava trabalhando no bordel com Bill"],
                ints=False
            )

            bill_validation = ttg.Truths(
                ["Abigail estava trabalhando no bordel com Bill",
                 "Bill estava com Abigail no bordel"],
                ["Bill estava com Abigail no bordel => Abigail estava trabalhando no bordel com Bill"],
                ints=False
            )

            # Lenny
            lenny_validation = ttg.Truths(
                ["Lenny estava no saloon com Sally",
                 "Sally viu Lenny no saloon"],
                ["Sally viu Lenny no saloon => Lenny estava no saloon com Sally"],
                ints=False
            )

            sally_validation = ttg.Truths(
                ["Lenny estava no saloon com Sally",
                 "Sally viu Lenny no saloon"],
                ["Sally viu Lenny no saloon => Lenny estava no saloon com Sally"],
                ints=False
            )

            # Pearson
            pearson_validation = ttg.Truths(
                ["Pearson estava com Sadie no acampamento",
                 "Sadie estava com Pearson no acampamento"],
                ["Sadie estava com Pearson no acampamento => Pearson estava com Sadie no acampamento"],
                ints=False
            )

            sadie_validation = ttg.Truths(
                ["Pearson estava com Sadie no acampamento",
                 "Sadie estava com Pearson no acampamento"],
                ["Pearson estava com Sadie no acampamento => Sadie estava com Pearson no acampamento"],
                ints=False
            )

            # Leopold
            leopold_validation = ttg.Truths(
                ["Leopold estava com Micah no bordel",
                 "Micah estava com Leopold no bordel"],
                ["Micah estava com Leopold no bordel => Leopold estava com Micah no bordel"],
                ints=False
            )

            micah_validation = ttg.Truths(
                ["Leopold estava com Micah no bordel",
                 "Micah estava com Leopold no bordel"],
                ["Leopold estava com Micah no bordel => Micah estava com Leopold no bordel"],
                ints=False
            )


            javier_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

        # Micah sendo assassino
        if murder == "Micah":
            # Micah avistou Abigail perto do acampamento
            # A = "Micah avistou Abigail perto do acampamento"
            # B = "Abigail estava trabalhando no bordel com Bill"
            # C = "Bill estava com Abigail no bordel"
            # C ^ B -> ¬A

            micah_validation = ttg.Truths(
                ["Micah avistou Abigail perto do acampamento",
                 "Abigail estava trabalhando no bordel com Bill",
                 "Bill estava com Abigail no bordel"],
                ["Abigail estava trabalhando no bordel com Bill and Bill estava com Abigail no bordel => not Micah avistou Abigail perto do acampamento"],
                ints=False
            )

            abigail_validation = ttg.Truths(
                ["Abigail estava trabalhando no bordel com Bill",
                 "Bill estava com Abigail no bordel"],
                ["Bill estava com Abigail no bordel => Abigail estava trabalhando no bordel com Bill"],
                ints=False
            )

            bill_validation = ttg.Truths(
                ["Abigail estava trabalhando no bordel com Bill",
                 "Bill estava com Abigail no bordel"],
                ["Bill estava com Abigail no bordel => Abigail estava trabalhando no bordel com Bill"],
                ints=False
            )

            # Lenny
            # D = "Lenny estava no saloon com Sally"
            # E = "Sally viu Lenny no saloon"
            # E -> D

            lenny_validation = ttg.Truths(
                ["Lenny estava no saloon com Sally",
                 "Sally viu Lenny no saloon"],
                ["Sally viu Lenny no saloon => Lenny estava no saloon com Sally"],
                ints=False
            )

            sally_validation = ttg.Truths(
                ["Lenny estava no saloon com Sally",
                 "Sally viu Lenny no saloon"],
                ["Sally viu Lenny no saloon => Lenny estava no saloon com Sally"],
                ints=False
            )

            # Pearson
            # G = "Pearson estava com Sadie no acampamento"
            # H = "Sadie estava com Pearson no acampamento"
            # H -> G

            pearson_validation = ttg.Truths(
                ["Pearson estava com Sadie no acampamento",
                 "Sadie estava com Pearson no acampamento"],
                ["Sadie estava com Pearson no acampamento => Pearson estava com Sadie no acampamento"],
                ints=False
            )

            sadie_validation = ttg.Truths(
                ["Pearson estava com Sadie no acampamento",
                 "Sadie estava com Pearson no acampamento"],
                ["Pearson estava com Sadie no acampamento => Sadie estava com Pearson no acampamento"],
                ints=False
            )


            javier_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            doutor_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            leopold_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

#se for de madrugada
    elif time_of_death == "madrugada":

        # Micah sendo assassino
        if murder == "Micah":
            # Micah estava com Doutor no Saloon
            # A = "Micah estava com Doutor no Saloon"
            # B = "Doutor estava no saloon com Sadie e Sally"
            # C = "Sadie estava com Doutor e Sally"
            # D = "Sally estava com Doutor e Sadie"
            # D ^ C ^ B -> A

            micah_validation = ttg.Truths(
                ["Micah estava com Doutor no Saloon",
                 "Doutor estava no saloon com Sadie e Sally",
                 "Sadie estava com Doutor e Sally",
                 "Sally estava com Doutor e Sadie"],
                ["Sally estava com Doutor e Sadie and Sadie estava com Doutor e Sally and Doutor estava no saloon com Sadie e Sally => Micah estava com Doutor no Saloon"],
                ints=False
            )

            # Abigail sendo álibi
            # E = "Abigail estava com Javier e Pearson no bordel"
            # F = "Javier estava com Abigail e Pearson no bordel"
            # G = "Pearson estava com Abigail e Javier no bordel"
            # G ^ F -> E

            abigail_validation = ttg.Truths(
                ["Abigail estava com Javier e Pearson no bordel",
                 "Javier estava com Abigail e Pearson no bordel",
                 "Pearson estava com Abigail e Javier no bordel"],
                ["Pearson estava com Abigail e Javier no bordel and Javier estava com Abigail e Pearson no bordel => Abigail estava com Javier e Pearson no bordel"],
                ints=False
            )

            javier_validation = ttg.Truths(
                ["Abigail estava com Javier e Pearson no bordel",
                 "Javier estava com Abigail e Pearson no bordel",
                 "Pearson estava com Abigail e Javier no bordel"],
                ["Pearson estava com Abigail e Javier no bordel and Abigail estava com Javier e Pearson no bordel => Javier estava com Abigail e Pearson no bordel"],
                ints=False
            )

            pearson_validation = ttg.Truths(
                ["Abigail estava com Javier e Pearson no bordel",
                 "Javier estava com Abigail e Pearson no bordel",
                 "Pearson estava com Abigail e Javier no bordel"],
                ["Abigail estava com Javier e Pearson no bordel and Javier estava com Abigail e Pearson no bordel => Pearson estava com Abigail e Javier no bordel"],
                ints=False
            )

            # Lenny sendo álibi
            # H = "Lenny estava com Bill e Leopold no hotel"
            # I = "Bill estava com Lenny e Leopold no hotel"
            # J = "Leopold estava com Bill e Lenny no hotel"
            # I ^ J -> H

            lenny_validation = ttg.Truths(
                ["Lenny estava com Bill e Leopold no hotel",
                 "Bill estava com Lenny e Leopold no hotel",
                 "Leopold estava com Bill e Lenny no hotel"],
                ["Bill estava com Lenny e Leopold no hotel and Leopold estava com Bill e Lenny no hotel => Lenny estava com Bill e Leopold no hotel"],
                ints=False
            )

            bill_validation = ttg.Truths(
                ["Lenny estava com Bill e Leopold no hotel",
                 "Bill estava com Lenny e Leopold no hotel",
                 "Leopold estava com Bill e Lenny no hotel"],
                ["Lenny estava com Bill e Leopold no hotel and Leopold estava com Bill e Lenny no hotel => Bill estava com Lenny e Leopold no hotel"],
                ints=False
            )

            leopold_validation = ttg.Truths(
                ["Lenny estava com Bill e Leopold no hotel",
                 "Bill estava com Lenny e Leopold no hotel",
                 "Leopold estava com Bill e Lenny no hotel"],
                ["Bill estava com Lenny e Leopold no hotel and Lenny estava com Bill e Leopold no hotel => Leopold estava com Bill e Lenny no hotel"],
                ints=False
            )

            # Sadie sendo álibi
            # K = "Sally estava trabalhando no saloon"
            # L = "Sadie estava com Sally e Doutor no saloon"
            # M = "Doutor estava com Sally e Sadie"
            # K ^ M -> L

            sadie_validation = ttg.Truths(
                ["Sally estava trabalhando no saloon",
                 "Sadie estava com Sally e Doutor no saloon",
                 "Doutor estava com Sally e Sadie"],
                ["Sally estava trabalhando no saloon and Doutor estava com Sally e Sadie => Sadie estava com Sally e Doutor no saloon"],
                ints=False
            )

            doutor_validation = ttg.Truths(
                ["Sally estava trabalhando no saloon",
                 "Sadie estava com Sally e Doutor no saloon",
                 "Doutor estava com Sally e Sadie"],
                ["Sally estava trabalhando no saloon and Sadie estava com Sally e Doutor no saloon => Doutor estava com Sally e Sadie"],
                ints=False
            )

            sally_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

        #Lenny sendo assassino
        elif murder == "Lenny":
            # Lenny disse que avistou Abigail
            # A = "Lenny disse que avistou Abigail"
            # B = "Abigail estava com Javier no bordel"
            # C = "Javier estava com Abigail no bordel"
            # C ^ B -> ¬A

            lenny_validation = ttg.Truths(
                ["Lenny disse que avistou Abigail",
                 "Abigail estava com Javier no bordel",
                 "Javier estava com Abigail no bordel"],
                [
                    "Javier estava com Abigail no bordel and Abigail estava com Javier no bordel => not Lenny disse que avistou Abigail"],
                ints=False
            )

            # Abigail sendo álibi
            # B = "Abigail estava com Javier no bordel"
            # C = "Javier estava com Abigail no bordel"
            # C -> B

            abigail_validation = ttg.Truths(
                ["Abigail estava com Javier no bordel",
                 "Javier estava com Abigail no bordel"],
                ["Javier estava com Abigail no bordel => Abigail estava com Javier no bordel"],
                ints=False
            )

            # Javier sendo álibi
            # B = "Abigail estava com Javier no bordel"
            # C = "Javier estava com Abigail no bordel"
            # B -> C

            javier_validation = ttg.Truths(
                ["Abigail estava com Javier no bordel",
                 "Javier estava com Abigail no bordel"],
                ["Abigail estava com Javier no bordel => Javier estava com Abigail no bordel"],
                ints=False
            )

            # Bill sendo álibi
            # D = "Bill estava com Leopold"
            # E = "Leopold estava com Bill"
            # E -> D

            bill_validation = ttg.Truths(
                ["Bill estava com Leopold",
                 "Leopold estava com Bill"],
                ["Leopold estava com Bill => Bill estava com Leopold"],
                ints=False
            )

            # Sadie sendo álibi
            # G = "Sadie estava no saloon com o Doutor"
            # H = "Doutor estava no Saloon com Sadie"
            # H -> G

            sadie_validation = ttg.Truths(
                ["Sadie estava no saloon com o Doutor",
                 "Doutor estava no Saloon com Sadie"],
                ["Doutor estava no Saloon com Sadie => Sadie estava no saloon com o Doutor"],
                ints=False
            )

            # Leopold sendo álibi
            # D = "Bill estava com Leopold"
            # E = "Leopold estava com Bill"
            # D -> E

            leopold_validation = ttg.Truths(
                ["Bill estava com Leopold",
                 "Leopold estava com Bill"],
                ["Bill estava com Leopold => Leopold estava com Bill"],
                ints=False
            )

            # Doutor sendo álibi
            # G = "Sadie estava no saloon com o Doutor"
            # H = "Doutor estava no Saloon com Sadie"
            # G  H
            doutor_validation = ttg.Truths(["Sadie estava no saloon com o Doutor",
                                            "Doutor estava no Saloon com Sadie"],
                                            ["Sadie estava no saloon com o Doutor => Doutor estava no Saloon com Sadie#"], ints=False)

            # Sally sendo álibi
            # I = "Sally estava trabalhando e viu o Doutor e a Sadie"
            # G = "Sadie estava no saloon com o Doutor"
            # H = "Doutor estava no Saloon com Sadie"
            # G ^ H  I
            sally_validation = ttg.Truths(["Sadie estava no saloon com o Doutor", "Doutor estava no Saloon com Sadie","Sally estava trabalhando e viu o Doutor e a Sadie"],
                                          ["Sadie estava no saloon com o Doutor and Doutor estava no Saloon com Sadie => Sally estava trabalhando e viu o Doutor e a Sadie"], ints=False)

            micah_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            pearson_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

        #Javier sendo assassino
        elif murder == "Javier":
            # Javier estava no bordel
            # A = "Javier estava no bordel"
            # B = "Abigail estava somente com Pearson no bordel"
            # C = "Pearson estava com Abigail no bordel"
            # B ^ C -> ¬A

            javier_validation = ttg.Truths(
                ["Javier estava no bordel",
                 "Abigail estava somente com Pearson no bordel",
                 "Pearson estava com Abigail no bordel"],
                [
                    "Abigail estava somente com Pearson no bordel and Pearson estava com Abigail no bordel => not Javier estava no bordel"],
                ints=False
            )

            # Abigail sendo álibi
            # B = "Abigail estava somente com Pearson no bordel"
            # C = "Pearson estava com Abigail no bordel"
            # C -> B

            abigail_validation = ttg.Truths(
                ["Abigail estava somente com Pearson no bordel",
                 "Pearson estava com Abigail no bordel"],
                ["Pearson estava com Abigail no bordel => Abigail estava somente com Pearson no bordel"],
                ints=False
            )

            # Lenny sendo álibi
            # D = "Lenny viu Leopold"
            # E = "Leopold viu Lenny"
            # E -> D

            lenny_validation = ttg.Truths(
                ["Lenny viu Leopold",
                 "Leopold viu Lenny"],
                ["Leopold viu Lenny => Lenny viu Leopold"],
                ints=False
            )

            # Bill sendo álibi
            # F = "Bill estava com Leopold"
            # G = "Leopold estava com Bill"
            # G -> F

            bill_validation = ttg.Truths(
                ["Bill estava com Leopold",
                 "Leopold estava com Bill"],
                ["Leopold estava com Bill => Bill estava com Leopold"],
                ints=False
            )

            # Sadie sendo álibi
            # I = "Sadie estava no saloon com o Doutor"
            # J = "Doutor estava no Saloon com Sadie"
            # J -> I

            sadie_validation = ttg.Truths(
                ["Sadie estava no saloon com o Doutor",
                 "Doutor estava no Saloon com Sadie"],
                ["Doutor estava no Saloon com Sadie => Sadie estava no saloon com o Doutor"],
                ints=False
            )

            # Leopold sendo álibi
            # F = "Bill estava com Leopold"
            # G = "Leopold estava com Bill"
            # G -> F

            leopold_validation = ttg.Truths(
                ["Bill estava com Leopold",
                 "Leopold estava com Bill"],
                ["Leopold estava com Bill => Bill estava com Leopold"],
                ints=False
            )

            # Doutor sendo álibi
            # G = "Sadie estava no saloon com o Doutor"
            # H = "Doutor estava no Saloon com Sadie"
            # G -> H

            doutor_validation = ttg.Truths(
                ["Sadie estava no saloon com o Doutor",
                 "Doutor estava no Saloon com Sadie"],
                ["Sadie estava no saloon com o Doutor => Doutor estava no Saloon com Sadie"],
                ints=False
            )

            # Sally sendo álibi
            # K = "Sally estava trabalhando e viu o Doutor e a Sadie"
            # I = "Sadie estava no saloon com o Doutor"
            # J = "Doutor estava no Saloon com Sadie"
            # J ^ I -> K

            sally_validation = ttg.Truths(
                ["Sadie estava no saloon com o Doutor",
                 "Doutor estava no Saloon com Sadie",
                 "Sally estava trabalhando e viu o Doutor e a Sadie"],
                [
                    "Doutor estava no Saloon com Sadie and Sadie estava no saloon com o Doutor => Sally estava trabalhando e viu o Doutor e a Sadie"],
                ints=False
            )

            micah_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            pearson_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

        #Bill sendo assassino
        elif murder == "Bill":
            # Bill estava com Leopold no hotel
            # A = "Bill estava com Leopold no hotel"
            # B = "Leopold estava só com Lenny no hotel"
            # C = "Lenny estava só com Leopold no hotel"
            # B ^ C -> ¬A

            bill_validation = ttg.Truths(
                ["Bill estava com Leopold no hotel",
                 "Leopold estava só com Lenny no hotel",
                 "Lenny estava só com Leopold no hotel"],
                ["Leopold estava só com Lenny no hotel and Lenny estava só com Leopold no hotel => not Bill estava com Leopold no hotel"],
                ints=False
            )

            # Abigail sendo álibi
            # D = "Abigail estava com Javier e Pearson no bordel"
            # E = "Javier estava com Abigail e Pearson no bordel"
            # F = "Pearson estava com Abigail e Javier no bordel"
            # E ^ F -> D

            abigail_validation = ttg.Truths(
                ["Abigail estava com Javier e Pearson no bordel",
                 "Javier estava com Abigail e Pearson no bordel",
                 "Pearson estava com Abigail e Javier no bordel"],
                ["Javier estava com Abigail e Pearson no bordel and Pearson estava com Abigail e Javier no bordel => Abigail estava com Javier e Pearson no bordel"],
                ints=False
            )

            # Lenny sendo álibi
            # B = "Leopold viu Lenny"
            # C = "Lenny viu Leopold"
            # C -> B

            lenny_validation = ttg.Truths(
                ["Leopold viu Lenny",
                 "Lenny viu Leopold"],
                ["Lenny viu Leopold => Leopold viu Lenny"],
                ints=False
            )

            # Javier sendo álibi
            # D = "Abigail estava com Javier e Pearson no bordel"
            # E = "Javier estava com Abigail e Pearson no bordel"
            # F = "Pearson estava com Abigail e Javier no bordel"
            # E ^ F -> D

            javier_validation = ttg.Truths(
                ["Abigail estava com Javier e Pearson no bordel",
                 "Javier estava com Abigail e Pearson no bordel",
                 "Pearson estava com Abigail e Javier no bordel"],
                ["Javier estava com Abigail e Pearson no bordel and Pearson estava com Abigail e Javier no bordel => Abigail estava com Javier e Pearson no bordel"],
                ints=False
            )

            # Pearson sendo álibi
            # D = "Abigail estava com Javier e Pearson no bordel"
            # E = "Javier estava com Abigail e Pearson no bordel"
            # F = "Pearson estava com Abigail e Javier no bordel"
            # E ^ D -> F

            pearson_validation = ttg.Truths(
                ["Abigail estava com Javier e Pearson no bordel",
                 "Javier estava com Abigail e Pearson no bordel",
                 "Pearson estava com Abigail e Javier no bordel"],
                ["Javier estava com Abigail e Pearson no bordel and Abigail estava com Javier e Pearson no bordel => Pearson estava com Abigail e Javier no bordel"],
                ints=False
            )

            # Sadie sendo álibi
            # G = "Sadie estava no saloon com o Doutor"
            # H = "Doutor estava com Sadie no saloon"
            # H -> G

            sadie_validation = ttg.Truths(
                ["Sadie estava no saloon com o Doutor",
                 "Doutor estava com Sadie no saloon"],
                ["Doutor estava com Sadie no saloon => Sadie estava no saloon com o Doutor"],
                ints=False
            )

            # Leopold sendo álibi
            # B = "Leopold viu Lenny"
            # C = "Lenny viu Leopold"
            # B -> C

            leopold_validation = ttg.Truths(
                ["Leopold viu Lenny",
                 "Lenny viu Leopold"],
                ["Leopold viu Lenny => Lenny viu Leopold"],
                ints=False
            )

            # Doutor sendo álibi
            # G = "Sadie estava no saloon com o Doutor"
            # H = "Doutor estava com Sadie no saloon"
            # G -> H

            doutor_validation = ttg.Truths(
                ["Sadie estava no saloon com o Doutor",
                 "Doutor estava com Sadie no saloon"],
                ["Sadie estava no saloon com o Doutor => Doutor estava com Sadie no saloon"],
                ints=False
            )


            micah_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            sally_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

        # Pearson sendo assassino
        elif murder == "Pearson":
            # Pearson viu Doutor caminhando
            # A = "Pearson viu Doutor caminhando"
            # B = "Sadie estava no saloon com o Doutor"
            # C = "Doutor estava com Sadie no saloon"
            # C ^ B -> ¬A

            pearson_validation = ttg.Truths(
                                            ["Pearson viu Doutor caminhando",
                                             "Sadie estava no saloon com o Doutor",
                                             "Doutor estava com Sadie no saloon"],
                                            [
                                                "Doutor estava com Sadie no saloon and Sadie estava no saloon com o Doutor => not Pearson viu Doutor caminhando"],
                                            ints=False
                                        )

            # Abigail sendo álibi
            # D = "Abigail estava no bordel com Javier"
            # E = "Javier estava no bordel com Abigail"
            # E -> D

            abigail_validation = ttg.Truths(
                                                ["Abigail estava no bordel com Javier",
                                                 "Javier estava no bordel com Abigail"],
                                                ["Javier estava no bordel com Abigail => Abigail estava no bordel com Javier"],
                                                ints=False
                                            )

            # Lenny sendo álibi
            # F = "Leopold viu Lenny"
            # G = "Lenny viu Leopold"
            # F -> G

            lenny_validation = ttg.Truths(
                                            ["Leopold viu Lenny",
                                             "Lenny viu Leopold"],
                                            ["Leopold viu Lenny => Lenny viu Leopold"],
                                            ints=False
                                        )

            # Javier sendo álibi
            # D = "Abigail estava no bordel com Javier"
            # E = "Javier estava no bordel com Abigail"
            # D -> E

            javier_validation = ttg.Truths(
                                        ["Abigail estava no bordel com Javier",
                                         "Javier estava no bordel com Abigail"],
                                        ["Abigail estava no bordel com Javier => Javier estava no bordel com Abigail"],
                                        ints=False)

            # Bill sendo álibi
            # H = "Bill estava com Leopold"
            # I = "Leopold estava com Bill"
            # I  H
            bill_validation = ttg.Truths(["Bill estava com Leopold", "Leopold estava com Bill"],
                                         ["Leopold estava com Bill => Bill estava com Leopold"], ints=False)

            # Sadie sendo álibi
            # B = "Sadie estava no saloon com o Doutor"
            # C = "Doutor estava com Sadie no saloon"
            # C  B
            sadie_validation = ttg.Truths(["Sadie estava no saloon com o Doutor", "Doutor estava com Sadie no saloon"],
                                          ["Doutor estava com Sadie no saloon => Sadie estava no saloon com o Doutor"], ints=False)

            # Leopold sendo álibi
            # H = "Bill estava com Leopold"
            # I = "Leopold estava com Bill"
            # H  I
            leopold_validation = ttg.Truths(["Bill estava com Leopold", "Leopold estava com Bill"],
                                                    ["Bill estava com Leopold => Leopold estava com Bill"], ints=False)

            # Doutor sendo álibi
            # B = "Sadie estava no saloon com o Doutor"
            # C = "Doutor estava com Sadie no saloon"
            # B  C
            doutor_validation = ttg.Truths(["Sadie estava no saloon com o Doutor", "Doutor estava com Sadie no saloon"],
                                           ["Sadie estava no saloon com o Doutor => Doutor estava com Sadie no saloon"], ints=False)

            micah_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            sally_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

        # Sadie sendo assassina
        elif murder == "Sadie":
            # A = "Sadie estava no saloon e viu Pearson no acampamento"
            # B = "Abigail estava com Javier e Pearson no bordel"
            # C = "Javier estava com Abigail e Pearson no bordel"
            # D = "Pearson estava com Abigail e Javier no bordel"
            # D ^ C ^ B  ¬A
            sadie_validation = ttg.Truths(["Sadie estava no saloon e viu Pearson no acampamento", "Abigail estava com Javier e Pearson no bordel", "Javier estava com Abigail e Pearson no bordel", "Pearson estava com Abigail e Javier no bordel"], ["Pearson estava com Abigail e Javier no bordel and Javier estava com Abigail e Pearson no bordel and Abigail estava com Javier e Pearson no bordel => not Sadie estava no saloon e viu Pearson no acampamento"], ints=False)

            # Abigail sendo álibi
            # B = "Abigail estava com Javier e Pearson no bordel"
            # C = "Javier estava com Abigail e Pearson no bordel"
            # D = "Pearson estava com Abigail e Javier no bordel"
            # C ^ D  B
            abigail_validation = ttg.Truths(["Javier estava com Abigail e Pearson no bordel", "Javier estava com Abigail e Pearson no bordel", "Pearson estava com Abigail e Javier no bordel"], ["Javier estava com Abigail e Pearson no bordel and Pearson estava com Abigail e Javier no bordel => Javier estava com Abigail e Pearson no bordel"], ints=False)

            # Lenny sendo álibi
            # E = "Leopold viu Lenny"
            # F = "Lenny viu Leopold"
            # E  F
            lenny_validation = ttg.Truths(["Leopold viu Lenny", "Lenny viu Leopold"],
                                        ["Leopold viu Lenny => Lenny viu Leopold"],
                                                ints=False)

            # Javier sendo álibi
            # B = "Abigail estava com Javier e Pearson no bordel"
            # C = "Javier estava com Abigail e Pearson no bordel"
            # D = "Pearson estava com Abigail e Javier no bordel"
            # B ^ D  C
            javier_validation = ttg.Truths(["Sadie estava com Doutor e Sally no saloon", "Javier estava com Abigail e Pearson no bordel", "Javier estava com Abigail e Pearson no bordel"], ["Abigail estava com Javier e Pearson no bordel and Javier estava com Abigail e Pearson no bordel => Javier estava com Abigail e Pearson no bordel"], ints=False)

            # Bill sendo álibi
            # G = "Bill estava com Leopold no hotel"
            # H = "Leopold estava com Bill no hotel"
            # H  G
            bill_validation = ttg.Truths(["Bill estava com Leopold no hotel",
                                            "Leopold estava com Bill no hotel"], ["Leopold estava com Bill no hotel => Bill estava com Leopold no hotel"], ints=False)

            # Pearson sendo álibi
            # B = "Abigail estava com Javier e Pearson no bordel"
            # C = "Javier estava com Abigail e Pearson no bordel"
            # D = "Pearson estava com Abigail e Javier no bordel"
            # C ^ B  D
            pearson_validation = ttg.Truths(["Abigail estava com Javier e Pearson no bordel",
                                             "Javier estava com Abigail e Pearson no bordel",
                                             "Pearson estava com Abigail e Javier no bordel"], ["Javier estava com Abigail e Pearson no bordel and Abigail estava com Javier e Pearson no bordel => Pearson estava com Abigail e Javier no bordel"], ints=False)

            # Leopold sendo álibi
            # E = "Leopold viu Lenny"
            # F = "Lenny viu Leopold"
            # F  E
            leopold_validation = ttg.Truths(["Leopold viu Lenny", "Lenny viu Leopold"], ["Lenny viu Leopold => Leopold viu Lenny"], ints=False)

            micah_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            doutor_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)
            sally_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

        # Leopold sendo assassino
        elif murder == "Leopold":
            # A = "Leopold estava dormindo"
            # B = "Abigail estava com Javier e Pearson no bordel"
            # C = "Lenny estava com Bill no hotel"
            # D = "Doutor estava com Sadie e Sally no saloon e viu Leopold"
            # E = "Micah estava dormindo no hotel"
            # E ^ D ^ C ^ B  ¬A
            leopold_validation = ttg.Truths(["Leopold estava dormindo", 
                                             "Abigail estava com Javier e Pearson no bordel", 
                                             "Lenny estava com Bill no hotel",
                                             "Doutor estava com Sadie e Sally no saloon e viu Leopold",
                                             "Micah estava dormindo no hotel"], ["Micah estava dormindo no hotel and Doutor estava com Sadie e Sally no saloon e viu Leopold and Lenny estava com Bill no hotel and Abigail estava com Javier e Pearson no bordel => not Leopold estava dormindo"], ints=False)

            # Abigail sendo álibi
            # B = "Abigail estava com Javier e Pearson no bordel"
            # F = "Javier estava com Abigail e Pearson no bordel"
            # G = "Pearson estava com Abigail e Javier no bordel"
            # F ^ G  B
            abigail_validation = ttg.Truths(["Abigail estava com Javier e Pearson no bordel",
                                             "Javier estava com Abigail e Pearson no bordel",
                                             "Pearson estava com Abigail e Javier no bordel"], ["Javier estava com Abigail e Pearson no bordel and Pearson estava com Abigail e Javier no bordel => Abigail estava com Javier e Pearson no bordel"], ints=False)

            # Lenny sendo álibi
            # C = "Lenny estava com Bill no hotel"
            # H = "Bill estava com Lenny no hotel"
            # H  C
            lenny_validation = ttg.Truths(["Lenny estava com Bill no hotel",
                                           "Bill estava com Lenny no hotel"], ["Bill estava com Lenny no hotel => Lenny estava com Bill no hotel"], ints=False)

            # Javier sendo álibi
            # B = "Abigail estava com Javier e Pearson no bordel"
            # F = "Javier estava com Abigail e Pearson no bordel"
            # G = "Pearson estava com Abigail e Javier no bordel"
            # B ^ G  F
            javier_validation = ttg.Truths(["Abigail estava com Javier e Pearson no bordel",
                                            "Javier estava com Abigail e Pearson no bordel",
                                            "Pearson estava com Abigail e Javier no bordel"], ["Abigail estava com Javier e Pearson no bordel and Pearson estava com Abigail e Javier no bordel => Javier estava com Abigail e Pearson no bordel"], ints=False)

            # Bill sendo álibi
            # C = "Lenny estava com Bill no hotel"
            # H = "Bill estava com Lenny no hotel"
            # C  H
            bill_validation = ttg.Truths(["Lenny estava com Bill no hotel",
                                          "Bill estava com Lenny no hotel"], ["Lenny estava com Bill no hotel => Bill estava com Lenny no hotel"], ints=False)

            # Pearson sendo álibi
            # B = "Abigail estava com Javier e Pearson no bordel"
            # F = "Abigail estava com Javier e Pearson no bordel"
            # G = "Pearson estava com Abigail e Javier no bordel"
            # F ^ B  G
            pearson_validation = ttg.Truths(["Abigail estava com Javier e Pearson no bordel", 
                                             "Abigail estava com Javier e Pearson no bordel", 
                                             "Pearson estava com Abigail e Javier no bordel"], ["F and B => G"], ints=False)

            # Sadie sendo álibi
            # D = "Doutor estava com Sadie e Sally no saloon e viu Leopold"
            # I = "Sadie estava com Doutor e Sally no saloon"
            # J = "Sally estava com Doutor e Sadie no saloon"
            # D ^ J  I
            sadie_validation = ttg.Truths(["Doutor estava com Sadie e Sally no saloon e viu Leopold",
                                           "Sadie estava com Doutor e Sally no saloon",
                                            "Sally estava com Doutor e Sadie no saloon"],
                                           ["Doutor estava com Sadie e Sally no saloon e viu Leopold and Sally estava com Doutor e Sadie no saloon => Sadie estava com Doutor e Sally no saloon"], ints=False)

            # Doutor sendo álibi
            # D = "Doutor estava com Sadie e Sally no saloon e viu Leopold"
            # I = "Sadie estava com Doutor e Sally no saloon"
            # J = "Sally estava com Doutor e Sadie no saloon"
            # I ^ J  D
            doutor_validation = ttg.Truths(["Doutor estava com Sadie e Sally no saloon e viu Leopold", "Sadie estava com Doutor e Sally no saloon",
                                            "Sally estava com Doutor e Sadie no saloon"],
                                             ["Sadie estava com Doutor e Sally no saloon and Doutor estava com Sadie e Sally no saloon e viu Leopold => Doutor estava com Sadie e Sally no saloon e viu Leopold"], ints=False)

            # Sally sendo álibi
            # D = "Doutor estava com Sadie e Sally no saloon e viu Leopold"
            # I = "Sadie estava com Doutor e Sally no saloon"
            # J = "Sally estava com Doutor e Sadie no saloon"
            # I ^ D  J
            sally_validation = ttg.Truths(["Doutor estava com Sadie e Sally no saloon e viu Leopold",
                                           "Sadie estava com Doutor e Sally no saloon",
                                           "Sally estava com Doutor e Sadie no saloon"],
                                          ["Sadie estava com Doutor e Sally no saloon and Doutor estava com Sadie e Sally no saloon e viu Leopold => Sally estava com Doutor e Sadie no saloon"], ints=False)

            micah_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

        # Doutor sendo assassino
        elif murder == "Doutor":
            # A = "Doutor viu Sally no acampamento"
            # B = "Sally estava trabalhando no saloon"
            # C = "Sadie estava com Sally no saloon"
            # C ^ B  A
            doutor_validation = ttg.Truths(["Doutor viu Sally no acampamento",
                                            "Sally estava trabalhando no saloon",
                                            "Sadie estava com Sally no saloon"],
                                           ["Sadie estava com Sally no saloon and Sally estava trabalhando no saloon => A"], ints=False)

            # Abigail sendo álibi
            # D = "Abigail estava com Javier e Pearson no bordel"
            # E = "Javier estava com Abigail e Pearson no bordel"
            # F = "Pearson estava com Abigail e Javier no bordel"
            # E ^ F  D
            abigail_validation = ttg.Truths(["Abigail estava com Javier e Pearson no bordel",
                                             "Javier estava com Abigail e Pearson no bordel",
                                             "Pearson estava com Abigail e Javier no bordel"], ["Javier estava com Abigail e Pearson no bordel and Pearson estava com Abigail e Javier no bordel => Abigail estava com Javier e Pearson no bordel"], ints=False)

            # Lenny sendo álibi
            # G = "Lenny estava com Bill e Leopold no hotel"
            # H = "Bill estava com Lenny e Leopold no hotel"
            # J = "Leopold estava com Bill e Lenny no hotel"
            # H ^ J  G
            lenny_validation = ttg.Truths(["Lenny estava com Bill e Leopold no hotel",
                                           "Bill estava com Lenny e Leopold no hotel",
                                           "Leopold estava com Bill e Lenny no hotel"],
                                          ["Bill estava com Lenny e Leopold no hotel and Leopold estava com Bill e Lenny no hotel => Lenny estava com Bill e Leopold no hotel"], ints=False)

            # Javier sendo álibi
            # D = "Abigail estava com Javier e Pearson no bordel"
            # E = "Javier estava com Abigail e Pearson no bordel"
            # F = "Pearson estava com Abigail e Javier no bordel"
            # D ^ F  E
            javier_validation = ttg.Truths(["Abigail estava com Javier e Pearson no bordel",
                                            "Abigail estava com Javier e Pearson no bordel",
                                            "Pearson estava com Abigail e Javier no bordel"],
                                           ["Abigail estava com Javier e Pearson no bordel and Pearson estava com Abigail e Javier no bordel => Javier estava com Abigail e Pearson no bordel"], ints=False)

            # Bill sendo álibi
            # G = "Lenny estava com Bill e Leopold no hotel"
            # H = "Bill estava com Lenny e Leopold no hotel"
            # J = "Leopold estava com Bill e Lenny no hotel"
            # G ^ J  H
            bill_validation = ttg.Truths(["Lenny estava com Bill e Leopold no hotel",
                                          "Bill estava com Lenny e Leopold no hotel",
                                          "Leopold estava com Bill e Lenny no hotel"],
                                         ["Lenny estava com Bill e Leopold no hotel and Leopold estava com Bill e Lenny no hotel => Bill estava com Lenny e Leopold no hotel"], ints=False)

            # Pearson sendo álibi
            # D = "Abigail estava com Javier e Pearson no bordel"
            # E = "Javier estava com Abigail e Pearson no bordel"
            # F = "Pearson estava com Abigail e Javier no bordel"
            # E ^ D  F
            pearson_validation = ttg.Truths(["Abigail estava com Javier e Pearson no bordel",
                                             "Javier estava com Abigail e Pearson no bordel",
                                             "Pearson estava com Abigail e Javier no bordel"],
                                            ["Javier estava com Abigail e Pearson no bordel and Abigail estava com Javier e Pearson no bordel => Pearson estava com Abigail e Javier no bordel"], ints=False)

            # Sadie sendo álibi
            # D = "Sally estava trabalhando no saloon"
            # I = "Sadie estava com Sally no saloon"
            # D  I
            sadie_validation = ttg.Truths(["Sally estava trabalhando no saloon",
                                           "Sadie estava com Sally no saloon"],
                                          ["Sally estava trabalhando no saloon => Sadie estava com Sally no saloon "], ints=False)

            # Leopold sendo álibi
            # G = "Lenny estava com Bill e Leopold no hotel"
            # H = "Bill estava com Lenny e Leopold no hotel"
            # J = "Leopold estava com Bill e Lenny no hotel"
            # G ^ H  J
            leopold_validation = ttg.Truths(["Lenny estava com Bill e Leopold no hotel",
                                             "Bill estava com Lenny e Leopold no hotel",
                                             "Leopold estava com Bill e Lenny no hotel"],
                                            ["Lenny estava com Bill e Leopold no hotel and ny e Leopold no hotel => Leopold estava com Bill e Lenny no hotel"], ints=False)

            # Sally sendo álibi
            # D = "Sally estava trabalhando no saloon"
            # I = "Sadie estava com Sally no saloon"
            # I  D
            sally_validation = ttg.Truths(["Sally estava trabalhando no saloon",
                                           "Sadie estava com Sally no saloon"],
                                          ["Sadie estava com Sally no saloon =>Sally estava trabalhando no saloon "], ints=False)

            micah_validation = ttg.Truths(["Possui Álibi"], ["Possui Álibi"], ints=False)

    return abigail_validation, bill_validation, doutor_validation, javier_validation, lenny_validation, leopold_validation, micah_validation, pearson_validation, sadie_validation, sally_validation

abigail_validation, bill_validation, doutor_validation, javier_validation, lenny_validation, leopold_validation, micah_validation, pearson_validation, sadie_validation, sally_validation = deductions()


def first_val(val):
    df = val.as_pandas
    first_row = df.iloc[0]
    return first_row


#menu de impressão de tabelas verdade
# ['Micah', 'Abigail', 'Lenny', 'Javier', 'Bill', 'Pearson', 'Sadie', 'Leopold', 'Doutor', 'Sally']
#    0          1          2      3        4         5        6          7          8        9
def get_table_truth():
    print("Qual validação você quer ver? ")
    print(f"1 -  {list(suspects.keys())[0]}\n"
          f"2 -  {list(suspects.keys())[1]}\n"
          f"3 -  {list(suspects.keys())[2]}\n"
          f"4 -  {list(suspects.keys())[3]}\n"
          f"5 -  {list(suspects.keys())[4]}\n"
          f"6 -  {list(suspects.keys())[5]}\n"
          f"7 -  {list(suspects.keys())[6]}\n"
          f"8 -  {list(suspects.keys())[7]}\n"
          f"9 -  {list(suspects.keys())[8]}\n"
          f"10 - {list(suspects.keys())[9]}\n")

    ans = input("Digite a opção: ")

    try:
        ans = int(ans)

        # 0 - Micah
        if ans == 1:
            print("Validação do álibi do Micah")
            print(pista_micah)
            print(micah_validation)
            print(" ")
            print(first_val(micah_validation))

        # 1 - Abigail
        elif ans == 2:
            print("Validação do álibi da Abigail")
            print(pista_abigail)
            print(abigail_validation)
            print(" ")
            print(first_val(abigail_validation))

        # 2 - Lenny
        elif ans == 3:
            print("Validação do álibi do Lenny")
            print(pista_lenny)
            print(lenny_validation)
            print(" ")
            print(first_val(lenny_validation))

        # 3 - Javier
        elif ans == 4:
            print("Validação do álibi do Javier")
            print(pista_javier)
            print(javier_validation)
            print(" ")
            print(first_val(javier_validation))

        # 4 - Bill
        elif ans == 5:
            print("Validação do álibi do Bill")
            print(pista_bill)
            print(bill_validation)
            print(" ")
            print(first_val(bill_validation))

        # 5 - Pearson
        elif ans == 6:
            print("Validação do álibi do Pearson")
            print(pista_pearson)
            print(pearson_validation)
            print(" ")
            print(first_val(pearson_validation))

        # 6 - Sadie
        elif ans == 7:
            print("Validação do álibi da Sadie")
            print(pista_sadie)
            print(sadie_validation)
            print(" ")
            print(first_val(sadie_validation))

        # 7 - Leopold
        elif ans == 8:
            print("Validação do álibi do Leopold")
            print(pista_leopold)
            print(leopold_validation)
            print(" ")
            print(first_val(leopold_validation))

        # 8 - Doutor
        elif ans == 9:
            print("Validação do álibi do Doutor")
            print(pista_doutor)
            print(doutor_validation)
            print(" ")
            print(first_val(doutor_validation))

        # 9 - Sally
        elif ans == 10:
            print("Validação do álibi da Sally")
            print(pista_sally)
            print(sally_validation)
            print(" ")
            print(first_val(sally_validation))

        else:
            print("Opção indisponível, tente novamente...")
            get_table_truth()  # Chama a função novamente

    except ValueError:
        print("Entrada inválida... Por favor, digite um número.")
        get_table_truth()  # Chama a função novamente


def final_valid():
    # Pergunta se deseja ver outra validação
    print("Deseja ver outra validação?")
    print("1 - Sim")
    print("2 - Não")

    try:
        ans = input("Digite a opção: ")
        ans = int(ans)

        if ans == 1:
            get_table_truth()  # Chama a função novamente
            final_valid()
        elif ans == 2:
            menu2()  # Substitua por sua função para voltar ao menu
        else:
            print("Opção indisponível, tente novamente...")
            get_table_truth() # Chama a função novamente

    except ValueError:
        print("Entrada inválida... Por favor, digite um número.")
        get_table_truth()  # Chama a função novamente


validations = {
    'pista_micah': micah_validation,
    'pista_abigail': abigail_validation,
    'pista_lenny': lenny_validation,
    'pista_pearson': pearson_validation,
    'pista_leopold': leopold_validation,
    'pista_sadie': sadie_validation,
    'pista_javier': javier_validation,
    'pista_sally': sally_validation,
    'pista_bill': bill_validation,
    'pista_doutor': doutor_validation
}

deductions_collection = []

#chamar a dedução
def get_deduction(b):
    global deductions_collection
    ded = validations.get(b)
    if ded is not None and ded not in deductions_collection:
        deductions_collection.append(ded)


#fazer acusação
def make_acc():
    print("\nXerife Arthur: Espero que tenha certeza de quem você vai acusar...")
    print("Xerife Arthur: Esses são os suspeitos: ")
    for i, suspect in enumerate(suspects.keys(), start=1):
        print(f"{i} - Acusar {suspect}")
    print("11 - Voltar à delegacia e analisar os próximos passos")

    ans = input("Xerife Arthur: Quem você quer acusar? ")

    try:
        ans = int(ans)
        if 1 <= ans <= len(suspects):
            if list(suspects.keys())[ans - 1] == murder:
                print("\nXerife Arthur: Bom trabalho!! Você encontrou o assassino, vou visitá-lo com um mandado de prisão, obrigada!")
                get_table_truth()
            else:
                print("\nXerife Arthur: Esse não é o assassino. O caso encerrou, o assassino confessou o crime antes de você o encontrar.")
                print(f"{murder} assassinou Dutch.\n")
                get_table_truth()

        elif ans == 11:
            menu2()

        else:
            print("Xerife Arthur: Não entendi, pode repetir? ")

    except ValueError:
        print("Xerife Arthur: Por favor, digite um número válido.")
        make_acc()

collection_clues = {}

def process_clue(a, name):
    global collection_clues
    collection_clues[name] = a
    get_deduction(a)


start()
menu1()

