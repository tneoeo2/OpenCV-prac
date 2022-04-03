 ##? 카메라 출력하기

import cv2


#cv2.VideoCapturee(idx) : idx(카메라 장치번호(ID)연결)
#  --노트북 내장카메라 : 0
#  -- 외장카메라 : 1~n
capture = cv2.VideoCapture(0)  #비디오 출력클래스: 내장/외장 카메라 받아옴

##capture.set(propid, value) : 카메라 속성, 값 설정
# propid : 변경하려는 카메라 설정
# value : 카메라 설정의 속성값
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  #프레임 크기 설정

while cv2.waitKey(33) < 0:  #waitKey() : time(시간)동안 키 입력이 있을 때 까지 프로그램 지연
    ##33초마다 반복문 실행
    ##waitKey(0)일 경우 지속적으로 키입력을 검사하여 프레임이 넘어가지 않는다.
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)
    
capture.release()  #메모리 해제 메서드 (카메라 장치에서 받아온 메모리 해제)
cv2.destroyAllWindows()  # 모든 윈도우창 닫기
#cv2.destroyWindow(winname) : 특정 윈도우창 닫기