def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    def calc_digito(cpf, digito):
        soma = sum(int(cpf[i]) * (digito + 1 - i) for i in range(digito))
        resto = (soma * 10) % 11
        return 0 if resto == 10 else resto

    d1 = calc_digito(cpf, 9)
    d2 = calc_digito(cpf, 10)
    return d1 == int(cpf[9]) and d2 == int(cpf[10])

def main():
    print("=== Validador Simples de CPF ===")
    cpf = input("Digite o CPF (com ou sem pontos e traço): ").strip()
    if validar_cpf(cpf):
        print("CPF válido!")
    else:
        print("CPF inválido!")

if __name__ == "__main__":
    main()
