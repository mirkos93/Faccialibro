import webbrowser
import string
from facebook import Facebook
import gtk
import os
class Finestra(gtk.Window):
    global fb
    global aid
    global home
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
    def __init__(self):
        gtk.Window.__init__(self, gtk.WINDOW_TOPLEVEL)
        self.set_title('FL - Faccialibro')
        #self.resize(220, 150)
        self.set_property("resizable", False)
        self.connect('destroy', self.chiudi)
        pixbuf = gtk.gdk.pixbuf_new_from_file(unicode(home)+'facebook.png')
        self.set_icon(pixbuf)

        b = gtk.Button('Select the Album!')
        b.connect('clicked', self.saveFile, None)
        b.show()
        create = gtk.Button("Create an Album")
        create.connect("clicked",self.createLink, None)
        create.show()
        global combobox
        combobox = gtk.combo_box_new_text()
        i = 0
        global albums
        albums = fb.photos.getAlbums()
        for album in albums:
            combobox.append_text(unicode(i)+unicode(" - ")+unicode(album['name']))
            i = i+1
        combobox.set_active(0)
        #combobox.connect('changed', self.changed_cb)
        combobox.show()

        label = gtk.Label("Select an album!")
        label.show()
        fixed = gtk.Fixed()
        fixed.put(label, 0, 0)
        fixed.put(combobox, 0, 20)
        fixed.put(b,0,50)
        fixed.put(create,0,80)
        fixed.show()
        self.add(fixed)

    def mostra(self):
        self.show()
        gtk.main()

    def saveFile(self, widget, data=None):
        model = combobox.get_model()
        index = combobox.get_active()
        value = model[index][0]
        value.split(" - ")
        intero = value[0]
        aid = albums[int(intero)]['aid']
        file = open(unicode(home)+"aid","w+")
        file.write(aid)
        file.close
        gtk.main_quit()

    def chiudi(self, widget, data=None):
        gtk.main_quit()
    def createLink(self, widget, data=None):
        webbrowser.open('http://www.facebook.com/albums/create.php',new=2)
if __name__ == '__main__':
    f = Finestra()
    f.mostra()