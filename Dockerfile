FROM rkr7x/fruits-dis:ver1.0
MAINTAINER Keisuke Kiriyama

ADD recognition_image /recognition_image
ADD call_function /call_function
ADD log /log
CMD python /call_function/call_function_with_flask.py


