import os
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

import revenuecat


def ts(year: int, month: int) -> int:
    """Unix seconds at the UTC start of a month, as RevenueCat returns them."""
    return int(datetime(year, month, 1, tzinfo=timezone.utc).timestamp())


class LoadConfigTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.dotenv = self.tmp / ".env"
        self.dotenv.write_text("")
        self.addCleanup(self._tmp.cleanup)

    def _conf(self, body: str) -> Path:
        p = self.tmp / "revenuecat.conf"
        p.write_text(body)
        return p

    def test_missing_file_returns_empty_list(self):
        self.assertEqual(
            revenuecat.load_revenuecat_config(self.tmp / "nope.conf", self.dotenv),
            [],
        )

    def test_parses_row_and_resolves_key_from_env(self):
        os.environ["RC_TEST_KEY"] = "sk_test_123"
        self.addCleanup(os.environ.pop, "RC_TEST_KEY", None)
        conf = self._conf("Chat Ultra | proj_abc | RC_TEST_KEY\n")

        apps = revenuecat.load_revenuecat_config(conf, self.dotenv)

        self.assertEqual(len(apps), 1)
        self.assertEqual(apps[0].friendly_name, "Chat Ultra")
        self.assertEqual(apps[0].project_id, "proj_abc")
        self.assertEqual(apps[0].api_key, "sk_test_123")

    def test_skips_comments_and_blank_lines(self):
        os.environ["RC_TEST_KEY"] = "sk_test_123"
        self.addCleanup(os.environ.pop, "RC_TEST_KEY", None)
        conf = self._conf(
            "# a comment\n"
            "\n"
            "Chat Ultra | proj_abc | RC_TEST_KEY\n"
        )

        self.assertEqual(len(revenuecat.load_revenuecat_config(conf, self.dotenv)), 1)

    def test_skips_app_with_unset_env_var(self):
        os.environ.pop("RC_ABSENT_KEY", None)
        conf = self._conf("Chat Ultra | proj_abc | RC_ABSENT_KEY\n")

        self.assertEqual(revenuecat.load_revenuecat_config(conf, self.dotenv), [])

    def test_skips_app_with_empty_project_id(self):
        os.environ["RC_TEST_KEY"] = "sk_test_123"
        self.addCleanup(os.environ.pop, "RC_TEST_KEY", None)
        conf = self._conf("Truth Seeker |  | RC_TEST_KEY\n")

        self.assertEqual(revenuecat.load_revenuecat_config(conf, self.dotenv), [])

    def test_wrong_field_count_exits(self):
        conf = self._conf("Chat Ultra | proj_abc\n")

        with self.assertRaises(SystemExit):
            revenuecat.load_revenuecat_config(conf, self.dotenv)


class ParseChartResponseTest(unittest.TestCase):
    MONTHS = ["202605", "202606", "202607"]

    def test_maps_cohort_timestamps_to_yyyymm(self):
        payload = {"values": [
            {"cohort": ts(2026, 5), "measure": 0, "value": 100.0},
            {"cohort": ts(2026, 6), "measure": 0, "value": 250.5},
        ]}

        out = revenuecat.parse_chart_response(payload, self.MONTHS)

        self.assertEqual(out["202605"], 100.0)
        self.assertEqual(out["202606"], 250.5)

    def test_every_requested_month_is_a_key(self):
        out = revenuecat.parse_chart_response({"values": []}, self.MONTHS)

        self.assertEqual(sorted(out), sorted(self.MONTHS))
        self.assertTrue(all(v is None for v in out.values()))

    def test_ignores_secondary_measures(self):
        payload = {"values": [
            {"cohort": ts(2026, 5), "measure": 0, "value": 100.0},
            {"cohort": ts(2026, 5), "measure": 1, "value": 42.0},
            {"cohort": ts(2026, 5), "measure": 2, "value": 7.0},
        ]}

        self.assertEqual(revenuecat.parse_chart_response(payload, self.MONTHS)["202605"], 100.0)

    def test_incomplete_period_becomes_none(self):
        payload = {"values": [
            {"cohort": ts(2026, 7), "measure": 0, "value": 12.0, "incomplete": True},
        ]}

        self.assertIsNone(revenuecat.parse_chart_response(payload, self.MONTHS)["202607"])

    def test_complete_flag_false_is_kept(self):
        payload = {"values": [
            {"cohort": ts(2026, 7), "measure": 0, "value": 12.0, "incomplete": False},
        ]}

        self.assertEqual(revenuecat.parse_chart_response(payload, self.MONTHS)["202607"], 12.0)

    def test_months_outside_the_window_are_dropped(self):
        payload = {"values": [
            {"cohort": ts(2025, 1), "measure": 0, "value": 999.0},
        ]}

        out = revenuecat.parse_chart_response(payload, self.MONTHS)

        self.assertNotIn("202501", out)
        self.assertTrue(all(v is None for v in out.values()))

    def test_null_value_becomes_none(self):
        payload = {"values": [
            {"cohort": ts(2026, 5), "measure": 0, "value": None},
        ]}

        self.assertIsNone(revenuecat.parse_chart_response(payload, self.MONTHS)["202605"])

    def test_empty_payload_is_safe(self):
        out = revenuecat.parse_chart_response({}, self.MONTHS)

        self.assertTrue(all(v is None for v in out.values()))


class MonthBoundsTest(unittest.TestCase):
    def test_spans_first_to_last_day_of_the_window(self):
        self.assertEqual(
            revenuecat._month_bounds(["202605", "202606", "202607"]),
            ("2026-05-01", "2026-07-31"),
        )

    def test_december_end_rolls_into_next_year(self):
        self.assertEqual(
            revenuecat._month_bounds(["202611", "202612"]),
            ("2026-11-01", "2026-12-31"),
        )

    def test_february_leap_year(self):
        self.assertEqual(
            revenuecat._month_bounds(["202402"]),
            ("2024-02-01", "2024-02-29"),
        )


class FetchAllTest(unittest.TestCase):
    MONTHS = ["202605", "202606"]

    def _app(self, name="Chat Ultra"):
        return revenuecat.RevenueCatApp(name, "proj_abc", "sk_test")

    def test_returns_empty_for_no_apps(self):
        self.assertEqual(revenuecat.fetch_all([], self.MONTHS), {})

    def test_returns_empty_for_no_months(self):
        self.assertEqual(revenuecat.fetch_all([self._app()], []), {})

    def test_maps_each_app_to_its_parsed_series(self):
        payload = {"values": [
            {"cohort": ts(2026, 5), "measure": 0, "value": 100.0},
        ]}

        out = revenuecat.fetch_all(
            [self._app()], self.MONTHS,
            fetch=lambda app, months: payload, sleep=lambda s: None,
        )

        self.assertEqual(out["Chat Ultra"]["202605"], 100.0)
        self.assertIsNone(out["Chat Ultra"]["202606"])

    def test_failed_fetch_yields_all_none_not_an_exception(self):
        out = revenuecat.fetch_all(
            [self._app()], self.MONTHS,
            fetch=lambda app, months: None, sleep=lambda s: None,
        )

        self.assertIn("Chat Ultra", out)
        self.assertTrue(all(v is None for v in out["Chat Ultra"].values()))

    def test_one_app_failing_does_not_affect_another(self):
        good = {"values": [{"cohort": ts(2026, 5), "measure": 0, "value": 7.0}]}

        def fetch(app, months):
            return None if app.friendly_name == "Bad App" else good

        out = revenuecat.fetch_all(
            [self._app("Bad App"), self._app("Good App")], self.MONTHS,
            fetch=fetch, sleep=lambda s: None,
        )

        self.assertIsNone(out["Bad App"]["202605"])
        self.assertEqual(out["Good App"]["202605"], 7.0)

    def test_throttles_between_apps_but_not_before_the_first(self):
        slept = []

        revenuecat.fetch_all(
            [self._app("A"), self._app("B"), self._app("C")], self.MONTHS,
            fetch=lambda app, months: {"values": []}, sleep=slept.append,
        )

        self.assertEqual(slept, [revenuecat.THROTTLE_SECONDS] * 2)


if __name__ == "__main__":
    unittest.main()
