import os
home = os.getenv("HOME")+unicode("/.faccialibro/")
write = "[Desktop Entry]\nVersion=1.0\nName=Faccialibro\nComment=Facebook notify in Unity\nExec=\""+home+"faccialibro.sh\" %u\nTerminal=false\nX-MultipleArgs=true\nMimeType=image/bmp;image/gif;image/jpeg;image/jpg;image/png;\nType=Application\nIcon="+home+"facebook.png\nCategories=Network;WebBrowser;\nX-Ayatana-Desktop-Shortcuts=SelAlbum;Notifications;Messages;Friends\nName[it_IT]=Faccialibro\nComment[it_IT]=Notifiche di Facebook su Unity\n\n[SelAlbum Shortcut Group]\nName=Select an Album\nExec=\""+home+"faccialibro.sh\" setAlbum\nTargetEnvironment=Unity\nName[it_IT]=Seleziona un album\n\n[Notifications Shortcut Group]\nName=Notifications\nExec=ndg-open 'http://www.facebook.com/notifications.php'\nTargetEnvironment=Unity\nName[it_IT]=Notifiche\n\n[Messages Shortcut Group]\nName=Messages\nExec=xdg-open 'http://www.facebook.com/?sk=messages'\nTargetEnvironment=Unity\nName[it_IT]=Messaggi\n\n[Friends Shortcut Group]\nName=Friends\nExec=xdg-open 'http://www.facebook.com/friends/edit/'\nTargetEnvironment=Unity\nName[it_IT]=Amici"
faccialibro_desktop = open("Faccialibro.desktop","w+")
faccialibro_desktop.write(write)
faccialibro_desktop.close()
print "Installed!"
