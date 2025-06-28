📘 LeetCode Favorite Solutions
Welcome to my curated collection of favorite LeetCode solutions — written in Python and organized by topic and difficulty. This repository showcases my approach to solving algorithmic problems with a focus on readability, efficiency, and clean code design.

🧠 Goals
Improve data structures & algorithmic thinking

Practice clean and optimized Python coding

Build a reference bank for common patterns and techniques

Help others learn through well-documented solutions

🛠️ Language & Tools
Language: Python 3

Platform: LeetCode

IDE: VS Code / LeetCode Web Editor

Version Control: Git & GitHub

📂 Structure
Copy
Edit
leetcode-fav-solutions/
├── arrays/
│   └── two_sum.py
├── trees/
│   └── max_depth.py
├── recursion/
│   └── is_symmetric.py
├── dynamic_programming/
│   └── climb_stairs.py
└── README.md
📌 Topics Covered
Arrays & Strings

Binary Trees

Recursion & DFS/BFS

Linked Lists

Hash Maps & Sets

Dynamic Programming

Greedy Algorithms

Binary Search

✅ How to Use
Each file contains:

Problem name & link

Explanation (in comments)

Clean Python solution

Clone or browse the repo to explore different patterns.

🧩 Sample Entry (inside files)
python

# Problem: 104. Maximum Depth of Binary Tree
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Approach: Recursive DFS
# Time: O(n), Space: O(h)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
🔗 Let's Connect
Feel free to star ⭐ the repo or contribute if you'd like to collaborate on learning and growing together!

GitHub: @Abdul00YO

LinkedIn: Abdullah Arshad
