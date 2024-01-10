# class def for ChatBot
class ChatBot:
    def __init__(self):
        # initialize user attributes + menu options
        self.user_name = ""
        self.user_age = 0
        self.menu_options = {
            1: "School Hours",
            2: "School Location",
            3: "School Contact Info",
            4: "Exit"
        }

    def welcome_user(self):
        # greet user + get name + age
        print("Francisco: Hello! I am Francisco the ChatBox!\nI am here to help you navigate basic SchoolName school information!")
        self.user_name = input("Francisco: What's your name?\nEnter name here: ")
        self.user_age = int(input("Francisco: How old are you?\nEnter age here: "))

    def get_user_information(self):
        # display user information
        print("Francisco: Hi {}! You are {} years old!".format(self.user_name, self.user_age))

    def display_options(self):
        # show menu options
        print("\nFrancisco: How can I help you on this fine day?")
        for option, description in self.menu_options.items():
            print("{}. {}".format(option, description))

    def get_user_choice(self):
        # get user input for menu choice
        choice = input("You: ")
        return int(choice) if choice.isdigit() else 5

    def go_user_choice(self, choice):
        # outputs based on user's choice
        if choice == 1:
            print("Francisco:\nHours for School: 8am - 3pm")
        elif choice == 2:
            print("Francisco:\nLocation: 1923 StreetName St City, State, Zip Code, Country")
        elif choice == 3:
            print("Francisco:\nContact Info:\nNumber: 823-232-2312\nEmail: schoolEmail@school.edu")
        elif choice == 4:
            print("Francisco: Goodbye, {}! Thank you for speaking to me.".format(self.user_name))
            exit()
        else:
            print("Francisco: I'm sorry, I don't understand you.")

    def start_chat(self):
        # initiate the chatbot + start the conversation loop
        self.welcome_user()
        self.get_user_information()

        while True:
            self.display_options()
            user_choice = self.get_user_choice()
            self.go_user_choice(user_choice)

# start convo 
# create instance of ChatBox class
chatbot = ChatBot()
chatbot.start_chat()
