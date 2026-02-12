# LeetCode 75 Practice in Python

A structured project for practicing and mastering the LeetCode 75 essential coding interview questions in Python.

## 📋 Project Overview

This repository contains solutions to the LeetCode 75 curated list of essential interview questions, organized by problem type. Each solution includes:
- Clean, well-documented Python code
- Comprehensive test cases
- Time and space complexity analysis (where applicable)

## 🗂️ Project Structure

```
pytho-leetcode-75/
├── src/                          # Solution modules
│   ├── array_string/             # Array and String problems
│   ├── two_pointers/             # Two Pointers technique
│   ├── sliding_window/           # Sliding Window problems
│   ├── prefix_sum/               # Prefix Sum problems
│   ├── hash_map/                 # Hash Map/Set problems
│   ├── stack/                    # Stack problems
│   ├── queue/                    # Queue problems
│   ├── linked_list/              # Linked List problems
│   ├── binary_tree/              # Binary Tree - DFS problems
│   ├── binary_tree_bfs/          # Binary Tree - BFS problems
│   ├── binary_search_tree/       # Binary Search Tree problems
│   ├── graph_dfs/                # Graph - DFS problems
│   ├── graph_bfs/                # Graph - BFS problems
│   ├── heap/                     # Heap/Priority Queue problems
│   ├── binary_search/            # Binary Search problems
│   ├── backtracking/             # Backtracking problems
│   ├── dp_1d/                    # Dynamic Programming - 1D
│   ├── dp_multidimensional/      # Dynamic Programming - Multidimensional
│   ├── bit_manipulation/         # Bit Manipulation problems
│   ├── trie/                     # Trie problems
│   ├── intervals/                # Intervals problems
│   └── monotonic_stack/          # Monotonic Stack problems
├── tests/                        # Test files
├── requirements.txt              # Python dependencies
├── pyproject.toml                # Project configuration
├── pytest.ini                    # Pytest configuration
└── README.md                     # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/cd155/pytho-leetcode-75.git
cd pytho-leetcode-75
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Or install with development dependencies:
```bash
pip install -e ".[dev]"
```

## 🧪 Running Tests

### Run all tests:
```bash
pytest
```

### Run tests for a specific problem:
```bash
pytest tests/test_merge_strings_alternately.py
```

### Run tests with verbose output:
```bash
pytest -v
```

### Run tests with coverage:
```bash
pytest --cov=src tests/
```

## 📝 Adding New Solutions

### 1. Create a solution file:
Create a new Python file in the appropriate category directory under `src/`. For example:

```python
# src/array_string/your_problem.py
"""
LeetCode XXXX: Problem Title

Problem description here...
"""

class Solution:
    def yourMethod(self, input_param):
        """
        Solution description.
        
        Args:
            input_param: Description
            
        Returns:
            Description of return value
        """
        # Your implementation here
        pass
```

### 2. Create corresponding test file:
Create a test file in the `tests/` directory:

```python
# tests/test_your_problem.py
"""
Tests for LeetCode XXXX: Problem Title
"""

import pytest
import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from category.your_problem import Solution


class TestYourProblem:
    """Test cases for your problem"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.solution = Solution()
    
    def test_case_1(self):
        """Test description"""
        assert self.solution.yourMethod(input) == expected_output
    
    def test_case_2(self):
        """Test description"""
        assert self.solution.yourMethod(input) == expected_output
```

### 3. Run your tests:
```bash
pytest tests/test_your_problem.py -v
```

## 📊 Problem Categories

The LeetCode 75 problems are organized into the following categories:

1. **Array / String** - Basic array and string manipulation
2. **Two Pointers** - Problems using two pointer technique
3. **Sliding Window** - Window-based array/string problems
4. **Prefix Sum** - Cumulative sum techniques
5. **Hash Map / Set** - Hash table based problems
6. **Stack** - Stack data structure problems
7. **Queue** - Queue data structure problems
8. **Linked List** - Linked list manipulation
9. **Binary Tree - DFS** - Tree traversal with DFS
10. **Binary Tree - BFS** - Tree traversal with BFS
11. **Binary Search Tree** - BST specific problems
12. **Graphs - DFS** - Graph traversal with DFS
13. **Graphs - BFS** - Graph traversal with BFS
14. **Heap / Priority Queue** - Heap-based problems
15. **Binary Search** - Binary search algorithm
16. **Backtracking** - Backtracking technique
17. **DP - 1D** - One-dimensional dynamic programming
18. **DP - Multidimensional** - Multi-dimensional DP
19. **Bit Manipulation** - Bitwise operations
20. **Trie** - Trie data structure
21. **Intervals** - Interval-based problems
22. **Monotonic Stack** - Monotonic stack technique

## 🎯 Example Solution

See `src/array_string/merge_strings_alternately.py` for an example solution with:
- Detailed problem description
- Clean implementation
- Type hints
- Comprehensive docstrings

And `tests/test_merge_strings_alternately.py` for example test cases.

## 🤝 Contributing

Feel free to add more solutions or improve existing ones! Make sure to:
1. Follow the existing code structure
2. Add comprehensive test cases
3. Include docstrings and comments
4. Run tests before committing

## 📚 Resources

- [LeetCode 75 Study Plan](https://leetcode.com/studyplan/leetcode-75/)
- [Python Documentation](https://docs.python.org/3/)
- [Pytest Documentation](https://docs.pytest.org/)

## 📄 License

This project is for educational purposes. All LeetCode problems are property of LeetCode.

---

Happy Coding! 🚀