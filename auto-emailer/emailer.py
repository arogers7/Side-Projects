import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

uba = "uba.mentorship.program@gmail.com"
menteeStanding, menteeCareer, menteeMajor, menteeEmail, menteeName, menteeMessage, mentorStanding, mentorCareer, mentorMajor, mentorEmail, mentorName, mentorMessage = np.loadtxt('MentorData.csv', delimiter=',', unpack=True, dtype='str')

menteeMSG = MIMEMultipart()
menteeMSG['Subject'] = "UBA Mentorship Match"
menteeMSG['From'] = uba

mentorMSG = MIMEMultipart()
mentorMSG['Subject'] = "UBA Mentorship Match"
mentorMSG['From'] = uba

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(uba,'ubamentorship')
#server.sendmail("uba.mentorship.program@gmail.com","arogers7@buffalo.edu","hello")

#optional message
message = '\n\n{} chose to write a short message to you about their interests and extracurricular activities:\n{}\n\n'


for i in range(len(mentorStanding)):
    mentorMSG['To'] = mentorEmail[i]
    menteeMSG['To'] = menteeEmail[i]

    temptext = """Hello {},\n\nThank you for participating in the Undergraduate Biology Association's mentorship program! You have been matched with {}, a {} {} major who is interested in """




    if (menteeCareer[i] == "Medical School" or menteeCareer[i] == "Dental School"):
        temptext += "attending {}"
    elif (menteeCareer[i] == "PhD"):
        temptext += "pursuing a {}"
    elif (menteeCareer[i] == "Masters"):
        temptext += "pursuing a {} degree"
    elif (mentorCareer[i] == "Physician's Assistant Program"):
        temptext += "a {}"
    else:
         temptext += " {}"

    temptext += ".{}"

    temptext += """Please reach out to {} at {} before classes start on August 28th. Together, you should work out a place and time to meet early in the semester.

Not sure what to do when you meet? You can go for lunch or dinner at your favorite place on campus, take the train downtown, go for a walk around campus, or anything else that you two agree on.

If you're interested in more UBA events and meetings, you can find a complete list on our website (https://ubwp.buffalo.edu/ubsa-uba/), facebook page (https://www.facebook.com/UndergraduateBiologyAssociation/), and slack (ub-uba.slack.com). If you have any questions or feedback, please reply back to this email or ask on slack.

Good luck for the upcoming year!"""



    if (len(menteeMessage[i]) > 0):
        mentorMes = message.format(menteeName[i],menteeMessage[i])
    else:
        mentorMes = "\n\n"
    if (len(mentorMessage[i]) > 0):
        menteeMes = message.format(mentorName[i],mentorMessage[i])
    else:
        menteeMes = "\n\n"

    mentorBody = temptext.format(mentorName[i],menteeName[i],menteeStanding[i],menteeMajor[i],menteeCareer[i],menteeMes,menteeName[i],menteeEmail[i])

    menteeBody = temptext.format(menteeName[i],mentorName[i],mentorStanding[i],mentorMajor[i],mentorCareer[i],mentorMes,mentorName[i],mentorEmail[i])

    mentorMSG.attach(MIMEText(mentorBody,'plain'))
    menteeMSG.attach(MIMEText(menteeBody,'plain'))
    server.sendmail(uba,mentorEmail[i],mentorMSG.as_string())
    server.sendmail(uba,menteeEmail[i],menteeMSG.as_string())
server.quit()
