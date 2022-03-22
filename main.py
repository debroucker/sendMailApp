# coding: utf-8

import json
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

def getLinesOfFile(f) :
    readFile = open(f, "r", encoding="utf8")
    lines = readFile.readlines()
    readFile.close()
    return [line.replace('\n', '').strip() for line in lines]

def getContentOfFile(f) :
    readFile = open(f, "r", encoding="utf8")
    content = readFile.read()
    readFile.close()
    return content

def writeInFile(f, res) :
    fileToWrite = open(f, "w", encoding="utf-8")
    fileToWrite.write(res)
    fileToWrite.close()

def addInFile(f, res) :
    fileToAdd = open(f, "a", encoding="utf-8")
    fileToAdd.write(res)
    fileToAdd.close()

def jsonToDict(f) : 
    with open(f, encoding="utf8") as json_data_file:
        return json.load(json_data_file)

def init_mail(fromAddr, password):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromAddr, password)
    return s

def sendMail(s, fromAddr, toAddr, files, body, subject) :
    try :
        msg = MIMEMultipart() 
        msg['From'] = fromAddr 
        msg['To'] = toAddr 
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        for f in files :
            name = f.split('/')[-1]
            attachment = open(f.strip(), "rb")
            p = MIMEBase('application', 'octet-stream') 
            p.set_payload((attachment).read()) 
            encoders.encode_base64(p) 
            p.add_header('Content-Disposition', f"attachment; filename={name}")
            msg.attach(p) 
        text = msg.as_string()
        s.sendmail(fromAddr, toAddr, text)
        return True
    except :
        return False

def main() : 
    #init
    res = ""
    body = getContentOfFile("body.txt")
    d = jsonToDict("config.json")
    alreadySend = getLinesOfFile("already_send.txt")
    notSend = getLinesOfFile("not_send.txt")
    #mail var
    mail = d['mail']
    pw = d['pw']
    try :
        s = init_mail(mail, pw)
        for l in notSend : 
            addr = l.strip()
            if addr != "":
                if addr not in alreadySend : 
                    if sendMail(s, mail, addr, d["files"].split(","), body, d["subject"]) : 
                        print(f"mail sended to {addr}")
                        addInFile("already_send.txt", addr + "\n")
                    else : 
                        print(f"error, not sended to {addr}")
                        res += addr + "\n"
                else :
                    print(f"already sended to {addr}")
        writeInFile("not_send.txt", res)
        s.quit()
    except :
        print(f"error, not connected to mail: '{mail}' with pw: '{pw}'")

main()
