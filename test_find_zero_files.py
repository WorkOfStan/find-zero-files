import io
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from find_zero_files import GRAY, RED, RESET, colored, scan


class ScanSampleTest(unittest.TestCase):
    def test_ignores_google_document_extensions(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "document.gdoc").write_bytes(b"\0" * 16)
            (root / "table.GSHEET").write_bytes(b"\0" * 16)
            output = io.StringIO()

            with redirect_stdout(output):
                found = scan(root)

            result = output.getvalue()
            self.assertNotIn("document.gdoc", result)
            self.assertNotIn("table.GSHEET", result)
            self.assertIn("Souborů v pořádku: 0", result)
            self.assertIn("Nalezeno podezřelých souborů: 0", result)
            self.assertEqual([], found)

    def test_terminal_colors(self):
        with patch("sys.stdout.isatty", return_value=True):
            self.assertEqual(f"{GRAY}OK{RESET}", colored("OK", GRAY))
            self.assertEqual(f"{RED}PODEZŘELÝ{RESET}", colored("PODEZŘELÝ", RED))

    def test_reports_good_and_suspicious_pdf(self):
        sample = Path(__file__).parent / "sample"
        output = io.StringIO()

        with redirect_stdout(output):
            found = scan(sample)

        result = output.getvalue()
        self.assertIn("OK:", result)
        self.assertIn("test.pdf", result)
        self.assertIn("PODEZŘELÝ:", result)
        self.assertIn("190523_Smlouva_EMPTY.pdf", result)
        self.assertIn("Souborů v pořádku: 1", result)
        self.assertEqual([sample / "190523_Smlouva_EMPTY.pdf"], found)


if __name__ == "__main__":
    unittest.main()
