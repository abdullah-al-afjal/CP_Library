x = 40
x = "Bangladesh"
print(x)
print(type(x))

print("Welcome to Python!")
print("Welcome', 'to', 'Python!")
print("Welcome\nto\nPython!")


# Soul to Soul
print(
    """With memories rich, I take my leave,
No storm can tarnish what I retrieve.
 
Unforgettable moments, a treasure to perceive,
This journey, my heart will not deceive.
 
Friendship's tongue speaks in silent cues,
Not in mere words, but in shared views.
 
A sheltering tree, where hearts infuse,
Love's essence, devoid of wings' abuse.
 
To fathom and to be understood,
The hallmark of friendship, pure and good.
 
Not a lesson from textbooks, understood,
But in life's trials, where bonds withstood.
 
Friendship, a sacred, special kind,
Acceptance whole, flaws intertwined.
 
But those who falter, you will find,
Not true friends, but shadows behind.
 
Soul to soul, a sacred pact,
Betrayal foreign, healing exact.
 
Explaining it? A daunting act,
Yet God, the true friend, in fact.
 
In search of flawlessness, a lonesome fate,
Yet true friendship embraces every trait.
 
God and His universe, beyond debate,
Hold us close, in love's embrace.
 
In shattered images, a truth to glean,
Each shard, a friend's essence seen.
 
Never discard, for in-between,
Lies the bond, forever keen."""
)


num = 77
if num >= 90:
    print("A")
elif num >= 80:
    print("B")
elif num >= 70:
    print("C")
elif num >= 60:
    print("D")
else:
    print("F")

power = 0
result = 1
while result <= 50:
    power += 1
    result = 3**power

print(f"{power} = {result}")


number = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]

total_sum = sum(number)

num_students = len(number)

average_grade = total_sum / num_students


print(f"The class average: {average_grade:.2f}")


# function
def fun():
    print("I am Python")
    # main code
    print("Hello World")
    fun()
    print("Do you love me?")
