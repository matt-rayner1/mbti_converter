### **Rule 1: letter1 → introvert or extravert**

```
if first_letter == 'I':
    dominant function is introverted
    auxiliary function is extraverted
else if first_letter == 'E':
    dominant function is extraverted
    auxiliary function is introverted
```

---

### **Rule 2: letter4 (J or P) → which function becomes extraverted**

For extraverts:

```
if first_letter == 'E':
    if fourth_letter == 'J':
        dominant = extraverted judging function (Te or Fe)
        auxiliary = introverted perceiving function (Ni or Si)
    else if fourth_letter == 'P':
        dominant = extraverted perceiving function (Ne or Se)
        auxiliary = introverted judging function (Ti or Fi)
```

For introverts:

```
if first_letter == 'I':
    if fourth_letter == 'J':
        auxiliary = extraverted perceiving function (Ne or Se)
        dominant = introverted judging function (Ti or Fi)
    else if fourth_letter == 'P':
        auxiliary = extraverted judging function (Te or Fe)
        dominant = introverted perceiving function (Ni or Si)
```

---

### **Rule 3: letter2 (N or S) → choose perceiving function**

```
if second_letter == 'N':
    perceiving functions are Ni and Ne
else if second_letter == 'S':
    perceiving functions are Si and Se
```

---

### **Rule 4: letter3 (T or F) → choose judging function**

```
if third_letter == 'T':
    judging functions are Ti and Te
else if third_letter == 'F':
    judging functions are Fi and Fe
```

---

### **Rule 5: tertiary and inferior**

```
tertiary function:
    opposite attitude (introvert/extravert) of auxiliary
    same function family as dominant (judging/perceiving)

inferior function:
    opposite attitude of dominant
    opposite function of dominant (Fi <-> Te, Ti <-> Fe, Ni <-> Se, Si <-> Ne)
```

---
