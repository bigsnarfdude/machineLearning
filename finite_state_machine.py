# finite state machine to demonstrate under the hood for regular expressions

edges = { (1, "v") : 2, \
          (2, "i") : 3, \
          (3, "n") : 4, \
          (4, "c") : 5, \
          (5, "e") : 6  \
        }

accepting = [6]


def finite_state_machine(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        if (current, letter) in edges:
            return finite_state_machine(string[1:], edges[(current, letter)], edges, accepting)
        else:
            return False

print "vince" , finite_state_machine('vince', 1, edges, accepting)
print "vincent" , finite_state_machine('vincent', 1, edges, accepting)
