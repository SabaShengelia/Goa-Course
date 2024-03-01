required_height = 170
required_weight = 70

target_age = 18
target_training_days = 31

height = int(input("Please Enter Your Height: "))
weight = int(input("Please Enter Your Weight: "))

age = int(input("Please Enter Your Age: "))
days = int(input("How Many Days Do You Want To Train: "))

print(required_height == height and required_weight == weight )
print(age >= target_age or days < target_training_days)
print(height < required_height or required_weight > weight)
print(days == target_training_days and age == target_age)

required_pushups = 25
required_squits = 40

pushups = int(input("How Many Pushups Have You Done: "))
squits = int(input("How Many Squits Have You Done: "))

print(required_pushups == pushups and required_squits == squits)