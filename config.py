###############################################################################
# SMTP configuration settings.
###############################################################################
smtp = {
    'username': 'username',
    'password': 'password',
    'host': 'email-smtp.example.com',
    'port': 587,
    'from_email': 'email-used-to-send-letters@examplecompany.gov',
}

###############################################################################
# This is the secret letter template that is used to send everyone the email.
# Note that {santa} and {recipient} are automaticly replaced by the secret
# Santa's name, and his/her recipient of their gift.
###############################################################################
email_template = {
    'James': 'james@examplecompany.gov',
    'Mary': 'mary@examplecompany.gov',
    'Nancy': 'nancy@examplecompany.gov',
    'John': 'john@examplecompany.gov',
    'Michael': 'michael@examplecompany.gov',
    'Lisa': 'lisa@examplecompany.gov',
    'David': 'david@examplecompany.gov',
    'Linda': 'linda@examplecompany.gov',
}

###############################################################################
# This contains a dictionary lookup of santa's (keys) who are not allowed to
# have particular recipients (values).
#
# If there are no incompatibles, leave this dictionary empty.
###############################################################################
incompatibles = {
    # Do not allow James to be a santa for Mary
    'James': ('Mary',),

    # Do not allow Mary to be a santa for James
    'Mary': ('James',),

    # Do not allow Nancy to be a santa for John or Mary
    'Nancy': ('John', 'Mary',),

    # Something like below is bad, Linda can't be a secret santa for anyone!
#   'Linda': ('James', 'Mary', 'Nancy', 'John', 'Michael', 'Lisa', 'David'),
}

###############################################################################
# DON'T PEAK INTO THIS FILE!
#
# This file will contain a record of what was emailed. It will reveal who is
# everyone's secret santa.
###############################################################################
secret_santa_record_file = 'secret-santa-record=file.txt'
