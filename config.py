###################################################################################################################################
# SMTP configuration settings.
###################################################################################################################################
smtp = {
    'username': 'username',
    'password': 'password',
    'host': 'email-smtp.example.com',
    'port': 587,
    'from_email': 'email-used-to-send-letters@examplecompany.gov',
}

###################################################################################################################################
# This is the secret letter template that is used to send everyone the email.
# Note that {santa} and {recipient} are automaticly replaced by the secret
# Santa's name, and his/her recipient of their gift.
###################################################################################################################################
email_template = {
    'Bailey': 'bailey@examplecompany.gov',
    'Nelson': 'nelson@examplecompany.gov',
    'Minami': 'minami@examplecompany.gov',
    'Jennifer': 'jennifer@examplecompany.gov',
    'Lopez': 'lopez@examplecompany.gov',
    'Will': 'will@examplecompany.gov',
    'Smith': 'smith@examplecompany.gov',
    'Kobe': 'kobe@examplecompany.gov',
}

###################################################################################################################################
# This contains a dictionary lookup of santa's (keys) who are not allowed to have particular recipients (values).
# If there are no incompatibles, leave this dictionary empty.
###################################################################################################################################
incompatibles = {
    # Do not allow Bailey to be a santa for Nelson
    'Bailey': ('Nelson',),

    # Do not allow Nelson to be a santa for Bailey
    'Nelson': ('Bailey',),

    # Do not allow Kobe to be a santa for Bailey or Nelson
    'Kobe': ('Bailey', 'Nelson',),

    # Something like below is bad, Bailey can't be a secret santa for anyone!
#   'Bailey': ('Nelson', 'Minami', 'Jennifer', 'Lopez', 'Will', 'Smith', 'Kobe'),
}

###################################################################################################################################
# DON'T PEAK INTO THIS FILE! This file will contain a record of what was emailed. It will reveal who is everyone's secret santa.
###################################################################################################################################
secret_santa_record_file = 'secret-santa-record=file.txt'
