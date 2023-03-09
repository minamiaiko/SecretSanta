#!usr/bin/env python3
import unittest

from context import secret_santa_mailer as ssm

class EmailTests(unittest.TestCase):

    def test_valid_basic(self):
        email = 'valid@examplecompany.gov'

        self.assertTrue(ssm.is_email_valid(email))

    def test_valid_basic_with_plus(self):
        email = 'john+valid@examplecompany.gov'

        self.assertTrue(ssm.is_email_valid(email))

    def test_valid_complex(self):
        email = 'john.valid+lab777@example-company.gov'

        self.assertTrue(ssm.is_email_valid(email))

    def test_valid_domain(self):
        email = 'john.VALID+lab777@EXAMPLE-COMPANY.GOV'

        self.assertTrue(ssm.is_email_valid(email))

    def test_valid_tree_sufix(self):
        email = 'valid@examplecompany.co.gov'
        
        self.assertTrue(ssm.is_email_valid(email))

    def test_invalid_basic(self):
        email = 'invalidemail.gov'

        self.assertFalse(ssm.is_email_valid(email))

    def test_invalid_bad_chars(self):
        email = 'invalid email here@examplecompany.gov'

        self.assertFalse(ssm.is_email_valid(email))

    def test_invalid_tld(self):
        email = 'invalid-email@examplecompany{}.gov'

        self.assertFalse(ssm.is_email_valid(email))


if __name__ == '__main__':
    unittest.main()
