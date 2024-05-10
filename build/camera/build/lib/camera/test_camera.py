import cv2
import sys

def is_camera_available(camera_index):
    try:
        cap = cv2.VideoCapture(camera_index)
        if cap.isOpened():
            cap.release()
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def display_camera_feed(camera_index):
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print(f"Camera {camera_index} is not available.")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error reading frame")
            break

        cv2.imshow(f"Camera {camera_index}", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_camera.py <camera_index>")
        sys.exit(1)

    camera_index = sys.argv[1]

    if is_camera_available(camera_index):
        print(f"Camera {camera_index} is available. Press 'q' to quit the feed.")
        display_camera_feed(camera_index)
    else:
        print(f"Camera {camera_index} is not available.")
