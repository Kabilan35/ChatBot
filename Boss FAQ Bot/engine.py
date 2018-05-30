
##dict of response for each type of intent
intent_response_dict = {
    "intro": ["This is a BOSS FAQ bot. One stop-shop to all your BOSS related queries"],
    "greet":["hey","hello","hi","hi hello","hello there"],
    "goodbye":["Bye","goodbye","See you"],
    "affirm":["yes","yep","yeah","indeed","good","great","ok","that's right"]

}
query_dict = {
    "ip address" : "use the command \"sudo ipconfig\"",
    "boss" : "BOSS is Bharat Operating System Solutions. An Indian GNU/Linux distribution customized for Indian environment.",
    "operating system" : "Software that coordinates between the hardware and other parts of the computer to run other software is called an operating system, or the OS.",
    "variants of BOSS" : "BOSS is available as Desktop version, server edition and educational versions.",
    "difference betweem BOSS and EduBOSS" : "Desktop version is for office and generic purpose whereas EduBOSS is designed and developed for Schools. ",
    "cost": "It's free of cost.",
    "version" : "Check Applications -> System Tools -> Settings -> Details -> Overview or run the following command in terminal, “lsb_release -a”.",
    "cd":"Send a request mail to bosslinux@cdac.in mentioning your complete postal address."
}
bossquery_response_dict = {
    "free copy/cd/dvd" : "Sent a request mail to bosslinux@cdac.in mentioning your complete postal address",
    "email id" : "Send your queries to bosslinux@cdac.in",
    "email" : "Send your queries to bosslinux@cdac.in"
}
bossquery_link_dict = {
    "download" : "Download from https://bosslinux.in/downloads or send a request mail to bosslinux@cdac.in mentioning your complete postal address.",
    "get boss" : "Download from <href> https://bosslinux.in/downloads </href> or sent a request mail to bosslinux@cdac.in mentioning your complete postal address."
}
boss_query_value_dict = {
    "latest version of boss":"Desktop version 6.0",
    "latest version of eduboss": "4.1",
    "debian based linux" : "Yes.  BOSS is a debian based linux.",
    "redhat based linux" : "No.  BOSS is a debian based linux.",
    "boss linux" : "No.  But, there are many FOSS equivalent for Microsoft Office suite like LibreOffice, Abi Word etc., are available in BOSS linux.",
}
boss_extra = {
    "boss" : "BOSS is Bharat Operating System Solutions. An Indian GNU/Linux distribution customized for Indian environment.",
    "eduboss" : "An educational variant of BOSS GNU/Linux focusing Indian schools.",
    "ferret" : "Yes. Open Applications -> Utilities -> Terminal and run “sudo apt-get update; sudo apt-get install ferret”",
    "contact" : "Toll-Free Number: 1800 4250 455",
    "Microsoft Office" : "No.  But, there are many FOSS equivalent for Microsoft Office suite like LibreOffice, Abi Word etc., are available in BOSS linux.",
    "developed" : "BOSS Linux was developed by CDAC, Chennai.",
    "support windows" : "No.  Both are two different operating systems.",
    "email id" : "Send your queries to bosslinux@cdac.in",
    "minimum requirements" : "To install BOSS , you need to have a minimum of 10.0 GB of hard disk space, 512 MB of RAM and a DVD­ ROM drive.",
    "windows and BOSS" : "Windows is a closed-source operating system and BOSS is an open source linux based operating system.",
    "download" : "Download from https://ask.otc.nic.in/downloads/os/BOSS_downloads/boss-6.1-i386-DVD-19082015.iso", #done
    "get boss linux" : "Download from https://bosslinux.in/downloads or send a request mail to bosslinux@cdac.in mentioning your complete postal address.",
    "install" : "Refer http://downloads.bosslinux.in/usermanual/BOSS_Anoop_Updated_Installation_Manual.pdf",

}

def boss_info(entities):
    if entities == None:
        return "Could not find out specific information about this ..." +  bossquery_response_dict["email"]
    # if len(entities) == 1:
    #     return bossquery_response_dict[entities[0]]
    for ent in entities:
        qtype = ent["type"]
        qval = ent["entity"]
        print(qval)
        if qtype == "extra":
            return boss_extra[qval]
    return "Contact us through " + bossquery_response_dict["email"]

def boss_query(entities):
    if entities == None:
        return "Could not query this ..." + bossquery_response_dict["email"]
    for ent in entities:
        qtype = ent["type"]
        qval = ent["entity"]
        print(qval)
        if qtype == "extra":
            return boss_extra[qval]
        if qtype == "Information":
            return query_dict[qval]
        if qtype == "Product Information":
            return boss_query_value_dict[qval]
        if qtype == "Contact":
            return bossquery_response_dict[qval]
        if qtype == "Link Information":
            return bossquery_link_dict[qval]

        return bossquery_response_dict[entities[0]]
    return "Sorry.." + bossquery_response_dict["email"]