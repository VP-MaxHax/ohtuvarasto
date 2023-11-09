import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_kaikki_mita_voidaan(self):
        self.varasto.lisaa_varastoon(4)

        saatu_maara = self.varasto.ota_varastosta(8)

        self.assertEqual(saatu_maara, 4)

    def test_varastoon_ei_voida_laittaa_liikaa(self):
        self.varasto.lisaa_varastoon(15)

        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_varaston_tyhjennys_ei_vie_saldoa_negatiiviseksi(self):
        self.varasto.lisaa_varastoon(4)

        self.varasto.ota_varastosta(8)

        self.assertEqual(self.varasto.saldo, 0)

    def test_varastoo_ei_voi_lisata_negatiivista_maaraa(self):

        self.varasto.lisaa_varastoon(-4)

        self.assertEqual(self.varasto.saldo, 0)

    def test_varaston_saldon_oikea_tulostus_muoto(self):
        self.varasto.lisaa_varastoon(3)

        self.assertEqual(str(self.varasto), f"saldo = {self.varasto.saldo}, \
        vielä tilaa {self.varasto.paljonko_mahtuu()}")

    def test_varaston_koko_nolla(self):
        varasto = Varasto(0)

        self.assertEqual(varasto.tilavuus, 0.0)

    def test_ei_voi_ottaa_tyhjasta_varastosta(self):
        self.varasto.ota_varastosta(5)

        self.assertEqual(self.varasto.saldo, 0.0)

    def test_alku_saldo_negatiivinen(self):
        varasto = Varasto(10, -5)

        self.assertEqual(varasto.saldo, 0.0)

    def test_alku_saldo_yli_maksimin(self):
        varasto = Varasto(10, 15)

        self.assertEqual(varasto.saldo, 10)

    def test_otetaan_negatiivisesta_saldosta(self):
        self.varasto.lisaa_varastoon(5)

        saatu_maara = self.varasto.ota_varastosta(-5)

        self.assertEqual(saatu_maara, 0.0)
