from facebook import Facebook
from gi.repository import Dbusmenu
from gi.repository import GObject
from gi.repository import Gio
from gi.repository import Unity
import os, sys, optparse, time, json
import webbrowser
import pynotify
import urllib
home = os.getenv("HOME")+unicode("/.faccialibro/")
file_session = open(unicode(home)+unicode("faccialibro.session"),"r")
session_read = file_session.read()
file_session.close()
if file_session:
    session_read = session_read
else:
    session_read = ""
if session_read == "":
    fb = Facebook('261918900490462', 'c2bb3994ddcd0078e33bc9fb63daa434')
    fb.auth.createToken()
    fb.login(popup=True)
    session = fb.auth.getSession()
    webbrowser.open('http://m.facebook.com/login.php?app_id=261918900490462&cancel=http%3A%2F%2Fwww.facebook.com%2Fconnect%2Flogin_success.html&fbconnect=1&next=http%3A%2F%2Fwww.facebook.com%2Fconnect%2Fuiserver.php%3Fmethod%3Dpermissions.request%26app_id%3D261918900490462%26display%3Dwap%26redirect_uri%3Dhttp%253A%252F%252Fwww.facebook.com%252Fconnect%252Flogin_success.html%26locale%3Dit_IT%26perms%3Duser_photos%26fbconnect%3D1%26from_login%3D1&rcount=1&locale2=it_IT&_rdr',new=2)
    file_session_write = open(unicode(home)+unicode("faccialibro.session"),"w+")
    file_session_write.write(session['session_key'])
    file_session_write.close()
    file_uid_write = open(unicode(home)+unicode("faccialibro.user-id"),"w+")
    file_uid_write.write(str(session['uid']))
    file_uid_write.close()
    file_secret_write = open(unicode(home)+unicode("faccialibro.secret"),"w+")
    file_secret_write.write(str(session['secret']))
    file_secret_write.close()
else:
    file_uid = open(unicode(home)+unicode("faccialibro.user-id"),"r")
    uid_read = file_uid.read()
    file_uid.close()
    file_secret = open(unicode(home)+unicode("faccialibro.secret"),"r")
    secret_read = file_secret.read()
    file_secret.close()
    fb = Facebook(api_key='261918900490462', secret_key='c2bb3994ddcd0078e33bc9fb63daa434')
    fb.session_key = session_read
    fb.uid = uid_read
    fb.secret = secret_read
loop = GObject.MainLoop()
launcher = Unity.LauncherEntry.get_for_desktop_id ("Faccialibro.desktop")
current_unseen = 0
unseen_changed = False
def updates():
    global current_unseen, unseen_changed
    notifiche = fb.notifications.get()
    unseen = notifiche['notification_counts']['unseen'] + notifiche['messages']['unseen'] + notifiche['friend_requests_counts']['unseen']
    if unseen == current_unseen:
        unseen_changed = False
    elif unseen > 0:
        launcher.set_property("count", unseen)
        launcher.set_property("count_visible", True)
        if unseen > current_unseen:
            unseen_changed = True
        current_unseen = True
    else:
        launcher.set_property("count", 0)
        launcher.set_property("count_visible", False)
        current_unseen = 0
        unseen_changed = False
    return True
def update_urgency():
    global unseen_changed
    if unseen_changed:
        launcher.set_property("urgent", True)
        return True
    else:
        launcher.set_property("urgent", False)
        return True
def get_updates():
    global current_unseen
    updates()
    update_urgency()
    return True
input = sys.argv[1]
if input=="none":
    GObject.timeout_add_seconds(1, get_updates)
    loop.run()
else:
    launcher.set_property("progress_visible",True)
    launcher.set_property("progress",0.00)
    file = open(unicode(home)+"aid","r")
    read = file.read()
    file.close()
    if read == "":
        read = ""
    launcher.set_property("progress",20.00)
    upload = fb.photos.upload(input,read)
    launcher.set_property("progress",80.00)
    save = unicode("/tmp/")+unicode(upload['story_fbid'])+unicode(".jpg")
    urllib.urlretrieve(upload['src_small'],save)
    bubble = pynotify.Notification("Faccialibro - PhotoUpload", "Your image has been uploaded", save)
    bubble.set_timeout(500)
    bubble.show()
    launcher.set_property("progress",100.00)
    launcher.set_property("progress_visible",False)
    exit()