base = [
    1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0,
    3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1
]

multiplier = [0.01, 0.1, 1, 10, 100, 1000, 10000]
e24 = [round(b * mul, 3) for mul in multiplier for b in base]
e24.append(100000)
