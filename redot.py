import os
import subprocess32 as sp
print "Please ensure that the user's /home quota is NOT full before you begin."
user = raw_input("Please input user name whose dotfiles you would like to update or replace:")
userfile = "/home/" + user
# get list of skeleton files; ignore file in subdir but include directory
dotfilelist = []
for root,dir,files in os.walk("/usr/arcts/systems/skel"):
    for file in files:
        if file == "init.el": #because it's in a subdirectory that will be added in the next for loop
            continue
        dotfilelist.append(file)
        print file

    for dr in dir:
        dotfilelist.append(dr)


print "Number of files in /skel: ",len(dotfilelist)

print dotfilelist

print ""
for item in dotfilelist:
        file = userfile+item
        skfile = "/usr/arcts/systems/skel/"+item
        old = file+".old"
        try:
            sp.check_call(["mv",file,old])

        except:
            print file," missing from /home directory.  Making this file"
            sp.check_call(["cp",skfile, file])

# generate .ssh
decision = raw_input("Would you like to remake the user's .ssh directory? (y/n)")
if decision != "y":
    print "Program finished"
    break
else:
    usersshdir = userfile + ".ssh"
    if os.path.isdir(usersshdir) == True:
       sp.check_call(["rm", "-rf", usersshdir])
    try:
        sp.check_call(["/bin/mkdir", usersshdir,  "-m 700"])
    except:
        print "Could not make .ssh directory"
        break

    try:
        sp.check_call(["/usr/bin/ssh-keygen","-t dsa","-f ~$USER/.ssh/id_dsa -N"])
    except:
         print "Could not create ssh keys"
         break

    try:
        sp.check_call(["/bin/cp", usersshdir + "/id_dsa.pub",usersshdir + "/authorized_keys2"])
    except:
        print "Could not create authorized_keys2"
        break
