X0 = 1

X11 = 0
X12 = 0

X21 = 0
X22 = 1

X31 = 1
X32 = 0

X41 = 1
X42 = 1

TARGETX1 = 0
TARGETX2 = 0
TARGETX3 = 0
TARGETX4 = 1

W0 = 0.5
W1 = 0.5
W2 = 0.5

LEARNINGRATE = 0.1


#-------------------------------------------------------#

print('epoch1')
print('1')
sum1 = (X0 * W0) + (X11 * W1) + (X12 * W2)  #sum
print('sum',sum1)
if sum1 >= 0.0:             #sigmoid   1,0
    sigmoid = 1
else:
    sigmoid = 0
print('sigmoid',sigmoid)
tarout = TARGETX1 - sigmoid             # target - output
print('tarout',tarout)
w0n = W0+LEARNINGRATE*tarout*X0             # new weight
w1n = W1+LEARNINGRATE*tarout*X11
w2n = W2+LEARNINGRATE*tarout*X12

print('w0n',w0n)
print('w1n',w1n)
print('w2n',w2n)

se1 = tarout**2                     #se

print('se1',se1)

print('2')
sum1 = (X0 * w0n) + (X21 * w1n) + (X22 * w2n)
print('sum',sum1)
if sum1 >= 0.0:
    sigmoid = 1
else:
    sigmoid = 0
print('sigmoid',sigmoid)
tarout = TARGETX2 - sigmoid
print('tarout',tarout)
w0n = w0n+LEARNINGRATE*tarout*X0
w1n = w1n+LEARNINGRATE*tarout*X21
w2n = w2n+LEARNINGRATE*tarout*X22

print('w0n',w0n)
print('w1n',w1n)
print('w2n',w2n)

se2 = tarout**2

print('se2',se2)

print('3')
sum1 = (X0 * w0n) + (X31 * w1n) + (X32 * w2n)
print('sum',sum1)
if sum1 >= 0.0:
    sigmoid = 1
else:
    sigmoid = 0
print('sigmoid',sigmoid)
tarout = TARGETX3 - sigmoid
print('tarout',tarout)
w0n = w0n+LEARNINGRATE*tarout*X0
w1n = w1n+LEARNINGRATE*tarout*X31
w2n = w2n+LEARNINGRATE*tarout*X32

print('w0n',w0n)
print('w1n',w1n)
print('w2n',w2n)

se3 = tarout**2

print('se3',se3)

print('4')
sum1 = (X0 * w0n) + (X41 * w1n) + (X42 * w2n)
print('sum',sum1)
if sum1 >= 0.0:
    sigmoid = 1
else:
    sigmoid = 0
print('sigmoid',sigmoid)
tarout = TARGETX4 - sigmoid
print('tarout',tarout)
w0n = w0n+LEARNINGRATE*tarout*X0
w1n = w1n+LEARNINGRATE*tarout*X41
w2n = w2n+LEARNINGRATE*tarout*X42

print('w0n',w0n)
print('w1n',w1n)
print('w2n',w2n)

se4 = tarout**2

print('se4',se4)

mse = (se1+se2+se3+se4)/4

print('error rate',mse)
print('------------------------------------------------------------------------------------------')
#-----------------------------------#

i = 1
while mse >= 0.2:
    i =  i+1
    print('epoch',i)
    print('####1')
    sum1 = (X0 * w0n) + (X11 * w1n) + (X12 * w1n)
    print('sum',sum1)
    if sum1 >= 0.0:
        sigmoid = 1
    else:
        sigmoid = 0
    print('sigmoid',sigmoid)
    tarout = TARGETX1 - sigmoid
    print('tarout',tarout)
    w0n = w0n+LEARNINGRATE*tarout*X0
    w1n = w1n+LEARNINGRATE*tarout*X11
    w2n = w2n+LEARNINGRATE*tarout*X12

    print('w0n',w0n)
    print('w1n',w1n)
    print('w2n',w2n)

    se1 = tarout**2

    print('se1',se1)
    print('####2')
    sum1 = (X0 * w0n) + (X21 * w1n) + (X22 * w2n)
    print('sum',sum1)
    if sum1 >= 0.0:
        sigmoid = 1
    else:
        sigmoid = 0
    print('sigmoid',sigmoid)
    tarout = TARGETX2 - sigmoid
    print('tarout',tarout)
    w0n = w0n+LEARNINGRATE*tarout*X0
    w1n = w1n+LEARNINGRATE*tarout*X21
    w2n = w2n+LEARNINGRATE*tarout*X22

    print('w0n',w0n)
    print('w1n',w1n)
    print('w2n',w2n)

    se2 = tarout**2

    print('se2',se2)

    print('####3')
    sum1 = (X0 * w0n) + (X31 * w1n) + (X32 * w2n)
    print('sum',sum1)
    if sum1 >= 0.0:
        sigmoid = 1
    else:
        sigmoid = 0
    print('sigmoid',sigmoid)
    tarout = TARGETX3 - sigmoid
    print('tarout',tarout)
    w0n = w0n+LEARNINGRATE*tarout*X0
    w1n = w1n+LEARNINGRATE*tarout*X31
    w2n = w2n+LEARNINGRATE*tarout*X32

    print('w0n',w0n)
    print('w1n',w1n)
    print('w2n',w2n)

    se3 = tarout**2

    print('se3',se3)
    print('####4')
    sum1 = (X0 * w0n) + (X41 * w1n) + (X42 * w2n)
    print('sum',sum1)
    if sum1 >= 0.0:
        sigmoid = 1
    else:
        sigmoid = 0
    print('sigmoid',sigmoid)
    tarout = TARGETX4 - sigmoid
    print('tarout',tarout)
    w0n = w0n+LEARNINGRATE*tarout*X0
    w1n = w1n+LEARNINGRATE*tarout*X41
    w2n = w2n+LEARNINGRATE*tarout*X42

    print('w0n',w0n)
    print('w1n',w1n)
    print('w2n',w2n)

    se4 = tarout**2

    print('se4',se4)

    mse = (se1+se2+se3+se4)/4

    print('error rate',mse)
    print('------------------------------------------------------------------------------------------')
print('epoch',i)
print('w0n',w0n)
print('w1n',w1n)
print('w2n',w2n)
print('error rate',mse)


