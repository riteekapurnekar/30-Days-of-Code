# Enter your code here. Read input from STDIN. Print output to STDOUT
actual_day, actual_month, actual_year = [int(x) for x in input().split(' ')]
expected_day, expected_month, expected_year = [int(x) for x in input().split(' ')]

if (actual_year, actual_month, actual_day) <= (expected_year, expected_month, expected_day):
    print(0)
elif (actual_year, actual_month) == (expected_year, expected_month):
    print(15 * (actual_day - expected_day))
elif actual_year == expected_year:
    print(500 * (actual_month - expected_month))
else:
    print(10000) 
