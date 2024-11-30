command=""
started=False
while True:
    command=input("> ").lower()
    if command=="start":
        if started:
            print("Car has already started")
        else:
            started=True
            print("Car started...")
    elif command=="stop":
        if not started :
            print("Car has already stopped")
        else:
            print("Car stopped.")
    elif command=="help":   
        print("""
start - to start the  car
stop-to stop the car
quit- to quit
             """)
    elif command=="quit":
        break
    else:
        print("I don't know about this.")