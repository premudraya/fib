# coding=utf-8
import subprocess
import matplotlib.pyplot as plt

numbers = range(1, 51)
times = []

for number in numbers:
    out = subprocess.check_output(["./fibonacci", "recursive", "%d" % (number,)])
    times.append(float(out))

plt.ylabel('время (с)')
plt.xlabel('число фибоначчи')
plt.plot(numbers, times, 'r.-')
plt.savefig('recursive-50.png')
plt.close()

times2 = []

for number in numbers:
    out = subprocess.check_output(["./fibonacci", "iterative", "%d" % (number,)])
    times2.append(float(out))

plt.ylabel('время (с)')
plt.xlabel('число фибоначчи')
plt.plot(numbers, times2, 'r.-')
plt.savefig('iterative-50.png')
plt.close()

times3 = []
hundred = range(1, 101)

for number in hundred:
    out = subprocess.check_output(["./fibonacci", "iterative", "%d" % (number,)])
    times3.append(float(out))

plt.ylabel('время (с)')
plt.xlabel('число фибоначчи')
plt.plot(hundred, times3, 'r.-')
plt.savefig('iterative-100.png')
plt.close()

plt.hold(True)
plt.figure(figsize=(10,10))
plt.ylabel('время (с)')
plt.xlabel('число фибоначчи')
plt.plot(numbers, times, 'r.-')
plt.plot(numbers, times2, 'g.-')
plt.plot(hundred, times3, 'b.-')

plt.savefig('all.png')
