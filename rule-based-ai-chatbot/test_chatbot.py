import unittest
from chatbot import sanitize, get_response, RESPONSES, FALLBACK, EXIT_COMMANDS


class TestSanitize(unittest.TestCase):
    def test_case_and_whitespace(self):
        self.assertEqual(sanitize("  HeLLo  "), "hello")

    def test_trailing_punctuation(self):
        self.assertEqual(sanitize("Hello!"), "hello")
        self.assertEqual(sanitize("How are you?"), "how are you")

    def test_inner_spaces_collapsed(self):
        self.assertEqual(sanitize("what   is   ai"), "what is ai")

    def test_empty(self):
        self.assertEqual(sanitize("   "), "")


class TestResponses(unittest.TestCase):
    def test_known_intent(self):
        self.assertEqual(get_response("hello"), RESPONSES["hello"])

    def test_fallback(self):
        self.assertEqual(get_response("asdfgh"), FALLBACK)

    def test_at_least_five_intents(self):
        self.assertGreaterEqual(len(RESPONSES), 5)

    def test_exit_commands_not_in_knowledge_base(self):
        self.assertTrue(EXIT_COMMANDS.isdisjoint(RESPONSES))


if __name__ == "__main__":
    unittest.main()
