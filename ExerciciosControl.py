import this
import ExerciciosModel
this.opcao = -1

def Menu():
    print('Menu\n\n'    +
        '\n1. Exercício 01' +
        '\n2. Execício  02' +
        '\n3. Exercício 03' +
        '\n4. Exercício 04' +
        '\n5. Exercício 05' +
        '\n6. Exercício 06' +
        '\n7. Exercício 07' +
        '\n8. Exercício 08' +
        '\n9. Exercício 09' +
        '\n0. Sair'         +
        '\nEscolha uma das opções acima: ')
    this.opcao = int(input())

def Executar():
        while(this.opcao != 0):
            Menu()
            if this.opcao == 0:
                print('Obrigado!')
            elif this.opcao == 1:
                print(ExerciciosModel.exercicio01())
            elif this.opcao == 2:
                num1 = int(input('Digite o primeiro valor'))
                print(ExerciciosModel.exercicio02(num1))
            elif this.opcao == 3:
                print(ExerciciosModel.exercicio03())
            elif this.opcao == 4:
                print('informe sua idade em anos, meses e dias:')
                print(ExerciciosModel.exercicio04())
            elif this.opcao == 5:
                print(ExerciciosModel.exercicio05())
            elif this.opcao == 6:
                print(ExerciciosModel.exercicio06())
            elif this.opcao == 7:
                print(ExerciciosModel.exercicio07())
            elif this.opcao == 8:
                print(ExerciciosModel.exercicio08())
            elif this.opcao == 9:
                print(ExerciciosModel.exercicio09())


            else:
                print('Opção informada não é valida!')


