ʹ��ָ�ϣ�
faceDB:�ļ��а�������˳�������Ч����ͼƬ����Ϊ����ѵ�����ݡ�
namelist.py:����faceDB�ڵ�����͸����������ֵĹ�ϵ��Ŀǰֻ���������ԡ�
---------------
Handle a keypress.

        space  -> Take a screenshot,saved as (time.ctime()).png.
        escape -> Quit.
        r      -> Reverse switch of faceRecognize,(default:off)
        m      -> Move png file to faceSetDataBase.
                  Please input an integer[1,2,3,4,5...](which'll be used 
                  as label ) to tell the
                  programe how to settle current *.png. After 
                  operation,png files will be moved to 
                  
                  Normally,file tree has the structure like this 
                  (./faceDB/[label]/i.png)
                  