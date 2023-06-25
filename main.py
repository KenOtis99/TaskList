#Main
import os
import modify
import json
import Art
#Organize and choose the options 
def main():
	goodbye = False
	while (goodbye!= True): 
		os.system('cls')
		print(Art.welcome)
		print("Welcome to your ToDo list!\n")
		print("Here are your tasks: ")
		modify.displayTaskName()
		#Print tasks

		print("""\nWhat would you like to do?\n
			1. Add to the list
			2. View task
			3. Edit task
			4. Mark task as completed
			5. Exit
			""")
		try: 
			choice = int(input("Your Choice: "))
			if choice == 1:
				os.system('cls')
				print(Art.todo)
				modify.addTask()
			elif choice == 2:
				os.system('cls')
				print(Art.todo)
				modify.displayTaskName()
				task= int(input(f"Which task would you like to view? "))
				os.system('cls')
				print(Art.todo)
				modify.loadTask(task)
			elif choice == 3:
				os.system('cls')
				print(Art.todo)
				modify.displayTaskName()
				task = int(input("Which task would you like to Edit? "))
				modify.loadTask(task)
				edit = input("Would you like to edit the name or description? ")
				edit = edit.upper()
				if edit == "NAME":
					modify.editTaskName(task)
				elif edit == "DESCRIPTION":
					modify.editTaskDesc(task)
			elif choice == 4:
				os.system('cls')
				print(Art.todo)
				modify.displayTaskName()
				task= int(input(f"Which task would you like to mark as completed? "))
				modify.removeTask(task)
				print("Task has been removed")
			elif choice == 5:
				os.system('cls')
				print(Art.goodbye)
				goodbye = True
		except ValueError:
			print("Invalid Input. Please try again")
			cont = input("Please press any key to continue...")

	
if __name__ == "__main__":
    main()