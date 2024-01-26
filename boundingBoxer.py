import cv2

def draw_bounding_boxes(image_path, boxes):
    # Read the image
    image = cv2.imread(image_path)

    # Get image dimensions
    height, width, _ = image.shape

    # Draw bounding boxes on the image
    for box in boxes:
        xmin, ymin, xmax, ymax = [int(val * width) if i % 2 == 0 else int(val * height) for i, val in enumerate(box)]
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

    # Display the image with bounding boxes
    cv2.imshow('Image with Bounding Boxes', image)

if __name__ == "__main__":
    while True:
        # Get input for bounding box coordinates
        num_boxes = int(input("Enter the number of bounding boxes: "))
        
        boxes = []
        for i in range(num_boxes):
            box_str = input(f"Enter bounding box coordinates for box {i + 1} in format [xmin, ymin, xmax, ymax]: ")
            box = [float(coord.strip()) for coord in box_str.strip('[]').split(',')]
            boxes.append(box)

        # Get input for image path
        image_path = input("Enter the path to the image: ")

        # Draw bounding boxes and display the image
        draw_bounding_boxes(image_path, boxes)

        # Wait for a key press and close the image window
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Ask if the user wants to process another image
        another_image = input("Do you want to process another image? (yes/no): ")
        if another_image.lower() != 'yes':
            break
