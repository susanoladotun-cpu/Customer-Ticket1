# Initialize an empty dictionary to store complaints
# Structure: {ticket_id: {"name": str, "issue": str, "status": str}}
complaints = {}
next_ticket_id = 1

def add_ticket():
    global next_ticket_id
    print("\n--- Add New Complaint ---")
    name = input("Enter Customer Name: ")
    issue = input("Enter Complaint: ")
    
    # Store the data in the dictionary
    complaints[next_ticket_id] = {
        "name": name,
        "issue": issue,
        "status": "Pending"
    }
    
    print(f"Success! Complaint recorded with Ticket ID: {next_ticket_id}")
    next_ticket_id += 1

def view_tickets(filter_pending=False):
    title = "Pending Complaints" if filter_pending else "All Complaints"
    print(f"\n--- {title} ---")
    
    found = False
    for tid, data in complaints.items():
        # If filter_pending is True, only show "Pending". Otherwise, show all.
        if filter_pending and data["status"] != "Pending":
            continue
            
        print(f"Ticket {tid} | Customer: {data['name']} | Status: {data['status']}")
        print(f" Issue: {data['issue']}")
        found = True
        
    if not found:
        print("No complaints found.")

def resolve_ticket():
    print("\n--- Resolve a Complaint ---")
    try:
        tid = int(input("Enter Ticket ID to resolve: "))
        if tid in complaints:
            if complaints[tid]["status"] == "Resolved":
                print(f"Ticket {tid} is already marked as Resolved.")
            else:
                complaints[tid]["status"] = "Resolved"
                print(f"Ticket {tid} has been updated to Resolved.")
        else:
            print("Error: Ticket ID not found.")
    except ValueError:
        print("Invalid input. Please enter a numeric Ticket ID.")

def main_menu():
    while True:
        print("\n==============================")
        print("Customer Support Ticket System")
        print("==============================")
        print("1. Add Complaint")
        print("2. View All Complaints")
        print("3. View Pending Complaints")
        print("4. Resolve Complaint")
        print("5. Exit")
        
        choice = input("\nSelect an option (1-5): ")
        
        if choice == '1':
            add_ticket()
        elif choice == '2':
            view_tickets(filter_pending=False)
        elif choice == '3':
            view_tickets(filter_pending=True)
        elif choice == '4':
            resolve_ticket()
        elif choice == '5':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()