def generate_reply(category, entities):

    organization = None
    money = None
    date = None

    # Extract important entities
    for text, label in entities:

        if "Organization" in label:
            organization = text

        elif "Money" in label:
            money = text

        elif "Date" in label:
            date = text

    # Build reply
    reply = "Dear Customer,\n\n"

    reply += "Thank you for contacting our support team.\n\n"

    # Category
    reply += f"We have received your complaint regarding your {category.lower()}"

    if organization:
        reply += f" involving {organization}"

    reply += ".\n\n"

    # Transaction details
    if money and date:
        reply += f"We understand that the transaction amount of ${money} on {date} is causing concern.\n\n"

    elif money:
        reply += f"We understand that the transaction amount of ${money} is causing concern.\n\n"

    elif date:
        reply += f"We understand that the issue occurred on {date}.\n\n"

    # Department based on category
    if category == "Credit card or prepaid card":
        department = "Billing Team"

    elif category == "Checking or savings account":
        department = "Banking Support Team"

    elif category == "Mortgage":
        department = "Mortgage Support Team"

    elif category == "Student loan":
        department = "Student Loan Team"

    elif category == "Debt collection":
        department = "Debt Resolution Team"

    else:
        department = "Customer Support Team"

    reply += f"Our {department} has started investigating your complaint and will contact you within 24 hours.\n\n"

    reply += "Thank you for your patience.\n\n"

    reply += "Best Regards,\nCustomer Support Team"

    return reply