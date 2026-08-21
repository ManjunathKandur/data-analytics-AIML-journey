# 📘 Day 08 — Python Sets


## 🎯 Objective

Learn how to use Python Sets to store unique values, remove duplicates, and compare datasets using set operations.

---

## 📚 Topics Covered

- Creating Sets
- Unique Values
- Adding & Removing Elements
- Union
- Intersection
- Difference
- Symmetric Difference
- Subset & Superset

---

## 🧠 Key Concepts

| Concept | Description |
|---------|-------------|
| Set | An unordered collection of unique values |
| Union  | Combines all unique elements from two sets |
| Intersection (`&`) | Returns common elements |
| Difference (`-`) | Returns elements present in one set but not the other |
| Symmetric Difference (`^`) | Returns elements that exist in exactly one set |
| Subset(.issubset/<=) | Checks whether one set is contained within another |
| Superset(.issuperset/>=) | Checks whether one set contains another set |

---

## 💻 Practice Programs

Completed the following exercises:

- Remove duplicates from a list
- Count unique values
- Find common students
- Compare two datasets
- Check subset relationship
- Check superset relationship

---

## 📝 Sample Code

```python
class_a = {"John", "Mike", "Sara", "Tom"}
class_b = {"Sara", "Tom", "David", "Emma"}

print("Union:", class_a | class_b)
print("Intersection:", class_a & class_b)
print("Only Class A:", class_a - class_b)
print("Only Class B:", class_b - class_a)
print("Symmetric Difference:", class_a ^ class_b)
```
---

## 🎓 Learning Outcome

By the end of Day 08, I can:

- Create and modify sets
- Remove duplicate values efficiently
- Perform all major set operations
- Compare collections using subset and superset
- Apply sets to real-world dataset comparison problems

---

## ✅ Status

**Day 08 Completed ✔️**
