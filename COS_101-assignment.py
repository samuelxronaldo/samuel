def a():
    velocity=float(input("input your velocity:"))
    time=float(input("input your time:"))
    #displacement= velocity*time
    output= str(velocity*time)
    print(output + "M")

def b():
    displacement=int(input("what is the displacement:"))
    time=int(input("what is time:"))
    #velocity=displacement/time
    output=str(displacement/time)
    print(output+" m/s")

def c ():
    mass=float(input("input your mass:"))
    gravity=float(input("input your gravity:"))
    #weight=mass*gravity
    output=str(mass*gravity)
    print(output+"N")

def d ():
    force=int(input("what is the force:"))
    area=int(input("what is the area:"))
    #pressure= force*area
    output=str(force/area)
    print(output+"pa")

def e():
    workdone=float(input("input your workdone:"))
    time=float(input("input your time:"))
    #power= workdone/time
    output=str(workdone/time)
    print(output+ "w")



def main():
        user_choice = input("choose from a - e: ")
        if user_choice == "a":
            a()
        elif user_choice == "b":
            b()
        elif user_choice == "c":
            c()
        elif user_choice == "d":
            d()
        elif user_choice == "e":
            e()

if __name__ == '__main__':
        main()