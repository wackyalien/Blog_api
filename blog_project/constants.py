from django.conf import settings

PORT_SERVER = "8000"

#URI_BASE = 'http://localhost:' + PORT_SERVER
URI_BASE = 'http://35.184.85.134:' + PORT_SERVER


URI_AUTH = URI_BASE + '/auth/token/'

# Firebase Server Key

fcm_server_key = "AAAAm_fBaRM:APA91bFWILJup_sfBDmbofUrCPKnosJfyGvKod_5m7dxWuKQa54S3sKzeA0SptINqUGroMTJJwP6212BcHK8EqlSPb31Y-5BsPYNazsZRZPHx-71j543gmYoRN48DI75XRzIJOKtgy6K"


days_of_the_week = {
    'Monday': 'Monday',
    'Tuesday': 'Tuesday',
    'Wednesday': 'Wednesday',
    'Thursday': 'Thursday',
    'Friday': 'Friday',
    'Saturday': 'Saturday',
    'Sunday': 'Sunday',
}
days_of_the_week_choices = [tuple([v, k]) for k, v in days_of_the_week.items()]

language = {
    'hi': 'Hindi',
    'en-uk': 'English UK',
    'en-usa': 'English USA'
}

language_choices = [tuple([v, k]) for k, v in language.items()]

level = {
    'high': 'high',
    'medium': 'medium',
    'low': 'low'
}
level_choices = [tuple([v, k]) for k, v in level.items()]

sex = {
    'FEMALE': 'FEMALE',
    'MALE': 'MALE',
    'TRANSGENDER': 'TRANSGENDER',
    'NOT_SPECIFIED': 'NOT_SPECIFIED'
}
sex_choices = [tuple([v, k]) for k, v in sex.items()]
sex_list = [k[0] for k in sex.items()]

profile_pic_source = {
    'CAMERA': 'CAMERA',
    'GALLERY': 'GALLERY',
}
profile_pic_source_choices = [tuple([v, k]) for k, v in profile_pic_source.items()]
profile_pic_source_list = [k[0] for k in profile_pic_source.items()]

occupation = {
    'STUDENT': 'Student',
    'UNEMPLOYED': 'Unemployed',
    'SELF EMPLOYED': 'Self Employed',
    'PUBLIC EMPLOYEE': 'Public Employee',
    'PRIVATE EMPLOYEE': 'Private Employee',
}
occupation_choices = [tuple([v, k]) for k, v in occupation.items()]

category = {
    'GN': 'General',
    'SC': 'Scheduled categorys',
    'ST': 'Scheduled Tribes',
    'OBC': 'Other Backward Classes',
    'SBC': 'Special Backwar Classes',
    'MN': 'Minority',
}
category_choices = [tuple([v, k]) for k, v in category.items()]

maritial_status = {

}
maritial_status_choices = [tuple([v, k]) for k, v in maritial_status.items()]

education_status = {
    'MATRICULATE': '10th Pass',
    'INTERMEDIATE': '12th Pass',
    'GRADUATE': 'Bachelors(1st) Degree',
    'POST GRADUATE': 'Masters(2nd) Degree',
}
education_status_choices = [tuple([v, k]) for k, v in education_status.items()]


ERROR_CONFIG = {
    'ERR-DJNG-001': ("No CODE Passed", "Error Message"),
    'ERR-DJNG-002': ("No Object found", "Error Message"),
    'ERR-DJNG-003': ("Multiple Objects Returned", "Error Message"),
    'ERR-GNRL-001': ("Invalid Phone Number", "Error Message"),
    'ERR-GNRL-002': ("Invalid Email Address", "Error Message"),
    'ERR-AUTH-001': ("Invalid Credentials", "Error Message"),
    'ERR-AUTH-002': ("Unsuccessful exchange of Authorization Code for an Access Token", "Error Message"),
    'ERR-AUTH-003': ("Incorrect password", "Error Message"),
    'ERR-AUTH-004': ("Passwords do not match", "Error Message"),
    'ERR-AUTH-005': ("Invalid Phone OTP", "Error Message"),
    'ERR-ADMIN-001': ("No admin permission",  "Error Message"),
    'ERR-USER-001': ("No User found", "Error Message"),
    'ERR-USER-002': ("User Already Exists", "Error Message"),
    'ERR-USER-003': ("User Blocked", "Error Message"),
    'ERR-USER-004': ("User Already Exists with Phone Number", "Error Message"),
    'ERR-USER-005': ("User Already Exists with Email ID", "Error Message"),
    'ERR-USER-006': ("User missing OTP details", "Error Message"),
    'ERR-USER-007': ("User permission denied", "Error Message"),
    'ERR-USER-008': ("User Already Exists with username", "Error Message"),
    'ERR-USER-009': ("User does not exists for given token", "Error Message"),
    'ERR-CONT-001': ("No such contact founder with email", "Error Message"),
    'ERR-CONT-002': ("No such contact founder with phone", "Error Message"),
    'ERR-COUR-001': ("No such course found", "Error Message"),
    'ERR-COUR-002': ("User is not enrolled into any such course", "Error Message"),
    'ERR-COUR-003': ("Cannot download certificate unless course completed", "Error Message"),
    'ERR-EVNT-001': ("Event has a false operation", "Error Message"),
    'ERR-EVNT-002': ("Event is no longer active", "Error Message"),
    'ERR-EVNT-003': ("User cannot be a rescuer", "Error Message"),
    'ERR-EVNT-004': ("Rescuer has already been assigned", "Error Message"),
    'ERR-EVNT-005': ("Event is no longer active", "Error Message"),
    'ERR-PMNT-001': ("Payment Failure", "Error Message"),
    'ERR-DB-001': ("Databse create Error", "Error while creating a database entry"),
    'ERR0002': ("Linkedin Access Token not present in LinkedIn response", "Error Message"),
    'ERR0003': ("Unmatching User from UserLinkedInData Object and Function Parameter", "Error Message"),
    'ERR0007': ("Invalid Phone Number", "Error Message"),
    'ERR0009': ("Invalid Email Address", "Error Message"),
    'ERR0011': ("Invalid Phone OTP", "Error Message"),
    'ERR0012': ("No OTP in Database", "Error Message"),
}

imported_contact_sources = {
    "LINKEDIN": "0",
    "GOOGLE": "1",
    "LINK": "2",
    "PHONE": "3",
}
imported_contact_sources_choices = [tuple([v, k]) for k, v in imported_contact_sources.items()]

user_contact_states = {
    "Invite Pending": "0",
    "Invite Sent": "1",
    "Invite Reminder Sent": "2",
    "Already Member": "3",
    "Invite Success": "4",
    "Invite Failure": "5",
}
user_contact_states_choices = [tuple([v, k]) for k, v in user_contact_states.items()]
