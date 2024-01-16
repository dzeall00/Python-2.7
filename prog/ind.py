#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")
    a = {"a", "e", "f", "i"}
    b = {"a", "b", "k", "n"}
    c = {"e", "f", "n" "o", "w", "x"}
    d = {"a", "d", "e", "o", "p", "t", "u"}
    x = (a.union(b)).intersection(d)
    print(f"x = {x}")
    # дополнения множеств
    an = u.difference(a)
    bn = u.difference(b)
    y = (an.intersection(bn)).difference(c.union(d))
    print(f"y = {y}")
