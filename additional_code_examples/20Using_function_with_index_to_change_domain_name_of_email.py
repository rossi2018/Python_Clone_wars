def replace_domain(email,old_domain,new_domain):
    if "@" + old_domain in email:
        index=email.index("@" + old_domain)
        new_domain=email[:index] + "@" + new_domain
        return new_domain
    return email

replace_domain()