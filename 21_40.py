# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

def get_divisors(n : int) -> list:
    divisors = []
    for i in range(1,n):
        if n % i == 0:
            divisors.append(i)
    return  sum(divisors)

def amicable_sum(n : int) -> int:
    ammicable_number = []
    for i in range(n):
        sum_of_divisors_a = get_divisors(i)
        sum_of_divisors_b = get_divisors(sum_of_divisors_a)
        print(i, sum_of_divisors_a, sum_of_divisors_b)
        if sum_of_divisors_b == i and i != sum_of_divisors_a:
            ammicable_number.append(i)
    return sum(ammicable_number)


# Names scores
def score(name, position):
    ascii_diffence = 64
    score = sum([ord(char) - ascii_diffence for char in name ]) * position
    return score




def name_score():
    
    with open ('names.txt') as file:
        file_data = file.read()
    file_data = file_data.replace('"','')
    file_data = file_data.replace(' ','')
    sorted_name_list = sorted(file_data.split(','))
    val = 0
    for i in range(0, len(sorted_name_list)):
        print(sorted_name_list[i], i + 1)

        val += score(sorted_name_list[i], i + 1)
    return val


# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
def sum_of_abundant_number():
    abundant_list = []
    limit = 28123
    for i in range(12, limit):
        a = []
        for j in range(i,0,-1):
            if i % j == 0:
                a.append(j)
        if sum(a) > i:
            abundant_list.append(i)
    abundant_set = set()
    for num1 in abundant_list:
        for num2 in abundant_list:
            if num1 + num2 > limit:
                break
            else:
                abundant_set.add(num1 + num2)
    return sum(list(abundant_set))

# Lexicographic permutations
from itertools import count, permutations
def lexicographic_permutations(n : str) -> str:
    perm_of_string = list(permutations(n))
    return ''.join(perm_of_string[999999])
    


def fibonacci_series() -> int:
    a, b = 0,1
    count = 1
    while True:
        count +=1
        a,b = b, b+a
        if len(str(b)) == 1000:
            return count

# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
    
def recurring_decimal(divisor):
	if divisor <10:
		divident = 10
	elif divisor >=10 and divisor <100:
		divident = 100
	else: 
		divident = 1000
	value_to_check = divident #10 or 100 or 1000
	string = ''
	for i in range(divisor):
		string += str(divident/divisor)
		divident = divident%divisor
		if divident < divisor:#adding decimal
			divident *= 10
			if divident < divisor:#adding zero after decimal
				divident *= 10
				string += '0'
				if divident < divisor:#adding another decimal after 0
					divident *= 10
					string += '0'
		if divident == value_to_check:
			return string        
            
def sieve(n):
	is_prime = [True]*n
	is_prime[0] = False
	is_prime[1] = False
	for i in range(2,int(n**0.5+1)):
		index = i*2
		while index < n:
			is_prime[index] = False
			index = index+i
	prime = []
	for i in range(n):
		if is_prime[i] == True:
			prime.append(i)
	return prime

def gcd(n1,n2):
	remainder = 1
	while remainder != 0:
		remainder = n1%n2
		n1 = n2
		n2 = remainder
	return n1


def lcm(n1,n2):
	return (n1*n2)/gcd(n1,n2)

primes = sieve(1000)
d = {n: 0 for n in range(1,1000)}
d[3] = 1

for i in primes[3:]:
	d[i] = len(recurring_decimal(i))


for i in range(6,1000):
	if not d[i]:
		if i % 2!= 0 and i%5!= 0: #number coprime to 10
			for j in primes:
				if i%j == 0:
					number1 = d[j]
					number2 = d[i/j]
					d[i] = lcm(number2,number1)
					break
		else: #number not coprime to 10
			number = i
			while number%2 == 0:
				number = number/2
			while number%5 == 0:
				number = number/5
			d[i] = d[number]


print (list(d.values()).index(max(list(d.values()) ) )+1 )



# Quadratic primes
def is_prime(n):
    prime_number_list =  [2,3,5,7]
    if n in prime_number_list:
        return True
    for i in range(8,n):
        if n % i == 0:
            return False
    return True

def quadratic_prime():
    val_dict = {}
    for i in range(-999,1000):
        for j in range(-1000,1001):
            count  = 0
            var = 1
            while True:
                z = (var * var) + (i * var) + j
                if is_prime(z):
                    count += 1
                    var +=1
                else:
                    print(f'{i}:{j} : {count}')
                    val_dict.update({
                        f'{i}.{j}' : count
                    })
                    break
    y = str(max(val_dict, key=val_dict.get)).split('.')
    return int(y[0])* int(y[1])



# Number spiral diagonals
# def spiral_daigonal(n : int) -> int:
#     a= []
#     for i in range(n):
        
        

# Distinct powers
from math import pow
def distinct_power():
    a = []
    for i in range(2,101):
        for j in range(2,101):
            a.append(int(pow(i,j)))
    a = set(a)
    return len(a)         
        
# Digit fifth powers
def fifth_digit_power():
    for i in range()

                     








if __name__ == '__main__':
    # print(amicable_sum(10000))
    # print(name_score())
    # print(sum_of_abundant_number())
    # print(lexicographic_permutations('0123456789'))
    # print(fibonacci_series())
    # print(quadratic_prime())
    print(distinct_power())