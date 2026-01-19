##  **argparse basics**

### Import it

```python
import argparse
```

---

### Create the parser

```python
parser = argparse.ArgumentParser(description="Describe what your script does")
```

---

### Add arguments

```python
parser.add_argument(
    "mbti",              # positional argument
    type=str,
    help="MBTI type, e.g., INFP"
)

parser.add_argument(
    "--verbose",         # optional flag
    action="store_true",
    help="Print detailed output"
)
```

---

### Parse arguments

```python
args = parser.parse_args()
```

---

### Use them

```python
print(args.mbti)
if args.verbose:
    print("Verbose mode is on!")
```

---

## **Key points to remember**

✅ Positional arguments → just `add_argument("name")`
✅ Optional flags → start with `--` and usually have `action="store_true"` if they’re boolean
✅ You can set `type`, `default`, `choices`, etc.
✅ `parser.parse_args()` returns a namespace object; access with `args.name`
