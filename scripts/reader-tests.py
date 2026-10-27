"""Regression checks for native equation markup and stable manuscript anchors."""
import unittest

from lxml import html

from build_reader import add_alias, validate_mathml


FORMULA = '''<math xmlns="http://www.w3.org/1998/Math/MathML"><mrow>
<mstyle class="label" id="equation-label"></mstyle>
<msub><mi>A</mi><mi>t</mi></msub></mrow></math>'''


class MathMarkupTests(unittest.TestCase):
    def test_equation_alias_is_outside_math_and_table(self):
        tree = html.fromstring('<div><table class="equation"><tr><td>'
                               + FORMULA + '</td></tr></table></div>')
        add_alias(tree.get_element_by_id("equation-label"), "eq:policy")
        alias = tree.get_element_by_id("eq:policy")
        self.assertEqual(alias.getparent(), tree)
        self.assertEqual(alias.getnext().tag, "table")
        self.assertEqual(len(tree.xpath(".//math//msub")), 1)
        validate_mathml(tree)

    def test_inline_formula_alias_is_outside_math(self):
        tree = html.fromstring('<p>' + FORMULA + '</p>')
        add_alias(tree.get_element_by_id("equation-label"), "eq:inline")
        self.assertEqual(tree.get_element_by_id("eq:inline").getnext().tag, "math")
        validate_mathml(tree)

    def test_html_span_inside_math_is_rejected(self):
        tree = html.fromstring('<div>' + FORMULA.replace('<mrow>',
                               '<mrow><span id="eq:broken"></span>') + '</div>')
        with self.assertRaisesRegex(ValueError, "Non-MathML element"):
            validate_mathml(tree)

    def test_namespace_reset_inside_math_is_rejected(self):
        tree = html.fromstring('<div>' + FORMULA.replace('<msub>',
                               '<msub xmlns="">') + '</div>')
        with self.assertRaisesRegex(ValueError, "Non-MathML element"):
            validate_mathml(tree)


if __name__ == "__main__":
    unittest.main()
