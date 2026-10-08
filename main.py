from pyscript import document

# List containing ICT members
CLUB_MEMBERS = [
    "Miku Martineau",
    "Lebron James",
    "Lamelo Ball",
    "Anthony Edwards",
]


def check_member(e)
 # get values from input fields
FIRSTNAME = document.getElementById("FIRSTNAME").value #get the first name
SURNAME = document.getElementById("SURNAME").value # get the last name

#combine names with a space using concatenation
FULLNAME = FIRSTNAME + " " + SURNAME #e.g Evaluates to "Miku Martineau" (str)

#checks if FULLNAME is IN CLUB_MEMBERS (true or false)
is_member = FULLNAME in CLUB_MEMBERS


result_message = (
  "Sorry " + SURNAME + ", your name is not on the list.", # index 0, false
  "Congratulations " + SURNAME + "! You are now part of the ICT club." # index 1, true
)

# use true (1) and false (0) as tuple to select the message
result = result_message[is_member]

# display result in HTML
document.getElementById("result").innerHTML = result