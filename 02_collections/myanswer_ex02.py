def main(nms):
    for i, name in enumerate(nms,1):
        if is_me(name):
            print("{0}.My name is {1}.".format(i,name))
        else:
            print("{0}.{1} is my classmate.".format(i,name))
        
def is_me(name):
    myname = "Angy"
    if myname == name:
        return True
    else:
        return False

if __name__ == "__main__":
    names =  ("Bill", "Anne", "Angy", "Cony", "Daniel", "Occhan")
    main(names)