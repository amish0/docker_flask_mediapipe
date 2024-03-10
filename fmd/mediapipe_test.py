import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import numpy as np

MARGIN = 10  # pixels
ROW_SIZE = 10  # pixels
FONT_SIZE = 1
FONT_THICKNESS = 1
TEXT_COLOR = (255, 0, 0)  # red

class ObjectDetector:
    def __init__(self):
        self.base_options = python.BaseOptions(model_asset_path='model/efficientdet_lite2.tflite')
        self.options = vision.ObjectDetectorOptions(base_options=self.base_options,
                                            score_threshold=0.5)
        self.detector = vision.ObjectDetector.create_from_options(self.options)
    
    def detect(self, image):
        results = self.detector.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=image))
        return results
    
    def visualize(self,
        image,
        detection_result
    ) -> np.ndarray:
        for detection in detection_result.detections:
            # Draw bounding_box
            bbox = detection.bounding_box
            start_point = bbox.origin_x, bbox.origin_y
            end_point = bbox.origin_x + bbox.width, bbox.origin_y + bbox.height
            cv2.rectangle(image, start_point, end_point, TEXT_COLOR, 3)

            # Draw label and score
            category = detection.categories[0]
            category_name = category.category_name
            probability = round(category.score, 2)
            result_text = category_name + ' (' + str(probability) + ')'
            text_location = (MARGIN + bbox.origin_x,
                            MARGIN + ROW_SIZE + bbox.origin_y)
            cv2.putText(image, result_text, text_location, cv2.FONT_HERSHEY_PLAIN,
                        FONT_SIZE, TEXT_COLOR, FONT_THICKNESS)

        return image
    
    def process(self, image):
        detection_result = self.detect(image)
        image = self.visualize(image, detection_result)
        return image
    