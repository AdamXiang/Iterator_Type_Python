# Custom Sequence Type in Python

## 🎯 Project Goal
This project aims to implement a **custom sequence type in Python** that behaves like built-in sequence types (such as `list`, `tuple`, or `str`) but with additional specialized behavior.  

Through this project, I want to demonstrate:
- How to **design and implement Python classes** that follow the **sequence protocol** (`__getitem__`, `__len__`, `__iter__`, slicing support, etc.).
- How to make custom types **integrate seamlessly** with Python’s built-in operators and idioms (e.g., indexing, iteration, `in` operator).
- How to apply **best practices in object-oriented design** and write **clean, maintainable, and Pythonic code**.

---

## ✨ Key Features
- Implements the **core sequence protocol** in Python:
  - `__getitem__` with support for both indexing and slicing
  - `__len__`
- Supports **common Python idioms**:
  - Membership check (`x in my_sequence`)
  - Iteration in `for` loops
  - Index-based access
- Extendable design for **custom behaviors**, e.g.:
  - Lazy evaluation
  - Type validation
  - Auto-transformation of elements

---

## 🧩 Why This Project?
Python’s built-in collections are powerful, but sometimes developers need a **custom sequence type** for:
- Enforcing constraints (e.g., only storing validated objects).
- Implementing domain-specific collections.
- Creating lightweight wrappers around existing data with extra semantics.

This project shows how to **bridge the gap between Python’s abstract base classes** and **practical use cases**, while following a **Pythonic design philosophy**.

---

## 🚀 Skills Demonstrated
- **Deep understanding of Python’s data model** (special methods, dunder methods).
- **Object-oriented programming** with clean abstractions.
- **Readable and maintainable code style**, following PEP 8 guidelines.
- Experience in **writing tests** (with `pytest`) to validate correctness.

---

## 📖 Usage Example

Here’s a minimal example of how this custom sequence type works:

```python
from polygon import Polygon
from polygons import Polygons

def main():
    # Create a Polygons sequence with max vertices = 10 and circumradius = 5
    polygons = Polygons(10, 5)
    print(polygons)  
    # Output: Polygons(m=10, R=5)

    # Length of the sequence (polygons from 3-gon up to 10-gon)
    print(f"Number of polygons: {len(polygons)}")  
    # Output: 8 (3-gon to 10-gon inclusive)

    # Indexing and slicing
    print("First polygon:", polygons[0])   # Polygon with 3 vertices (triangle)
    print("Last polygon:", polygons[-1])   # Polygon with 10 vertices

    print("Slice [2:5]:", polygons[2:5])   # Returns polygons with 5–7 vertices

    # Access properties of a specific polygon
    hexagon = polygons[3]  # Polygon with 6 vertices
    print(f"Hexagon - sides: {hexagon.count_edges}, area: {hexagon.area:.2f}, perimeter: {hexagon.perimeter:.2f}")

    # Find the most efficient polygon (max area-to-perimeter ratio)
    best = polygons.max_efficiency_polygon
    print(f"Most efficient polygon: {best.count_vertices}-gon with efficiency {best.area/best.perimeter:.4f}")

if __name__ == "__main__":
    main()
```

---

## 📂 Repository Structure

```bash
custom-sequence-type/
├── custom_sequence/
│   ├── __init__.py
│   ├── polygon.py          
|   ├── polygons.py      # Core implementation of the custom sequence
├── tests/
│   └── test_sequence.py # Unit tests with pytest
├── README.md            # Project documentation
├── requirements.txt     # Project dependencies
└── LICENSE
```

---

## 🔮 Future Work
- Add support for mutability (e.g., **`__setitem__`**, `append`, `extend`).
- Benchmark performance compared with built-in lists.
- Explore **integration with collections.abc** for automatic interface validation.
- Provide examples of **real-world applications** (e.g., immutable configs, validated datasets).


## 👉 Install dependencies with:
```bash
pip install -r requirements.txt
```

## 👉 To run the tests, simply execute:
```bash
pytest tests/
```