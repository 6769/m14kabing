;
;Use Windows'TTS service to speak something.
;via cmd parameters or GUI
;
spk:=ComObjCreate("SAPI.SPVOICE")
volce="hello"
argc = %0%
;MsgBox, %argc%
if  (argc==0){
InputBox, volce, TTS, Please enter what you want to say:
len:=Strlen(volce) 
if ErrorLevel
    ;MsgBox, CANCEL was pressed.
	argc:=0

else
	if(len>0)
    spk.Speak(volce)

}else{
	
	volce=%1%
	spk.Speak(volce)
}
Exit, 0