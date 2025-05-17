from faker import Faker;
f = Faker();
for i in range(20):
    test = f.random_int(1,10);
    print(test);
