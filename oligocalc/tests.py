from django.test import TestCase, Client
from django.urls import reverse

from . import views
from . import forms


# ───────────────────────────────────────────
# 1. Calculator (CalcView)
# ───────────────────────────────────────────
class CalcViewLoadTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_renders_calculator(self):
        resp = self.client.get(reverse('oligocalc:calculator'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'oligocalc/calculator.html')


class CalcViewAlgorithmTests(TestCase):
    def setUp(self):
        self.view = views.CalcView()
        self.form = forms.CalcForm(data={
            "sequence": "CCCCGCGAGCACAGA",
            "btnradio": "dna",
            "volume": 10,
            "absorbance260": 1.0,
            "mv_conc": 50,
            "dv_conc": 3,
            "dntp_conc": 0.8,
            "dna_conc": 0.2,
            "target": "dna",
            "param_set": "qPCR",
        })
        self.assertTrue(self.form.is_valid())

    def test_sequence_properties_with_known_sequence(self):
        result = self.view.calculate_results(self.form)
        self.assertAlmostEqual(result['melting_t'], 63.4, delta=0.1)
        self.assertAlmostEqual(result['concentration_molar'], 7.0, delta=0.1)
        self.assertAlmostEqual(result['concentration_mass'], 31.8, delta=0.1)
        self.assertAlmostEqual(result['quantity'], 70.2, delta=0.1)
        self.assertEqual(result['sequence_dna_rev_compl'], 'TCTGTGCTCGCGGGG')
        self.assertEqual(result['epsilon260'], 142400)
        self.assertEqual(result['length'], 15)
        self.assertAlmostEqual(result['mass_monoisotopic'], 4529.809, delta=0.001)
        self.assertAlmostEqual(result['mass_average'], 4532.0, delta=0.1)
        self.assertEqual(result['brutto_formula'], 'C143H181N61O84P14')


# ───────────────────────────────────────────
# 2. TaqMan Finder (TaqManFindView)
# ───────────────────────────────────────────
class TaqManFindViewTests(TestCase):
    def setUp(self):
        self.fasta = (
            '>ACTB_truncated\n'
            'ACCGCCGAGACCGCGTCCGCCCCGCGAGCACAGAGCCTCGCCTTTGCCGATCCGCCGCCCGTCCACACCCGCCGCCAGCTCACCATGGATGATGATATCGCCGCGCTCGTCGTCGACAACGGCTCCGGCATGTGCAAGGCCGGCTTCGCGGGCGACGATGCCCCCCGGGCCGTCTTCCCCTCCATCGTGGGGCGCCCCAGGCACCAGGGC'
        )
        self.payload = {
            'fasta': self.fasta,
            'primer1': 4529.8,
            'primer2': 5909.0,
            'probe':   6023.1,
            'probe_dye': 'VIC-MGB',
            'amp_size': 171,
        }
        self.url = reverse('oligocalc:taqman_find')

    def test_post_with_data_returns_non_empty_results(self):
        response = self.client.post(self.url, self.payload, follow=True)
        self.assertEqual(response.status_code, 200)
        context = response.context[0]

        self.assertIn('results', context)
        self.assertIsInstance(context['results'], list)
        self.assertEqual(len(context['results']), 1)

        seqF_seq, seqF_pos, *_rest = context['results'][0]
        self.assertIsInstance(seqF_seq, str)
        self.assertIsInstance(seqF_pos, int)


# ───────────────────────────────────────────
# 3. siRNA Scan & Score (SirnaScoreView)
# ───────────────────────────────────────────
class SirnaScoreViewTests(TestCase):
    def setUp(self):
        self.fasta = (
            ">74mer\n"
            "AUGGUGAGCAAGGGCGAGGAGCUAUGGCGUGCUGAUCAUGGUGAGCAAGGGCGAGGAGCUAUGGCGUGCUGAUC"
        )
        self.url = reverse('oligocalc:sirna_score')

    def test_long_transcript_returns_both_candidate_lists(self):
        response = self.client.post(self.url, {'fasta': self.fasta}, follow=True)
        self.assertEqual(response.status_code, 200)

        ctx = response.context[0]
        self.assertIn('sirna_19_list', ctx)
        self.assertIn('sirna_21_list', ctx)

        self.assertIsInstance(ctx['sirna_19_list'], list)
        self.assertIsInstance(ctx['sirna_21_list'], list)
        self.assertGreater(len(ctx['sirna_19_list']), 0)
        self.assertGreater(len(ctx['sirna_21_list']), 0)

        first_19 = ctx['sirna_19_list'][0]
        self.assertEqual(len(first_19), 12)

        first_21 = ctx['sirna_21_list'][0]
        self.assertEqual(len(first_21), 11)
