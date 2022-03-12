from PIL import Image, ImageDraw

def framer(image, frame = 10):
    image_open = Image.open(image)
    image_width, image_height = image_open.size
    canvas_width, canvas_height = image_width + frame * 2, image_height + frame *2
    canvas_image = Image.new("RGB", (canvas_width, canvas_height))
    canvas_draw = ImageDraw.Draw(canvas_image)
    canvas_draw.rectangle([(canvas_width, canvas_height / 2), (0, 0)], fill = (0, 90, 187))
    canvas_draw.rectangle([(0, canvas_height / 2), (canvas_width, canvas_height)], fill = (255, 213, 0))
    canvas_image.paste(image_open, (frame, frame))
    return(canvas_image)
