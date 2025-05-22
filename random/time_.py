import time
print(time.time())
def lots_of_numbers(max):
    t1 = time.time()
    for x in range(0, max):
        print(x)
    t2 = time.time()
    print('it took %s seconds'% (t2-t1))
lots_of_numbers(800000)

print(time.asctime())

t = (2020, 2, 23, 10, 30, 48, 6, 365, 59)
print(time.asctime(t))

print(time.localtime())
# time.struct_time(tm_year=2020, tm_mon=2,tm_mday=23)
t = time.localtime()
year = t[0]
month = t[1]
print(year)
print(month)

for x in range(1, 61):
    print(x)
    time.sleep(1)
