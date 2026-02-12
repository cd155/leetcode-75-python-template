"""
Tests for LeetCode 714: Best Time to Buy and Sell Stock with Transaction Fee
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from dp_multidimensional.best_time_to_buy_and_sell_stock_with_transaction_fee import Solution


class TestBestTimeToBuyAndSellStockWithTransactionFee:
    """Test cases for LeetCode 714: Best Time to Buy and Sell Stock with Transaction Fee"""

    def setup_method(self):
        self.solution = Solution()

    def test_example_1(self):
        assert self.solution.maxProfit([1,3,2,8,4,9], 2) == 8

    def test_example_2(self):
        assert self.solution.maxProfit([1,3,7,5,10,3], 3) == 6

