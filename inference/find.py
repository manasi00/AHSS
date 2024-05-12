from deepface import DeepFace as df
import os
import cv2
from pathlib import Path
import datetime as dt
import sql

def find_faces(img_path, db_path):
    result = df.find(img_path = img_path, db_path = db_path, model_name = 'VGG-Face', enforce_detection = True, detector_backend = 'mtcnn')
    return result

while True:
    for file in os.listdir('./inference/face_image/exit'):
        if file.endswith('.jpg'):
            try:
                result = find_faces(f'./inference/face_image/exit/{file}', './inference/face_image/enter')
                for i in range(len(result[0]['identity'])):
                    print(Path(result[0]['identity'][i]))
                
                if result[0]['identity'][0]:
                    im_path = result[0]['identity'][0]
                    new_path = "./frontend/static/events/"
                    if not os.path.exists(new_path):
                        os.makedirs(new_path)
                    im_copy = cv2.imread(im_path)
                    cv2.imwrite(new_path+file, im_copy)
                    conn = sql.create_connection()             
                    cursor = conn.cursor()
                    query = "UPDATE Events SET face_path=?, exited_at = ? WHERE face_path = ?"
                    cursor.execute(query, ('events/'+file, dt.datetime.now(), str(Path(im_path))))
                    conn.commit()
                    os.remove(f'./inference/face_image/exit/{file}')
                    os.remove(im_path)
                    conn.close()
                
            except Exception as e:
                print(e)
    print('No new faces found in exit folder')