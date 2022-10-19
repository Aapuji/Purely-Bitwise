# Purely Bitwise

The goal of this is to try to write operations purely through bitwise operations: `&`, `|`, `~`, `^`, `<<`, `>>`; and maybe `<<<` and `>>>`.
However, some additional things are allowed:
- the `cmp` function, which returns `true` if 0 and `false` otherwise
- if statements, but only using `cmp`. (eg. `if cmp(n): return 0`)
- recursion
