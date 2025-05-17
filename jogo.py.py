print ("""
    Você chegou ao Asilo Oswald, uma instituição de saúde mental especializada em crianças que sofreram traumas graves, 
    logo uma enfermeira se aproxima para coletar alguns dados sobre você e dar início ao tratamento.
""")

jogador = input('Enfermeira - Por gentileza informe seu nome: ') 
print (f'Enfermeira - Prazer {jogador}, sou a enfermeira Fernanda.')
idade = int(input('Enfermeira - Para finalizarmos o cadastro me informe sua idade: '))

if idade < 12:
    print('Oooops, parece que você é novo demais para jogar este jogo :/')
    
else:
    print(f"""
    Enfermeira - Perfeito! Poderia por gentileza me acompanhar até a sala do Dr. Osvald.
          
    Ao chegar ao consultório do Dr. Osvald, ele o convida a se sentar e começa a se apresentar.
          
    Dr. Osvald – Olá, {jogador}. Sou o Dr. Osvald, e estarei cuidando de você a partir de agora. Dei uma olhada no seu histórico 
    e percebi que você passou por algumas situações difíceis. Pode confiar em mim, estou aqui para te ajudar.
    Vou te receitar um medicamento que deve te fazer sentir melhor e mais tranquilo.

    Dr. Osvald – Tenho o remédio aqui comigo. Você prefere tomá-lo agora ou gostaria de ir para o seu quarto primeiro?
    """)
while True:
    remedio = ""
    while remedio not in ["1", "2"]: #while para escolher pilula
        print("Escolha uma opção:")
        print("1 - Tomar o remédio agora")
        print("2 - Ir para o quarto")
        remedio = input("> ")
    
    if remedio == "1":
        print("""
            Você decidiu tomar o remédio. Pouco depois, a enfermeira Fernanda o acompanhou até seu quarto.
            No entanto, ao se deitar e tentar relaxar, algo estranho começou a acontecer...
              
            Sua visão ficou turva, os sons ao redor pareciam distantes — e, de repente, você começou a ter alucinações.
            Diante de seus olhos, surgiram dois espíritos.""") 
        
    
        espiritos = ""
        while espiritos not in ["1", "2", "3"]: #while para escolher o espíritos
            print(f"""
                Os espíritos começaram a se aproximar, falando com você ao mesmo tempo.
                Um parecia calmo e triste.
                O outro, agitado e intenso.
                Mas, {jogador}, você só pode conversar com um deles. Qual você escolhe?""") 
            print("1 – O espírito calmo e melancólico.")
            print("2 – O espírito agitado e inquieto.")
            print("3 - Não quero conversar com ninguém.")
            espiritos = input("> ")  

        if espiritos == "1": 
            print(f"""
                Espírito Calmo - Olá {jogador}, me chamo Remor, vou te ajudar a sair desse lugar
                Espírito Calmo – {jogador}, o Dr. Osvald é muito mais perigoso do que aparenta. Ele vai fazer de tudo para manter você preso aqui... para sempre.  
                Mas não se preocupe — eu vou te ajudar. Descobri uma passagem secreta na sala de cirurgia. Venha comigo. A enfermeira esqueceu de trancar a porta do seu quarto.

                --- VOCÊ ENTRA NA SALA DE CIRURGIA ---

                Espírito Calmo – Ali! Aquela é a saída! É por onde eles descartam os corpos... cai direto num túnel que leva para fora.

                --- BARULHO DE PASSOS SE APROXIMANDO ---

                Dr. Osvald – {jogador}, o que você está fazendo aqui?

                Agora você precisa agir rápido.  
                Você vê duas coisas ao seu alcance: um alicate e um bisturi.
            """)  # espíritos bom

            instrumento = ""
            while instrumento not in ["1", "2", "3"]: #while para escolher o instrumento
                print("Qual você escolhe?")
                print("1 - Alicate.")
                print("2 - Bisturi.")
                print("3 - Não quero pegar.")
                instrumento = input("> ")

            if instrumento == "1":
                print(f"""
                {jogador}, Em vez de pegar o bisturi, você escolheu o alicate — uma ferramenta inútil naquele momento.  
                      
                Sem conseguir se defender, o Dr. Osvald agiu rapidamente.  
                Ele te imobilizou com facilidade e, em poucos segundos, você já estava preso em uma camisa de força.

                Agora, trancado, você percebe a verdade cruel:  
                Você nunca mais sairá deste lugar.

                Sinto muito, {jogador}...""")
                reiniciar = input("Deseja recomeçar o jogo? (sim/não): ").strip().lower()
                if reiniciar != "sim":
                    print("Obrigado por jogar! Até a próxima.")
                    break 

            elif instrumento == "2":
                print(f"""
                Você fez a escolha certa, {jogador}.
                      
                Com o bisturi em mãos, conseguiu se defender do Dr. Osvald no momento exato.  
                Em meio à luta, acabou ferindo-o mortalmente. Ele caiu, sem forças para impedi-lo.

                Sem perder tempo, você correu até a passagem secreta que o espírito Ramor havia mostrado.  
                Atravessou o túnel escuro... e, finalmente, saiu do Asilo Oswald.

                Você está livre. Parabéns, {jogador}!""")
            else:
                print(f"Meus sentimentos, {jogador} você foi descoberto, agora ficará para sempre no Asilo Oswald - BOA SORTE!.")
                reiniciar = input("Deseja recomeçar o jogo? (sim/não): ").strip().lower()
                if reiniciar != "sim":
                    print("Obrigado por jogar! Até a próxima.")
                    break

        elif espiritos == "2": 
            print(f"""
                Espirito agitado - Olá {jogador}, me chamo Sulzbach, vou te ajudar a sair desse lugar.
                Espirito agitado - VAMOS SAIR AGORA DAQUI O DR. OSVALD VAI TE MATAR!!! Vou te levar para um lugar seguro.
                
                O Sulzbach te guia até chegar na sala de cirurgia, indicabdo que ali é a melhor saída secreta da instituição.
                  
                Espirito agitado - Ali!Ali! Na cadeira, sentando nela você vai conseguir se teletransportar para fora dessa clínica!
                
                E agora o que você vai fazer?
                """) # Fantasma ruim
            
            cadeira = ""
            while cadeira not in ["1", "2"]: #while para escolher se ele irá acreditar ou não no espírito Sulzbach
                print("1 - Acreditar no Sulzbach")
                print("2 - Não acreditar no Sulzbach")
                cadeira = input("> ")
                if cadeira == "1":
                    print(f"""
                    {jogador}, você resolveu acreditar no Sulzbach, ele te influenciou a sentar em uma cadeira, porém não era apenas uma cadeira normal.
                          
                    ERA UMA CADEIRA ELÉTRICA.
                          
                    O espírito ligou a cadeira afirmando que sairia daquela clínica, ele estava certo. Você morreu e foi parar nacidade dos pés juntos""")
                    reiniciar = input("Deseja recomeçar o jogo? (sim/não): ").strip().lower()
                    if reiniciar != "sim":
                        print("Obrigado por jogar! Até a próxima.")
                        break
                else:
                    print(f"""
                    {jogador}, você resolveu não acreditar no Sulzbach, ele ficou furioso com sua decisão, assim ele decide se abitar em seu corpo.
                          
                    VOCÊ FOI POSSUÍDO!
                          
                    Assim teve mudanças de voz, comportamento, força física incomum, o Dr. Oswald chegou na sala, viu sua situação e chamou todos da clínica para te conter.
                    Colocam em uma camisa de força e te coloca em uma sala com condições desumanas de se habitar. 
                        
                    {jogador}, você ficará nesse local para sempre junto ao seu maior inimigo Sulzbach.""")  
                    reiniciar = input("Deseja recomeçar o jogo? (sim/não): ").strip().lower()
                    if reiniciar != "sim":
                        print("Obrigado por jogar! Até a próxima.")
                        break 
        else:
            print(f"{jogador},você não terá nenhuma ajuda e viverá para sempre no Asilo Oswald - BOA SORTE!.")  
            reiniciar = input("Deseja recomeçar o jogo? (sim/não): ").strip().lower()
            if reiniciar != "sim":
                print("Obrigado por jogar! Até a próxima.")
                break
    else:
        print(f"""
        {jogador}, infelizmente você optou por não tomar a pilula, por conta disso você foi diressionado até um quarto brando pela enfermeira Fernanda.
        Esse quarto está apenas você e seus pensamentos, pois ele é fechado por quatro paredes todas completamentes brancas sem nenhum acesso a parte externa dele, 
        apenas uma janelinha onde recebe suprimentos básicos.
        Com o passar dos dias você chega a loucura junto com seus pensamentos, diante dessa situação o Dr. Oswald decidiu lhe fazer uma lobotomia, fazendo você ficar em estado vegetativo.
              
        Sinto muito! """)

        reiniciar = input("Deseja recomeçar o jogo? (sim/não): ").strip().lower()
        if reiniciar != "sim":
            print("Obrigado por jogar! Até a próxima.")
            break