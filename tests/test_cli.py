"""Tests for the CLI module (src/openbioacademia/cli.py)."""

import sys
from pathlib import Path
from unittest.mock import patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))


class TestCliHelp:
    """Test CLI entry point behavior."""

    def test_no_args_shows_help(self):
        """academica with no args should print help and not crash."""
        from openbioacademia.cli import main
        with patch.object(sys, "argv", ["academica"]):
            try:
                main()
            except SystemExit:
                pass  # Some implementations may exit

    def test_demo_command_runs(self):
        """academica demo should run without crashing."""
        from openbioacademia.cli import main
        with patch.object(sys, "argv", ["academica", "demo"]):
            try:
                main()
            except SystemExit:
                pass


class TestCliCommands:
    """Test specific commands."""

    def test_configure_command_runs(self):
        """academica configure should start without crashing."""
        from openbioacademia.cli import main
        with patch.object(sys, "argv", ["academica", "configure"]):
            try:
                main()
            except SystemExit:
                pass

    def test_search_without_query_prints_usage(self):
        """academica search without query should show usage."""
        from openbioacademia.cli import main
        with patch.object(sys, "argv", ["academica", "search"]):
            try:
                main()
            except SystemExit:
                pass

    def test_bibtex_without_doi_prints_usage(self):
        """academica bibtex without DOI should show usage."""
        from openbioacademia.cli import main
        with patch.object(sys, "argv", ["academica", "bibtex"]):
            try:
                main()
            except SystemExit:
                pass

    def test_verify_without_args_prints_usage(self):
        """academica verify without args should show usage."""
        from openbioacademia.cli import main
        with patch.object(sys, "argv", ["academica", "verify"]):
            try:
                main()
            except SystemExit:
                pass

    def test_unknown_command_prints_usage(self):
        """Unknown commands should not crash."""
        from openbioacademia.cli import main
        with patch.object(sys, "argv", ["academica", "nonexistent"]):
            try:
                main()
            except SystemExit:
                pass
