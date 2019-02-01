
if __name__ == "__main__":

    from Orcamento import Orcamento, CalculadorDeImpostos
    from Impostos import calcula_ISS, calcula_ICMS, cacula_ICPP


    calculador = CalculadorDeImpostos()
    orcamento = Orcamento(500)

    calculador.realiza_calculo(orcamento, calcula_ISS)
    calculador.realiza_calculo(orcamento, calcula_ICMS)
    calculador.realiza_calculo(orcamento, cacula_ICPP)