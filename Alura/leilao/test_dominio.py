from unittest import TestCase
from dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):
    def test_avalia(self):
        henrique = Usuario('Henrique')
        yuri = Usuario('Yuri')

        lance_do_henrique = Lance(henrique, 100.0)
        lance_do_yuri = Lance(yuri, 200.0)

        leilao = Leilao('Celular')
        leilao.lances.append(lance_do_henrique)
        leilao.lances.append(lance_do_yuri)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100
        maior_valor_esperado = 200

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)