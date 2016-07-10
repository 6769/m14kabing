使用指南：
faceDB:文件夹安照数组顺序存入有效人脸图片，作为启动训练数据。
namelist.py:设置faceDB内的数组和该组人脸名字的关系，目前只有名字属性。
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
                  