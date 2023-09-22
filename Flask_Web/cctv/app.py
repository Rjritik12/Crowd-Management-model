from flask import Flask, render_template, Response
# import cv2
# import cvlib as cv
# from cvlib.object_detection import draw_bbox
# from vidgear.gears import CamGear

# app = Flask(__name__)

# @app.route('/video')
# def video():
#     return render_template('video.')

# @app.route('/video_feed')
# def video_feed():
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


# def generate_frames():
#     stream = CamGear(source='https://www.youtube.com/live/nE8qkw9u7tQ?si=L01zxLfSnABzazWM', stream_mode=True, logging=True).start()
#     count = 0
#     while True:
#         frame = stream.read()
#         count += 1
#         if count % 6 != 0:
#             continue
        
#         frame = cv2.resize(frame, (1020, 600))
#         bbox, label, conf = cv.detect_common_objects(frame)
#         frame = draw_bbox(frame, bbox, label, conf)
#         c = label.count('person')
#         cv2.putText(frame, str(c), (50, 60), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 3))

#         _, buffer = cv2.imencode('.jpg', frame)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                 b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# if _name_ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, Response
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from vidgear.gears import CamGear

app = Flask(__name__)

@app.route('/video')
def video():
    return render_template('video.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


def generate_frames():
    stream = CamGear(source='https://www.youtube.com/live/St7aTfoIdYQ?si=BREt_ZhBYC_tk5IP', stream_mode=True, logging=True).start()
    count = 0
    while True:
        frame = stream.read()
        count += 1
        if count % 6 != 0:
            continue
        
        frame = cv2.resize(frame, (1020, 600))
        bbox, label, conf = cv.detect_common_objects(frame)
        frame = draw_bbox(frame, bbox, label, conf)
        c = label.count('person')
        cv2.putText(frame, str(c), (50, 60), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 3))

        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

if __name__ == "__main__":
    app.run(debug=True)