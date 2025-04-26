# 🔢 Age Calculator Program
# 👨‍💻 Developed by: Ali
# 📅 DOB Used: 2001-08-17

from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()  # Get today's date
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")  # Convert input to date
    age = today.year - birthdate.year

    # Subtract 1 if birthday hasn't occurred yet this year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1

    return age

if __name__ == "__main__":
    print("🎂 Welcome to the Age Calculator Program!")
    print("👋 Hello Ali!")
    
    # Fixed DOB for this example
    dob = "2001-08-17"
    print(f"📌 Your date of birth is: {dob}")
    
    age = calculate_age(dob)
    print(f"🎉 You are {age} years old.")

