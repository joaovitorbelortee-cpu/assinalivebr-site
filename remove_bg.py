from PIL import Image
import sys

def remove_white_background(input_path, output_path):
    try:
        img = Image.open(input_path)
        img = img.convert("RGBA")
        datas = img.getdata()

        newData = []
        for item in datas:
            # Change all white (also shades of whites)
            # to transparent
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        img.putdata(newData)
        img.save(output_path, "PNG")
        print("Success")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_p = r"C:\Users\Pichau\.gemini\antigravity\brain\a176b4f1-9c40-43de-9074-8cb861c3045e\media__1771250769567.png"
    output_p = r"C:\Users\Pichau\.gemini\antigravity\scratch\assinalivebr-site\assets\logo.png"
    remove_white_background(input_p, output_p)
