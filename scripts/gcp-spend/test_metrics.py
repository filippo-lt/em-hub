import unittest

import run


class CostRatioTest(unittest.TestCase):
    def test_computes_percentage(self):
        self.assertAlmostEqual(run.cost_ratio(250.0, 1000.0), 25.0)

    def test_none_revenue_gives_none(self):
        self.assertIsNone(run.cost_ratio(250.0, None))

    def test_zero_revenue_gives_none_not_division_error(self):
        self.assertIsNone(run.cost_ratio(250.0, 0.0))

    def test_negative_revenue_gives_none(self):
        self.assertIsNone(run.cost_ratio(250.0, -10.0))

    def test_spend_above_revenue_exceeds_one_hundred(self):
        self.assertAlmostEqual(run.cost_ratio(1500.0, 1000.0), 150.0)

    def test_zero_spend_is_zero_not_none(self):
        self.assertEqual(run.cost_ratio(0.0, 1000.0), 0.0)


class CostRatioDeltaTest(unittest.TestCase):
    def test_rising_ratio_is_positive(self):
        self.assertAlmostEqual(run.cost_ratio_delta_pp(30.0, 25.0), 5.0)

    def test_falling_ratio_is_negative(self):
        self.assertAlmostEqual(run.cost_ratio_delta_pp(20.0, 25.0), -5.0)

    def test_none_current_gives_none(self):
        self.assertIsNone(run.cost_ratio_delta_pp(None, 25.0))

    def test_none_previous_gives_none(self):
        self.assertIsNone(run.cost_ratio_delta_pp(30.0, None))


class AggregateRevenueTest(unittest.TestCase):
    MONTHS = ["202605", "202606"]

    def _apps(self):
        return [run.AppConfig("Chat Ultra", "chatai2-32311", "billing_export_data",
                              "01D6E9-4884D4-C31F38", "active")]

    def _rows(self):
        return [{"app": "Chat Ultra", "invoice_month": "202605",
                 "service": "Compute Engine", "net_cost": 100.0, "currency": "EUR"}]

    def test_revenue_is_attached_to_the_matching_app(self):
        histories, _, _ = run.aggregate(
            self._rows(), self._apps(), self.MONTHS,
            rev_data={"Chat Ultra": {"202605": 500.0, "202606": None}},
        )

        self.assertEqual(histories[0].revenue_by_month, [500.0, None])

    def test_app_without_revenue_data_gets_all_none(self):
        histories, _, _ = run.aggregate(self._rows(), self._apps(), self.MONTHS)

        self.assertEqual(histories[0].revenue_by_month, [None, None])


class PctAxisTest(unittest.TestCase):
    MONTHS = ["202605", "202606", "202607"]

    def test_pct_gridline_labels_carry_a_percent_sign(self):
        chart = run.build_line_chart(
            [10.0, 20.0, 40.0], self.MONTHS, "202607", fmt_y="pct",
        )

        self.assertTrue(all(g["label"].endswith("%") for g in chart["gridlines"]))

    def test_pct_labels_are_not_abbreviated_to_thousands(self):
        chart = run.build_line_chart(
            [1500.0, 1600.0, 1700.0], self.MONTHS, "202607", fmt_y="pct",
        )

        self.assertNotIn("K", chart["gridlines"][-1]["label"])

    def test_money_format_is_unchanged(self):
        chart = run.build_line_chart(
            [1500.0, 1600.0, 1700.0], self.MONTHS, "202607", fmt_y="money",
        )

        self.assertTrue(chart["gridlines"][-1]["label"].startswith("$"))


class OverlaySeriesTest(unittest.TestCase):
    def _history(self, revenue):
        return run.AppHistory(
            name="Chat Ultra", project_id="p", color="#000",
            by_month=[1.0] * len(revenue),
            services_by_month={}, total_in_window=1.0,
            mau_by_month=[10] * len(revenue),
            new_by_month=[1] * len(revenue),
            revenue_by_month=revenue,
        )

    def test_spend_only_when_nothing_else_is_available(self):
        series = run.build_overlay_series(
            self._history([None, None, None]), has_amplitude=False,
        )

        self.assertEqual([s["name"] for s in series], ["Spend"])

    def test_amplitude_adds_mau_and_new_users(self):
        series = run.build_overlay_series(
            self._history([None, None, None]), has_amplitude=True,
        )

        self.assertEqual([s["name"] for s in series], ["Spend", "MAU", "New users"])

    def test_revenue_included_at_three_months(self):
        series = run.build_overlay_series(
            self._history([1.0, 2.0, 3.0]), has_amplitude=False,
        )

        self.assertEqual([s["name"] for s in series], ["Spend", "Revenue"])

    def test_revenue_omitted_below_three_months(self):
        series = run.build_overlay_series(
            self._history([None, 2.0, 3.0]), has_amplitude=False,
        )

        self.assertEqual([s["name"] for s in series], ["Spend"])


class AppPageContextTest(unittest.TestCase):
    MONTHS = ["202605", "202606", "202607"]

    def _history(self, revenue):
        return run.AppHistory(
            name="Chat Ultra", project_id="p", color="#000",
            by_month=[100.0, 200.0, 300.0],
            services_by_month={}, total_in_window=600.0,
            mau_by_month=[None, None, None],
            new_by_month=[None, None, None],
            revenue_by_month=revenue,
        )

    def _ctx(self, revenue):
        return run.app_page_context(
            h=self._history(revenue), months=self.MONTHS, pending=[],
            currency="EUR", target_month="202607",
        )

    def test_has_revenue_false_when_all_none(self):
        ctx = self._ctx([None, None, None])

        self.assertFalse(ctx["has_revenue"])
        self.assertIsNone(ctx["ratio_chart"])

    def test_cost_ratio_at_target_month(self):
        ctx = self._ctx([1000.0, 1000.0, 1000.0])

        self.assertAlmostEqual(ctx["cost_ratio"], 30.0)

    def test_cost_ratio_delta_is_percentage_points(self):
        ctx = self._ctx([1000.0, 1000.0, 1000.0])

        self.assertAlmostEqual(ctx["cost_ratio_delta_pp"], 10.0)

    def test_table_rows_carry_revenue_and_ratio(self):
        rows = self._ctx([1000.0, 1000.0, 1000.0])["table_rows"]

        self.assertEqual(rows[0]["revenue"], 1000.0)
        self.assertAlmostEqual(rows[0]["cost_ratio"], 10.0)

    def test_unsettled_target_month_yields_no_ratio(self):
        ctx = self._ctx([1000.0, 1000.0, None])

        self.assertIsNone(ctx["cost_ratio"])
        self.assertIsNone(ctx["cost_ratio_delta_pp"])

    def test_overlay_hidden_when_only_spend_has_data(self):
        self.assertFalse(self._ctx([None, None, None])["show_overlay"])

    def test_overlay_shown_when_revenue_qualifies(self):
        self.assertTrue(self._ctx([1000.0, 1000.0, 1000.0])["show_overlay"])


class DashboardContextTest(unittest.TestCase):
    MONTHS = ["202605", "202606", "202607"]

    def _history(self, revenue):
        return run.AppHistory(
            name="Chat Ultra", project_id="p", color="#000",
            by_month=[100.0, 200.0, 300.0],
            services_by_month={}, total_in_window=600.0,
            mau_by_month=[None, None, None],
            new_by_month=[None, None, None],
            revenue_by_month=revenue,
        )

    def _apps(self, revenue):
        ctx = run.dashboard_context(
            histories=[self._history(revenue)],
            monthly_totals=[{"month": m, "total": 1.0} for m in self.MONTHS],
            months=self.MONTHS, pending=[], currency="EUR", target_month="202607",
        )
        return ctx["apps"]

    def test_card_carries_cost_ratio_and_delta(self):
        app = self._apps([1000.0, 1000.0, 1000.0])[0]

        self.assertAlmostEqual(app["cost_ratio"], 30.0)
        self.assertAlmostEqual(app["cost_ratio_delta_pp"], 10.0)

    def test_card_ratio_is_none_without_revenue(self):
        app = self._apps([None, None, None])[0]

        self.assertIsNone(app["cost_ratio"])
        self.assertIsNone(app["cost_ratio_delta_pp"])


if __name__ == "__main__":
    unittest.main()
