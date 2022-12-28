# Real World Problem  - The company you're working in changes the domain name so it needs to change all emails to be on the new email...

# Example code

# This function will work in all domains
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:  # We make sure to check the concatenation of the "@" sign and the old domain are contained in email
        # Find out the index of the old domain that starts at "@" and the old_domain
        index = email.index("@" + old_domain)
        # this will replace the old email
        new_email = email[:index] + "@" + new_domain
        return new_email  # we return new email
    return email  # else we return if the email doesn't contain the Old Domain
